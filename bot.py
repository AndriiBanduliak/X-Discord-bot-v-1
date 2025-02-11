import discord  # Importiert die Discord-Bibliothek
from discord.ext import commands, tasks  # Importiert Befehle und Hintergrundaufgaben
import tweepy  # Bibliothek für Twitter API
import os  # Ermöglicht den Zugriff auf Umgebungsvariablen
import logging  # Fügt Protokollierung (Logging) hinzu

# --- LOGGING EINSTELLEN ---
LOG_FILE = "bot.log"
if os.path.exists(LOG_FILE):
    os.rename(LOG_FILE, LOG_FILE + ".old")  # Falls die Logdatei existiert, wird sie umbenannt

logging.basicConfig(
    level=logging.INFO,  # Protokollierungslevel: INFO (zeigt normale Nachrichten und Fehler)
    format="%(asctime)s [%(levelname)s] %(message)s",  # Format der Logs
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Speichert Logs in einer Datei
        logging.StreamHandler()  # Zeigt Logs direkt in der Konsole
    ]
)

# --- DISCORD BOT EINSTELLUNGEN ---
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")  # Token aus den Umgebungsvariablen abrufen

# Discord-Bot mit speziellen Rechten (Intents) initialisieren
intents = discord.Intents.default()
intents.messages = True  # Erlaubt das Lesen und Senden von Nachrichten
intents.guilds = True  # Erlaubt die Verbindung mit Servern (Guilds)
bot = commands.Bot(command_prefix="!", intents=intents)  # Präfix für Befehle: !

# --- TWITTER (X) API EINSTELLUNGEN ---
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_SECRET = os.environ.get("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")

# Authentifizierung bei der Twitter API mit OAuth
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
twitter_api = tweepy.API(auth)


async def get_tweets(username, count=5):
    """Holt die letzten Tweets eines bestimmten Twitter-Kontos."""
    try:
        tweets = twitter_api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]
    except tweepy.TweepError as e:
        logging.error("Twitter API Fehler: %s", e)
        return []


@tasks.loop(minutes=15)
async def check_twitter():
    """Überwacht einen Twitter-Account und sendet relevante Tweets an Discord."""
    twitter_user = "elonmusk"  # Ersetze mit dem gewünschten Twitter-Account
    keywords = ["Tesla", "SpaceX"]  # Keywords für die Suche

    logging.info("Überprüfung des Twitter-Kontos: %s", twitter_user)

    tweets = await get_tweets(twitter_user, count=5)
    filtered_tweets = [tweet for tweet in tweets if any(keyword.lower() in tweet.lower() for keyword in keywords)]

    if filtered_tweets:
        channel = bot.get_channel(123456789012345678)  # Discord-Kanal-ID anpassen!
        if channel:
            for tweet in filtered_tweets:
                await channel.send(f"🚀 Neuer Tweet von @{twitter_user}:\n{tweet}")
                logging.info("Nachricht in Kanal %d gesendet", channel.id)
        else:
            logging.warning("Kanal mit ID %d nicht gefunden!", 123456789012345678)


@check_twitter.before_loop
async def before_check_twitter():
    """Wartet, bis der Bot bereit ist, bevor die Twitter-Überwachung beginnt."""
    await bot.wait_until_ready()


@bot.event
async def on_ready():
    """Wird ausgeführt, wenn der Bot erfolgreich verbunden ist."""
    logging.info("Bot %s ist online!", bot.user.name)
    check_twitter.start()  # Startet die Überwachung von Twitter


# --- DISCORD BEFEHLE ---
@bot.command()
async def twitter(ctx, username: str, count: int = 5):
    """Befehl !twitter <Benutzername> <Anzahl> - Zeigt die letzten Tweets eines Nutzers."""
    await ctx.send(f"🔍 Lade die letzten {count} Tweets von @{username}...")
    tweets = await get_tweets(username, count)

    if tweets:
        for tweet in tweets:
            await ctx.send(f"📝 {tweet}")
    else:
        await ctx.send("❌ Keine Tweets gefunden!")


@bot.command()
async def helpme(ctx):
    """Befehl !helpme - Zeigt eine Liste aller verfügbaren Befehle."""
    help_text = """
    **🤖 Verfügbare Befehle:**
    `!twitter <Benutzername> <Anzahl>` - Holt die letzten Tweets eines Nutzers.
    `!helpme` - Zeigt diese Hilfe an.
    """
    await ctx.send(help_text)


# --- BOT STARTEN ---
if __name__ == "__main__":
    if not TOKEN:
        logging.error("Fehler: DISCORD_BOT_TOKEN nicht gesetzt.")
    else:
        logging.info("Starte den Bot...")
        bot.run(TOKEN)

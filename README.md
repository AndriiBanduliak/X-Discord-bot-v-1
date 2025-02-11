# Discord Twitter Bot

This is a simple Discord bot that can fetch and display tweets from Twitter (now X).  It can also monitor a specific Twitter account for keywords and post matching tweets to a Discord channel.

## Table of Contents

*   [Features](#features)
*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
*   [Configuration](#configuration)
*   [Usage](#usage)
*   [Commands](#commands)
*   [Support](#support)

## Features

*   **Fetch Tweets:** Retrieve the latest tweets from any Twitter user.
*   **Keyword Monitoring:**  Automatically monitor a Twitter account for specific keywords and post matching tweets to a Discord channel.
*   **Logging:**  Logs bot activity to a file and the console for debugging.
*   **Help Command:** Provides a list of available commands within Discord.

## Prerequisites

*   Python 3.6 or higher
*   A Discord bot token. [How to create a Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html)
*   A Twitter (X) API key and secret. [How to get Twitter API Keys](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    ./setup.sh
    ```
    This script does the following:
    * Creates a virtual environment named `venv`.
    * Activates the virtual environment.
    * Installs the required Python packages from `requirements.txt`.

3. **Activate the virtual enviornment after the first run.**

    ```bash
    source venv/bin/activate
    ```

## Configuration

1.  **Set environment variables:** You need to set the following environment variables:

    *   `DISCORD_BOT_TOKEN`: Your Discord bot token.
    *   `TWITTER_API_KEY`: Your Twitter API key.
    *   `TWITTER_API_SECRET`: Your Twitter API secret.
    *   `TWITTER_BEARER_TOKEN`: Your Twitter Bearer Token.
    *   `TWITTER_ACCESS_TOKEN`: Your Twitter Access Token.
    *   `TWITTER_ACCESS_SECRET`: Your Twitter Access Secret.

    You can set these variables directly in your terminal before running the bot, or you can use a `.env` file (not included in this example for security reasons).  Example of setting in the terminal:

    ```bash
    export DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"
    export TWITTER_API_KEY="YOUR_TWITTER_API_KEY"
    export TWITTER_API_SECRET="YOUR_TWITTER_API_SECRET"
    export TWITTER_BEARER_TOKEN="YOUR_TWITTER_BEARER_TOKEN"
    export TWITTER_ACCESS_TOKEN="YOUR_TWITTER_ACCESS_TOKEN"
    export TWITTER_ACCESS_SECRET="YOUR_TWITTER_ACCESS_SECRET"

    ```

2.  **Configure the bot:**

    *   **Discord Channel ID:**  In the `bot.py` file, find the line `channel = bot.get_channel(123456789012345678)` and replace `123456789012345678` with the ID of the Discord channel where you want the bot to post tweets.  [How to get a Discord Channel ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
    *   **Twitter Username:** In the `bot.py` file, find the line `twitter_user = "elonmusk"` and replace `"elonmusk"` with the Twitter username you want to monitor.
    *   **Keywords:** In the `bot.py` file, find the line `keywords = ["Tesla", "SpaceX"]` and replace `["Tesla", "SpaceX"]` with the keywords you want to search for in tweets.

## Usage

1.  **Run the bot:**

    ```bash
    python bot.py
    ```

## Commands

The bot responds to the following commands in Discord:

*   `!twitter <username> <count>`:  Fetches the last `<count>` tweets from the specified `<username>`.  For example: `!twitter elonmusk 5`
*   `!helpme`: Displays a list of available commands.


---

# Discord Twitter Bot (Deutsch)

Dies ist ein einfacher Discord-Bot, der Tweets von Twitter (jetzt X) abrufen und anzeigen kann. Er kann auch ein bestimmtes Twitter-Konto auf Schlüsselwörter überwachen und passende Tweets in einen Discord-Kanal posten.

## Inhaltsverzeichnis

*   [Funktionen](#funktionen)
*   [Voraussetzungen](#voraussetzungen)
*   [Installation](#installation-deutsch)
*   [Konfiguration](#konfiguration-deutsch)
*   [Verwendung](#verwendung-deutsch)
*   [Befehle](#befehle-deutsch)
*   [Unterstützung](#unterstützung-deutsch)

## Funktionen

*   **Tweets abrufen:** Ruft die neuesten Tweets von einem beliebigen Twitter-Benutzer ab.
*   **Schlüsselwortüberwachung:** Überwacht automatisch ein Twitter-Konto auf bestimmte Schlüsselwörter und postet passende Tweets in einen Discord-Kanal.
*   **Protokollierung:** Protokolliert die Bot-Aktivität zur Fehlerbehebung in einer Datei und in der Konsole.
*   **Hilfe-Befehl:** Zeigt eine Liste der verfügbaren Befehle innerhalb von Discord an.

## Voraussetzungen

*   Python 3.6 oder höher
*   Ein Discord-Bot-Token. [So erstellen Sie einen Discord-Bot](https://discordpy.readthedocs.io/en/latest/discord.html)
*   Einen Twitter (X) API-Schlüssel und Secret. [So erhalten Sie Twitter API-Schlüssel](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

## Installation (Deutsch)

1.  **Repository klonen:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Virtuelle Umgebung erstellen und aktivieren:**
    ```bash
    ./setup.sh
    ```
    Dieses Skript macht Folgendes:
    * Erstellt eine virtuelle Umgebung namens `venv`.
    * Aktiviert die virtuelle Umgebung.
    * Installiert die erforderlichen Python-Pakete aus `requirements.txt`.

3. **Aktiviere die virtuelle Umgebung nach der ersten Ausführung:**

    ```bash
    source venv/bin/activate
    ```

## Konfiguration (Deutsch)

1.  **Umgebungsvariablen setzen:** Sie müssen die folgenden Umgebungsvariablen setzen:

    *   `DISCORD_BOT_TOKEN`: Ihr Discord-Bot-Token.
    *   `TWITTER_API_KEY`: Ihr Twitter API-Schlüssel.
    *   `TWITTER_API_SECRET`: Ihr Twitter API-Secret.
    *   `TWITTER_BEARER_TOKEN`: Ihr Twitter Bearer Token.
    *   `TWITTER_ACCESS_TOKEN`: Ihr Twitter Access Token.
    *   `TWITTER_ACCESS_SECRET`: Ihr Twitter Access Secret.

    Sie können diese Variablen direkt in Ihrem Terminal setzen, bevor Sie den Bot ausführen, oder Sie können eine `.env`-Datei verwenden (aus Sicherheitsgründen nicht in diesem Beispiel enthalten). Beispiel für das Setzen im Terminal:

    ```bash
    export DISCORD_BOT_TOKEN="IHR_DISCORD_BOT_TOKEN"
    export TWITTER_API_KEY="IHR_TWITTER_API_KEY"
    export TWITTER_API_SECRET="IHR_TWITTER_API_SECRET"
    export TWITTER_BEARER_TOKEN="IHR_TWITTER_BEARER_TOKEN"
    export TWITTER_ACCESS_TOKEN="IHR_TWITTER_ACCESS_TOKEN"
    export TWITTER_ACCESS_SECRET="IHR_TWITTER_ACCESS_SECRET"
    ```

2.  **Bot konfigurieren:**

    *   **Discord-Kanal-ID:** Suchen Sie in der Datei `bot.py` die Zeile `channel = bot.get_channel(123456789012345678)` und ersetzen Sie `123456789012345678` durch die ID des Discord-Kanals, in dem der Bot Tweets posten soll. [So erhalten Sie eine Discord-Kanal-ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
    *   **Twitter-Benutzername:** Suchen Sie in der Datei `bot.py` die Zeile `twitter_user = "elonmusk"` und ersetzen Sie `"elonmusk"` durch den Twitter-Benutzernamen, den Sie überwachen möchten.
    *   **Schlüsselwörter:** Suchen Sie in der Datei `bot.py` die Zeile `keywords = ["Tesla", "SpaceX"]` und ersetzen Sie `["Tesla", "SpaceX"]` durch die Schlüsselwörter, nach denen Sie in Tweets suchen möchten.

## Verwendung (Deutsch)

1.  **Bot ausführen:**

    ```bash
    python bot.py
    ```

## Befehle (Deutsch)

Der Bot reagiert in Discord auf die folgenden Befehle:

*   `!twitter <Benutzername> <Anzahl>`: Ruft die letzten `<Anzahl>` Tweets von dem angegebenen `<Benutzernamen>` ab. Beispiel: `!twitter elonmusk 5`
*   `!helpme`: Zeigt eine Liste der verfügbaren Befehle an.

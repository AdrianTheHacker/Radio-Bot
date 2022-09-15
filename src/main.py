from dotenv import load_dotenv

from discord_client import bot
from audio_grabber import download_song

from os import environ


def main():
    load_dotenv()

    print("Hard Bass")
    # bot.run(environ["DISCORD_BOT_TOKEN"])
    download_song("https://www.youtube.com/watch?v=fnFG6HXcsKQ&ab_channel=AlanAztec", "hard_bass")
    

if __name__ == "__main__":
    main()

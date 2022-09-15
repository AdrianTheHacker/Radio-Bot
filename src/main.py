from dotenv import load_dotenv

from discord_client import bot

from os import environ


def main():
    load_dotenv()

    print("Hard Bass")
    bot.run(environ["DISCORD_BOT_TOKEN"])
    

if __name__ == "__main__":
    main()

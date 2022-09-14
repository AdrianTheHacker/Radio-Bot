import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi {ctx.message.author}")


@bot.command()
async def join(ctx, voice_channel="Gentlemen's Club"):
    # TODO 
    # -> Allow bot to join different voice channels without having to run ~leave
    # -> Fix bug with bot crashing after running ~join when bot is already inside of a voice channel
    # -> Fix bug with bot crashing when voice channel doesn't exist

    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=voice_channel) # sets "voice_channel" to a given voice channel
    await voice_channel.connect()


@bot.command()
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client.is_connected():
        await voice_client.disconnect()

    else: 
        await ctx.send(f"{bot.user.name} isn't inside of a voice channel right now")

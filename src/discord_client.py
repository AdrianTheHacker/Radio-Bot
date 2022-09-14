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


# @bot.command()
# async def add(ctx, video_link, name):
#     # Adds song to the hard_bass_library
    
#     # Download the video as an mp3
#     # Add the video's audio to the hard_bass_library
#     # -> Bot will have to check for audio files with the same names
    
#     voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
#     await voice.play(discord.FFmpegPCMAudio(executable=constants.FFMPEG_PATH, source=constants.AUDIO_FILE_PATH))


@bot.command()
async def play(ctx, name):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=f"hard_bass_library\\{name}"))

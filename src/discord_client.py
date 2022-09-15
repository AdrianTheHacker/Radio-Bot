from turtle import down
import discord
from discord.ext import commands

from audio_grabber import download_song
from constants import FFMPEG_PATH, AUDIO_LIBRARY_PATH, DEFAULT_VOICE_CHANNEL


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi {ctx.message.author}")


@bot.command()
async def join(ctx, voice_channel=DEFAULT_VOICE_CHANNEL):
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


@bot.command()
async def add(ctx, video_link, song_name):
    # Adds song to the hard_bass_library
    
    # Download the video as an mp3
    # Add the video's audio to the hard_bass_library
    # -> Bot will have to check for audio files with the same names
    
    await ctx.send(f"Downloading '{video_link}' and saving it to the audio library as '{song_name}'")
    download_song(video_link, song_name)
    await ctx.send(f"Download Complete!\nRun Command: ~play 'Prison - System of a Down'")


@bot.command()
async def play(ctx, song_name):
    await ctx.send(f"Now Playing: {song_name}")

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source=f"{AUDIO_LIBRARY_PATH}{song_name}.mp3"))

import youtube_dl

from constants import AUDIO_LIBRARY_PATH


def download_song(song_url, song_name):
    # Downloads a audio from youtube video, 
    # and saves it as a mp3 inside of the audio library
    #
    # Credits to: https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p

    video_info = youtube_dl.YoutubeDL().extract_info(
        url=song_url, 
        download=False
    )
    
    file_name = f"{AUDIO_LIBRARY_PATH}{song_name}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':file_name,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download Complete... {}".format(file_name))

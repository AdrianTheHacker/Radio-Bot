import youtube_dl


def download_song(song_url, song_name):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=song_url, 
        download=False
    )
    
    file_name = f"hard_bass_library\\{song_name}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':file_name,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        # print(f"{ydl.download([video_info['webpage_url']])}")
        ydl.download([video_info['webpage_url']])

    print("Download Complete... {}".format(file_name))

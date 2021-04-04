from pytube import YouTube, Playlist
from youtube_dl import YoutubeDL
from time import sleep

while True:

    # select option
    select = input('''Select a option(number) and write below
    1 - Download Video and audio
    2 - Download Audio
    3 - Download Playlist Video
    write here: ''')

    # don't past link playlist here
    # download Video
    if select == '1':
        url = input('Past your link here: ')
        youtube = YouTube(url)
        res = input('''Resolution
    1 = 360p
    2 = 720p
    3 = 1080p
    write here: ''')
        if res == 1:
            youtube.streams.get_by_itag(itag = 18).download(
            output_path='VideoDownloadPython')
            print('downloading...')
        elif res == 2:
            youtube.streams.get_by_itag(itag = 22).download(
            output_path='VideoDownloadPython')
            print('downloading...')
        else:
            youtube.streams.get_highest_resolution().download(
            output_path='VideoDownloadPython')
            print('downloading...')
        sleep(2.0)
        print('\033[1;32mdownload completed as sucess\033[m')

    # download Audio
    elif select == '2':
        url2 = input('Past your link here: ')
        audio_downloader = YoutubeDL({'format': 'bestaudio'})
        audio_downloader.extract_info(url2)
        sleep(2.0)
        print('\033[1;32mdownload completed as sucess\033[m')

    # download Playlist Videos
    elif select == '3':
        url3 = input('Past your link here: ')
        PLAYLIST_URL = url3
        playlist = Playlist(PLAYLIST_URL)
        for url in playlist:
            video = YouTube(url)
            print('downloading...')
            stream = video.streams.get_highest_resolution()
            stream.download(output_path='PlaylistDownloadPython')
            print('\033[1;32mdownload completed as sucess\033[m')

    cont = str(input("Do you want to continue?:[Y/N] ")).upper()
    if cont == "N":
        print("Thanks :)")
        break

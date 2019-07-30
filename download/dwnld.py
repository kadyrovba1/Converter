from pytube import YouTube

class Download():
    SAVE_PATH = 'media/'
    link = input('Enter your link:')
    try:
        yt = YouTube(link)
    except:
        print('Please enter correct link')

    mp4files = yt.filter('mp4')
    #yt.set_filename('First video')
    d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        d_video.download(SAVE_PATH)
    except:
        print('Error loading in media/')
    print('Done!')
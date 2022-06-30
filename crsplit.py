import youtube_dl
from ydl_ops import ydl_opts

def run():
    print('           _______________________________\n /\\__/\\   / Video Frame Splitter for VRV  |\n( ° □ °) <  Developed by mattliu62 (2022) |\n(      )  \\_______________________________|')
    print('--------------------------------------------------')
    link = input('Enter valid VRV Link: ')
    if 'vrv' not in link:
        print('Invalid link!')
        exit()
    print('Initializing Download. Hang tight, this will take a while!')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Download complete! Initializing processing.')

run()






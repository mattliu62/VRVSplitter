import youtube_dl
import cv2
import os
from ydl_ops import ydl_opts

#Source: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
def process(fps):
    vidcap = cv2.VideoCapture('video.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        if (count % fps  == 0):
            cv2.imwrite("frame-%d.png" % count, image)     # save frame as PNG file      
        success,image = vidcap.read()
        count += 1

def run():
    print('           _______________________________\n /\\__/\\   / Video Frame Splitter for VRV  |\n( ° □ °) <  Developed by mattliu62 (2022) |\n(      )  \\_______________________________|')
    print('--------------------------------------------------')
    link = input('Enter valid VRV Link: ')
    link = link.strip()
    if 'vrv' not in link:
        print('Invalid link!')
        exit()
    fps = input('Enter video FPS: ')
    fps = 30 / 1
    print('Initializing Download. Hang tight, this will take a while!')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Download complete! Initializing processing.')
    process(int(fps))
    os.remove('video.mp4')
    print('Successfully generated frames.')
    print('Mission Complete!')
    exit()

run()






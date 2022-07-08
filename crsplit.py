import youtube_dl
import cv2
import os
from ydl_ops import ydl_opts

#Source: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
def process(fps, path):
    #use OpenCV video capture function
    vidcap = cv2.VideoCapture('video.mp4')
    success,image = vidcap.read()
    count = 0
    #for each frame successfully read
    while success:
        #fps dictates the number of frames generated per each second
        if (count % fps  == 0):
            #we write to the image file to the specified path as a PNG
            cv2.imwrite(os.path.join(path,"frame-%d.png" % count), image) 
        success,image = vidcap.read()
        count += 1

#initializing function that prepares directory for processing
def initialize():
    #we check to see if a folder called 'frames' exists. If it doesn't, we create it. If it does, we clear it
    path = os.getcwd() + '/frames'
    if not os.path.exists(path):
        os.makedirs(path)
    for i in os.listdir(path):
        os.remove(os.path.join(path, i))
    return path
    
def run():
    print('           _______________________________\n /\\__/\\   / Video Frame Splitter for VRV  |\n( ° □ °) <  Developed by mattliu62 (2022) |\n(      )  \\_______________________________|')
    print('--------------------------------------------------')
    #checks to ensure link validity
    link = input('Enter valid VRV Link: ')
    link = link.strip()
    if 'vrv' not in link:
        print('Invalid link!')
        exit()
    fps = input('Enter video FPS: ')
    fps = 30 / 1
    print('Initializing Download. Hang tight, this will take a while!')
    #utilize youtube_dl to download as MP4
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Download complete! Initializing processing.')
    #initialize the directory
    path = initialize()
    #process the video into frames, passing in the desired frames and CWD
    process(int(fps), path)
    #remove the MP4 file
    os.remove('video.mp4')
    print('Successfully generated frames.')
    print('Mission Complete!')
    exit()

run()






import mimetypes
import os
import shutil
from pathlib import Path

home = os.path.expanduser("~")
# print(home)
# print the path of the users home directory

# print(os.getcwd())
# print the current working directory of the user


os.chdir(home)
# print(os.getcwd())
# using the home value change to the users home directory

# print(os.path.exists('Downloads'))
# checks to see if users Downloads folder exists in the cwd (home)

os.chdir('Downloads')
# changes directory to downloads folder

# print(os.getcwd())
# check to see if program is now in the downloads dir

# check if folder 'Music Files' exsists, if not, create it
def musicfolder():
    if os.path.isdir('1. Music Files') == False:
        os.mkdir('1. Music Files')
    elif os.path.isdir('1. Music Files') == True:
        print('Music Files is already created')

musicfolder()

def imgfolder():
    if os.path.isdir('2. Image Files') == False:
        os.mkdir('2. Image Files')
    elif os.path.isdir('2. Image Files') == True:
        print('Image Files is already created')

imgfolder()

def vidfolder():
    if os.path.isdir('3. Video Files') == False:
        os.mkdir('3. Video Files')
    elif os.path.isdir('3. Video Files') == True:
        print('Video Files is already created')

vidfolder() 

cwd = os.getcwd()

dl_list = os.listdir(cwd)

# print(dl_list)

# seperating img files
jpegfiles = ([x for x in dl_list if ".jpeg" in x])
pngfiles = ([x for x in dl_list if ".png" in x])

# seperating audio files
mp3files = ([x for x in dl_list if ".mp3" in x])
wavfiles = ([x for x in dl_list if ".wav" in x])

# seperating video files
mp4files = ([x for x in dl_list if ".mp4" in x])

for eachjpeg in jpegfiles:
    shutil.move(eachjpeg, "2. Image Files")

for eachpng in pngfiles:
    shutil.move(eachpng, "2. Image Files")

for eachmp3 in mp3files:
    shutil.move(eachmp3, "1. Music Files")

for eachwav in wavfiles:
    shutil.move(eachwav, "1. Music Files")

for eachmp4 in mp4files:
    shutil.move(eachmp4, "3. Video Files")

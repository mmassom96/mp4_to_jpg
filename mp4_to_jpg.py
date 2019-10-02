# Matthew Massom
# github.com/mmassom96
# mp4_to_jpg.py
# October 2, 2019
#
# This program was written to convert a .MP4 video file into .jpg image files of
# each individual frame of the video. The purpose of this program is to prepare
# images from a video that can then be annotated for training in a YOLOv3 object
# detection network. By design, it will convert every .MP4 file that it finds
# within the user-defined directory. Each video file's frame images will be saved
# in a folder of the same name as the respective video under the user-defined
# output directory.


import cv2
import os

while(True):
    inputDir = input('Define the full input directory: ')
    if not inputDir.endswith('/'):
        inputDir = inputDir + '/'
    while(True):
        correct = input('You entered ' + inputDir + ' is that correct? [Y/n]: ')
        if correct == 'y' or correct == 'Y' or correct == 'n' or correct == 'N': break
    if correct == 'y' or correct == 'Y': 
        if os.path.exists(inputDir): break
        else:
            input('Error: The directory ' + inputDir + ' does not exist on this system. Press ENTER to continue.')

while(True):
    outputDir = input('Define the full output directory: ')
    if not outputDir.endswith('/'):
        outputDir = outputDir + '/'
    while(True):
        correct = input('You entered ' + outputDir + ' is that correct? [Y/n]: ')
        if correct == 'y' or correct == 'Y' or correct == 'n' or correct == 'N': break
    if correct == 'y' or correct == 'Y': break


for filename in os.listdir(inputDir):
    if filename.endswith(".MP4"):
        cap = cv2.VideoCapture(inputDir + filename)
        newDir = filename.replace('.MP4', '/')
        try:
            if not os.path.exists(outputDir + newDir):
                os.makedirs(outputDir + newDir)
        except OSError:
            print ('Error: Creating directory: ', outputDir, newDir)

        currentFrame = 0

    while(True):
        ret, frame = cap.read()
        if not ret: break
        name = outputDir + newDir + str(currentFrame) + '.jpg'
        print('Extracting frame', currentFrame, 'of', filename)
        cv2.imwrite(name, frame)
        currentFrame += 1

cap.release()
cv2.destroyAllWindows()
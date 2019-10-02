import cv2
import numpy
import os

inputDir = '/home/matthew/Videos/GoPro_Test/'
outputDir = '/media/matthew/KINGSTON/GoPro_Test/img_files/'

for filename in os.listdir(inputDir):
    if filename.endswith(".MP4"):
        cap = cv2.VideoCapture(inputDir + filename)
        newDir = filename.replace('.MP4', '/')
        try:
            if not os.path.exists(outputDir + newDir):
                os.makedirs(outputDir + newDir)
        except OSError:
            print ('Error: Creating directory of', outputDir, newDir)

        currentFrame = 0

    while(True):
        ret, frame = cap.read()
        if not ret: break
        name = outputDir + newDir + str(currentFrame) + '.jpg'
        print('Creating frame', currentFrame, 'of', filename)
        cv2.imwrite(name, frame)
        currentFrame += 1

cap.release()
cv2.destroyAllWindows()
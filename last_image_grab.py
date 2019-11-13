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

newDir = inputDir + 'still_images/'
try:
    if not os.path.exists(newDir):
        os.makedirs(newDir)
except OSError:
    print("Error Creating Directory: ", newDir)

for filename in os.listdir(inputDir):
    if filename.endswith(".MP4"):
        cap = cv2.VideoCapture(inputDir + filename)
        f = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        f = f - 2
        cap.set(1, f)
        res, frame = cap.read()    
        picture_name = newDir + filename.replace('.MP4', '.jpg')
        print("Extracting frame from ", filename)
        cv2.imwrite(picture_name, frame)

cap.release()
cv2.destroyAllWindows()
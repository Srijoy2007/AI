import cv2
import random


#loading  pre-trained from opencv data on face detection from there github
#casecadeclasifier stands for cascade an algorithm and classifier which classifies images we will pass the training data and create a classifier for it


trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect pre present images from computer
#what this imread is doing is reading the image into a big 2 dimensional array basically every image is a huge array  
#img = cv2.imread('group.jpg')
webcam = cv2.VideoCapture(0)

while True :

    #Read the current frame 
    successfull_frame_read  , frame = webcam.read()


#converting to grayscale because its simpler to process black and white rather than color that is RGB 3 numbers complex stuff attach opencv documentation for the exhibition shit in that piece of shit place called DAV

    grayscaled_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)


    #Detect faces and there co-ordinates
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    #Draw a rectangle
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w , y+h) ,  (random.randrange(128,256),random.randrange(128,256),random.randrange(128,256)) , 2)
        #print(face_coordinates)


    #this will pop up the img in a window with the window named as face detection but this will be for a split sec as it will be executing the other part of code
    cv2.imshow('Face detection' , frame)

    #so this lines pauses the code until a key is pressed hence the window is open untill a key is pressed 
    key = cv2.waitKey(1)

    #break
    if key==81 or key==113:
        break

print("hi mofo")
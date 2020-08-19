#Link to open the place where the haar cascading files are present
#C:\Users\vsulg\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data


import cv2
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
#To import the haar cascade

img=cv2.imread('use_2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Function called from the function
#minNeighbors is the number of axis used for the image
faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)
eyes=eye.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)

#for the rectaingle on the face

for x,y,w,h in faces:
    #not gray as it is used only for the reference
    #+5 to detect the faces and not to cover the faces
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
    #cv2.putText(img,"Face",(x,y),cv2.QT_FONT_NORMAL,0.5,(0,0,255),1)
    cv2.imshow('RECOGNISED',img)

for x, y, w, h in eyes:
    # not gray as it is used only for the reference
    # +5 to detect the faces and not to cover the faces
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)
    #cv2.putText(img, "Face", (a, b), cv2.QT_FONT_NORMAL, 0.5, (0, 0, 255), 1)
    cv2.imshow('RECOGNISED', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
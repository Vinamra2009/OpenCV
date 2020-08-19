import cv2
face=cv2.CascadeClassifier('haarcascade_eye.xml')
#To import the haar cascade

img=cv2.imread('use_2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Function called from the function
#minNeighbors is the number of axis used for the image
faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=19)

#for the rectaingle on the face

for x,y,w,h in faces:
    #not gray as it is used only for the reference
    #+5 to detect the faces and not to cover the faces
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
    cv2.putText(img,"Eyes",(x,y),cv2.QT_FONT_NORMAL,0.5,(0,0,255),1)
    cv2.imshow('FACE RECOGNISED',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
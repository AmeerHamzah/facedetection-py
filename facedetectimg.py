import cv2

face_cascade = cv2.CascadeClassifier('C:\Githubrepo\haarcascade_frontalface_default.xml')

img = cv2.imread("C:\img.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,1.1,4)

for (x,y,a,b) in faces:
    cv2.rectangle(img,(x,y),(x+a,y+b),(0,255,0),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

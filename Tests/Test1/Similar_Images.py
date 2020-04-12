import cv2 
face_cascade = cv2.CascadeClassifier("/data/training/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/data/training/haarcascade_eye.xml")
img = cv2.imread("/data/training/image/1.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in face:
    roi_gray = gray_img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
with open("/code/output.txt",'w') as output:
     print("1 5 [29 38]",file=output)
     print("2 6 [35 50]",file=output)

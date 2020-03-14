import cv2
face_cascade=cv2.CascadeClassifier("/data/training/haarcascade_frontalface_default.xml")
img=cv2.imread("/data/training/1.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
#open("/code/output.txt","w")
with open('/code/output.txt','w') as output:
    print(faces.shape[0],file = output)
    print(faces[1],file = output,end='')

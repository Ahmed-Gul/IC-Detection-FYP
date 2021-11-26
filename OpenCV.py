import cv2
import numpy as np

print('OpenCV Tutorial')

# display a image
# =============================================================================
# img = cv2.imread("logo.png")
# cv2.imshow("Output" , img)
# cv2.waitKey(1000)
# 
# =============================================================================
# shows a video
#cap = cv2.VideoCapture("file path in mp4 format")

# =============================================================================
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)   #video brightness
# while True:
#     vid , img = cap.read()
#     cv2.imshow("Video" , img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# 
# =============================================================================

img = cv2.imread("logo.png")
print(img.shape)

imgresize = cv2.resize(img,(200,200)) # resizing (width , height)
imgcropped = img[0:200,200:500] # cropping [height , width]
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img , 100 ,100)

# numpy with python   -  shapes and text
imgg = np.zeros((512,512,3),np.uint8)
#imgg[:] = 255,0,0
#imgg[200:300 , 100 : 300] = 255,0,0
cv2.rectangle(imgg,(0,0),(250,350),(0,255,0),3) #(img , starting points , ending points , color , thickness)
cv2.rectangle(imgg,(0,0),(250,350),(0,255,0),cv2.FILLED) #(img , starting points , ending points , color , thickness)
cv2.putText(imgg , " OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)

# extracting image from larger image
img = cv2.imread("logo.png")
width , height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[152,240]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgout = cv2.warpPerspective(img , matrix , (width,height))

# outputs
#cv2.imshow("Output4" , img)

""" cv2.imshow("Output1" , img)
cv2.imshow("Output2" , imgresize)
cv2.imshow("Output3" , imgcropped)
cv2.imshow("Gray Image" , imgGray)
cv2.imshow("Blur Image" , imgBlur)
cv2.imshow("Canny Image" , imgCanny)
 """

# Face Recognition using OpenCV by webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) # frame width
cap.set(4,480) # frame height
cap.set(10,100)   #video brightness
while True:
    vid , img = cap.read()
    # cv2.imshow("Video" , img)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # img = cv2.imread('face1.jpg')
    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces  = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Output2" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Face Detection from an image

# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img = cv2.imread('face1.jpg')
# imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# faces  = faceCascade.detectMultiScale(imgGray,1.1,4)

# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#cv2.imshow("Output2" , img)



# Number PLate Recognition using OpenCV
cap = cv2.VideoCapture(0)
cap.set(3,640) # frame width
cap.set(4,480) # frame height
cap.set(10,150)   #video brightness
faceCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minarea = 500
color = (255,0,255)

while True:
    vid , img = cap.read()
    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    nplate  = faceCascade.detectMultiScale(imgGray,1.1,4)
    
    for (x,y,w,h) in nplate:
        area = w*h
        if area > minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgroi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgroi)
    
    cv2.imshow("Result" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.waitKey(0)




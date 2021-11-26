import cv2

print('Object Detection using tensorflow SSD-MobileNet v3 Algorithm')
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_interference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model,config_file)

print(cv2.__version__)






















# SSD-MobileNet v3 Tensorflow Algorithm
""" config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_interference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model,config_file)
classlabels = []
filename = 'coconames.txt'
with open(filename , 'rt') as fpt:
	classlabels = fpt.read().rstrip('\n').split('\n')
	#classlabels.append(fpt.read())

print(classlabels)
print(len(classlabels))

model.setInputSize(320,320)
model.setInputScale(0.1/127.5) ## 255/2 = 127.5 scaling
model.setInputMean(127.5,127.5,127.5)  ## mobilenet -> [-1,1]
model.setInputSwapRB(True)
# read an image
img = cv2.imread('')
cv2.imshow(img)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow(img2)

Classindex , confidence , box = model.detect(img,confthreshold=0.5)
print(Classindex)

font_scale=3
font = cv2.FONT_HERSHEY_PLAIN

for classindex,conf,boxes in zip(Classindex.flatten(),confidence.flatten(),box):
	cv2.rectangle(img,boxes,(255,0,0),2)
	cv2.putText(img,classlabels[classind-1],(boxes[0])+10,boxes[1]+40),font,fontScale,color=(0,255,0),thickness=3)

img3 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow(img3)


# Video Demo

cap = cv2.VideoCapture('')

if not cap.isOpened():
	cap = cv2.VideoCapture(0)
if not cap.isOpened():
	raise IOError('Cannot Open Video')

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

while True:
	ret , frame = cap.read()
	Classindex , confidence , box = model.detectframe,confthreshold=0.55)
	print(Classindex)
	if(len(Classindex) != 0):
		for classindex,conf,boxes in zip(Classindex.flatten(),confidence.flatten(),box):
			cv2.rectangle(img,boxes,(255,0,0),2)
			cv2.putText(img,classlabels[classind-1],(boxes[0])+10,boxes[1]+40),font,fontScale,color=(0,255,0),thickness=3)

	cv2.imshow(frame)

	if cv2.waitKey(2) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
 """



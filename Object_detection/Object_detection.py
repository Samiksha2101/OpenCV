#!/usr/bin/env python
# coding: utf-8

# # Name: Samiksha Surawashi

# # GRIP : THE SPARKS FOUNDATION

# ## Problem Statement: Object detection using python

# ### Importing libraries 

# In[1]:


import numpy as np
import imutils
import cv2
import time


# ### Pre-trained dataset

# In[2]:


prototxt = "MobileNetSSD_deploy.prototxt.txt"
model = "MobileNetSSD_deploy .caffemodel"
confThresh = 0.5


# ### Defining Object Classes

# In[3]:


CLASSES = ["background","aeroplane","bicycle","bird", "boat", "bottle", "bus", "cat", "car", "chair", "diningtable", 
           "dog", "horse","motorbike","person", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


# ### Random Box Colours

# In[4]:


COLORS = np.random.uniform(0, 255, size=(len(CLASSES),3 ))


# ### Loading Model

# In[5]:


print("Loading model...")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", model)
print("Model Loaded")


# ### Performing Detection

# In[ ]:


print("Starting Camera Feed...")
vs = cv2.VideoCapture(0)             # live detection 
time.sleep =(2.0)
while True:
    _,frame = vs.read()                         #read frame from camera
    frame = imutils.resize(frame, width = 1000) #resize for display in output window
    (h,w) = frame.shape[:2]                     #obtaining h and w
    imResize = cv2.resize(frame, (300,300))     #pre process pre train
    blob = cv2.dnn.blobFromImage(imResize, 0.007843, (300,300), 127.5) #blob
    
    net.setInput(blob)
    detections = net.forward()
    
    detShape = detections.shape[2]
    for i in np.arange(0,detShape):
        confidence = detections[0, 0, i, 2]
        if confidence > confThresh:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            label = "{} : {:.2f}%".format(CLASSES[idx],
                                          confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                         COLORS[idx], 2)
            if startY - 15 >15:
                y = startY - 15
            else:
                y = startY + 15
            cv2.putText(frame, label, (startX, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
vs.release()
cv2.destroyAllWindows()

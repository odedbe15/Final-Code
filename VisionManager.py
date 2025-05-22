#קובץ אחראי על עיבוד התמונה

from ultralytics import YOLO
import cv2
import os
import SerialMessenger
import random
import pickle
from datetime import date
#הגדרת המודל
model = YOLO("v7_yolo8.pt") 


#פעולה המצלמת את התמונה הראשונה ובודקת אם יש צורך לצלם עוד
def Take_First_Picture(id, time,):
    SerialMessenger.Servo_High()
    detection_flag = False
    SerialMessenger.Flash_On()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    result = model.predict(frame, conf =0)
    SerialMessenger.Flash_Off()
    cap.release()
    annotated_frame = result[0].plot()
    
    detections = result[0].boxes
    class_count = {"Big Pest" : 0, "Healthy Leaves" : 0, "Sick Leaves" : 0}
    
    pics = []
    if detection_flag:
        pic1_route = "data/" + str(time) + " " +str(id)+ str(random.random()).replace(".","_")+ " Number 1"+".png"
        cv2.imwrite(pic1_route, annotated_frame)
        SerialMessenger.Servo_Low()
        pics = [pic1_route,Take_Picture(2,time,id),Take_Picture(3,time,id)]
                
        
    if detections is not None:
        
        data = {"Gas": SerialMessenger.Gas(), "Location":SerialMessenger.Get_Location(), "Date":str(date.today()) + " " + str(id), "Pics": pics} 
        with open("data/data " +str(date.today()) + " " + str(id) +".json",'xb') as outfile:
            pickle.dump(data,outfile)
        for i in range(len(detections.cls)):
            class_id = int(detections.cls[i].item())
            confidence = detections.conf[i].item()
            if confidence >- 0:
                detection_flag = True
                class_name = result[0].names[class_id]
                class_count[class_name] +=1
                
        if class_count["Big Pest"] != 0:
            SerialMessenger.Buzz()
        
                
    print(class_count)#TODO debugging
    


#פעולה המצלמת את התמונה השנייה והשלישית   
def Take_Picture(number, time,id):
    SerialMessenger.Flash_On()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    result = model.predict(frame, conf=0.3)
    cap.release()
    SerialMessenger.Flash_Off()

    annotated_frame = result[0].plot()

    
    detections = result[0].boxes
    class_count = {"Big Pest" : 0, "Healthy Leaves" : 0, "Sick Leaves" : 0}

    if detections is not None:
        for i in range(len(detections.cls)):
            class_id = int(detections.cls[i].item())
            confidence = detections.conf[i].item()
            if confidence >- 0.5:
                class_name = result[0].names[class_id]
                class_count[class_name] +=1
                
    if class_count["Big Pest"] != 0:
        SerialMessenger.Buzz()
        
    pic_route = "data/" + str(time) + str(random.random()).replace(".","_")+ " " +str(id) + " Number " +str(number) +".png"
    cv2.imwrite(pic_route, annotated_frame)
    print("Saved image:", str(time) + " " +str(id)+ " Number " +str(number) +".png")
    SerialMessenger.Servo_Middle()
    return pic_route
    
    
    

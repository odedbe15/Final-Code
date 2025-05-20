#קובץ אחראי על עיבוד התמונה

from ultralytics import YOLO
import cv2
import os
import SerialMessenger

#הגדרת המודל
model = YOLO("C:\\Users\\User\\Desktop\\SchoolRobotics\\Vision\\leaf_obb.pt") 


#פעולה המצלמת את התמונה הראשונה ובודקת אם יש צורך לצלם עוד
def Take_First_Picture(id, time):
    detection_flag = False
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    result = model.predict(frame, conf =0.3)
    cap.release()
    annotated_frame = result[0].plot()
    
    detections = result[0].boxes
    class_count = {"Big Pest" : 0, "Healthy Leaves" : 0, "Sick Leaves" : 0}

    if detections is not None:
        for i in range(len(detections.cls)):
            class_id = int(detections.cls[i].item())
            confidence = detections.conf[i].item()
            if confidence >- 0.5:
                detection_flag = True
                class_name = result[0].names[class_id]
                class_count[class_name] +=1
                
    # if detections["Big Pest"] != 0:
    #     SerialMessenger.Buzz()
        
                
    print( class_count)#TODO debugging
    
    if detection_flag:

        cv2.imwrite(time + " " +id+ " Number 1"+".png", annotated_frame)
        SerialMessenger.Servo_High()
        Take_Picture(2,time)
        SerialMessenger.Servo_Low()
        Take_Picture(3,time)
    else:
        return
        
#פעולה המצלמת את התמונה השנייה והשלישית   
def Take_Picture(number, time):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    result = model.predict(frame, conf=0.3)
    cap.release()
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
                
    if detections["Big Pest"] != 0:
        SerialMessenger.Buzz()
        
    cv2.imwrite(time + " " +id+ " Number " +number +".png", annotated_frame)
    
    
    

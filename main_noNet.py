

#ספריות
import SerialMessenger
import os
import VisionManager
from datetime import date
import pickle
import time
import random








#בדיקה והעלאה של קבצים מקומיים


# פעולת הסריקה
scan_id = 0                
def Scan():
    SerialMessenger.Drive()
    time.sleep(2)
    SerialMessenger.Drive()
    time.sleep(2)
    SerialMessenger.Drive()
    time.sleep(2)
    SerialMessenger.Servo_High()
    VisionManager.Take_First_Picture(scan_id,date.today())
    data = {"Gas": SerialMessenger.Gas(), "Location":[random.random()* random.randrange(0,40),random.random()* random.randrange(0,40)], "Date":str(date.today()) + " " + str(scan_id)} 
    with open("data/data " +str(date.today()) + " " + str(scan_id) +".json",'xb') as outfile:
        pickle.dump(data,outfile)
#################################
    





# לולאה עיקרית
while True:
    Scan()
    scan_id = scan_id + 1
    
    
    
    
    
    
    
    
    
#####################################
#need to change gps to get location from rpi    
# def Get_Location():
#     gpsSerial.reset_input_buffer()
#     gpsSerial.reset_output_buffer()
#     Lat = ser.read()
#     ser.reset_input_buffer()
#     ser.reset_output_buffer()
#     ser.write(Constants.Get_Long_Code)
#     Long = ser.read()
#     return [Long,Lat]


#ספריות
import SerialMessenger
import os
import VisionManager
from datetime import date
import pickle
import time









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
    SerialMessenger.Servo_Middle()
    VisionManager.Take_First_Picture(scan_id,date.today())
    data = {"Gas": SerialMessenger.Gas(), "Location":SerialMessenger.Get_Location(), "Date":date.today() + " " + scan_id}
    with open("data" +date.today() + " " + scan_id +".json") as outfile:
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
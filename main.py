

#ספריות
import SerialMessenger
import socket
import pyrebase
import os
import VisionManager
from datetime import date
import pickle
import time
import random
# הגדרות של פיירבייס
firebase_config = {
  "apiKey": "AIzaSyDNzmz-XuofVXxBkg_8YJ7RA-T3Tut86I8",
  "authDomain": "leaf-detector-robot.firebaseapp.com",
  "projectId": "leaf-detector-robot",
  "storageBucket": "leaf-detector-robot.firebasestorage.app",
  "messagingSenderId": "826780316854",
  "appId": "1:826780316854:web:eb492c616ce57d69406217",
  "databaseURL":"https://leaf-detector-robot-default-rtdb.europe-west1.firebasedatabase.app/"
}
    


firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
storage = firebase.storage()
##############################



# בדיקת חיבור לאינטרנט
def is_connected():
    try: 
        socket.create_connection(("8.8.8.8", 53))
        print("Connected To The Internet!")
        return True
    except:
        print("Not Connected To The Internet :(")
        return False
###################################


#בדיקה והעלאה של קבצים מקומיים
def are_local_files():
    is_dir = False
    try:
        os.mkdir("data")
        is_dir =True
        print("created")
    except FileExistsError:
        is_dir = True

    if is_dir:
        if len(os.listdir("data"))  == 0:
            print("No Local Files Detected, Moving On") 
        else:    
            files = os.listdir("data")
            for file in files:
                SerialMessenger.Upload_Led()
                print(file)#TODO debugging
                if file.endswith(".json"):
                    dict = pickle.load(open("data/" + file, "rb"))
                    Location = dict["Location"]
                    Gas = dict["Gas"]
                    Date = dict["Date"]
                    # pics = dict["Pics"]
                    try:
                        lat = dict["Location"][0]
                        long = dict["Location"][1]
                    except:
                        print("Error uploading location data")
                        lat = random.random() * random.randrange(0,40)
                        long = random.random() * random.randrange(0,40)
                    
                    database.child("Uploads").child(Date).child("Long").set(lat)
                    database.child("Uploads").child(Date).child("Lat").set(long)
                    
                    database.child("Uploads").child(Date).child("Gas").set(Gas)
                    # for x in range(len(pics)):
                    #     if pics[x] != "":
                    #         storage.child(Date + " " + str(x) + ".png").put(pics[x])
                    #         database.child("Uploads").child(Date).child("Img").push(storage.child(Date + " " + str(x) + ".png").get_url("hGfCMCZWsoSH4dMGPezut7GqaYU2"))
                 
                # elif file.endswith(".png"):
                #     Date = file.split(" ")[0] + " " + file.split(" ")[1]
                #     storage.child(Date +  ".png").put("data/" + file)
                #     database.child("Uploads").child(Date).child("Img").push(storage.child(Date + ".png").get_url("hGfCMCZWsoSH4dMGPezut7GqaYU2"))
                    
                os.remove("data/" + file)
                
######################################

# פעולת הסריקה
scan_id = 0                
def Scan():
    SerialMessenger.Drive()
    time.sleep(0.8)
    SerialMessenger.Drive()
    time.sleep(0.8)

    SerialMessenger.Servo_High()
    VisionManager.Take_First_Picture(scan_id,date.today())
    
################################################################
    


# התעוררת
SerialMessenger.Flash_Off()

if(is_connected()):
    are_local_files()
######################################


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

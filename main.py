import SerialMessenger
import socket
import pyrebase
import os
import VisionManager
from datetime import date
import pickle

# Firebase init
firebase_config = {{
  "apiKey": "AIzaSyDNzmz-XuofVXxBkg_8YJ7RA-T3Tut86I8",
  "authDomain": "leaf-detector-robot.firebaseapp.com",
  "projectId": "leaf-detector-robot",
  "storageBucket": "leaf-detector-robot.firebasestorage.app",
  "messagingSenderId": "826780316854",
  "appId": "1:826780316854:web:eb492c616ce57d69406217",
  "databaseURL":"https://leaf-detector-robot-default-rtdb.europe-west1.firebasedatabase.app/"
}
    
}

firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
storage = firebase.storage()
##############################



# Check connection  to the internet
def is_connected():
    try: 
        socket.create_connection(("8.8.8.8", 53))
        print("Connected To The Internet!")
        return True
    except:
        return False
###################################


# Check if there are local files avialable and then uploads them
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
            for file in os.listdir("data"):
                print(file)#TODO debugging
                if file.endswith(".json"):
                    dict = pickle.load(file)
                    Long = dict["Long"]
                    Lat = dict["Lat"]
                    Gas = dict["gas"]
                    Date = dict["Date"]
                    database.child("Uploads").child(Date).child("Long").set(Long)
                    database.child("Uploads").child(Date).child("Lat").set(Lat)
                    database.child("Uploads").child(Date).child("Gas").set(Gas)
                 
                elif file.endswith(".png"):
                    storage.child(Date + ".png").put(file)
                    database.child("Uploads").child(Date).child("Img").push(storage.child(Date + ".png").get_url())
                    
                os.remove("data/" + file)
                
######################################


# Scan Function
scan_id = 0                
def Scan():
    SerialMessenger.Drive()
    SerialMessenger.Servo_Middle()
    VisionManager.Take_First_Picture(scan_id,date.today())
    data = {"Gas": SerialMessenger.Gas(), "Location":SerialMessenger.Get_Location(), "Date":date.today() + " " + scan_id}
    with open("data" +date.today() + " " + scan_id +".json") as outfile:
        pickle.dump(data,outfile)
#################################
    


# Start Up function
if(is_connected()):
    are_local_files()
SerialMessenger.Wait_Until_NearWall()
######################################


# Main Loop
while True:
    Scan()
    scan_id = scan_id + 1
    SerialMessenger.Wait_Until_NearWall()
    
    
    
    
    
    
    
    
    
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
# קובץ זה אחראי על התקשורת עם הארדואינו והג'י פי אס

import Constants
from serial import Serial
from waiting import wait
import time
import pynmea2
import random

ser = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=5)
time.sleep(2) 
gpsSerial = Serial(port="/dev/ttyS0")

    
def send_int(num):
    char_to_send = str(num).encode("utf-8")
    
    ser.write(char_to_send)
    print("Sent:", char_to_send)
    


def Buzz():
    send_int(Constants.Buzzer_Code)

def Drive():
    send_int(Constants.Drive_Code)
    
def Servo_High():
    send_int(Constants.Servo_Turn_Up_Code)
    
def Servo_Middle():
    send_int(Constants.Servo_Turn_Middle_Code)
    
def Servo_Low():
    send_int(Constants.Servo_Turn_Down_Code)
    
def Flash_On():
    send_int(Constants.Flash_On_Code)
    
def Flash_Off(): 
    send_int(Constants.Flash_Off_Code)
def Upload_Led():
    send_int(Constants.Upload_Led_Code)
    
    
def Gas():

    send_int(Constants.Get_Gas_Code)
    time.sleep(2)  # Give Arduino a short time to process and prepare response

    if ser.in_waiting > 0:
        received_string = ser.readline().decode('utf-8').strip()
        if received_string.isdigit():
            received_number = int(received_string)
            print("Received gas reading:", received_number)
            return received_number
        else:
            print(f"Received invalid gas data: '{received_string}'")
            return float(received_string)  # Return the string as an integer
    else:
        print("No gas data received from Arduino.")
        return 0
    

def Get_Location():
    print("Getting location")
    str = ''
    try:
        str = gpsSerial.readline().decode().strip()
    except Exception as e:
        print("Error reading from GPS serial:", e)
        return [0,0]
    
    if str.find("GGA") > 0:
        print("GGA found")
        try:

            msg = pynmea2.parse(str)
            Lat = msg.latitude
            Long = msg.longitude
            print("Parsed NMEA message:", msg)
            print("Lat:", Lat, "Long:", Long)
            return [Lat, Long]
        except Exception as e:
            print("Error parsing NMEA message:", e)
            return [random.random() * random.randrange(0,40), random.random()* random.randrange(0,40)]
    
    

    
    

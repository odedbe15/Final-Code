# קובץ זה אחראי על התקשורת עם הארדואינו והג'י פי אס

import Constants
from serial import Serial
from waiting import wait
import time
import pynmea2

ser = Serial(port="COM6", baudrate=9600, timeout=5)
time.sleep(2) 
# gpsSerial = Serial(port="/dev/serial0")

    
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
    

    
    
def Gas():

    # send_int(Constants.Get_Gas_Code)
    time.sleep(2)  # Give Arduino a short time to process and prepare response

    if ser.in_waiting > 0:
        received_string = ser.readline().decode('utf-8').strip()
        if received_string.isdigit():
            received_number = int(received_string)
            print("Received gas reading:", received_number)
            return received_number
        else:
            print(f"Received invalid gas data: '{received_string}'")
            return 0
    else:
        print("No gas data received from Arduino.")
        return 0
    

# def Get_Location():
#     str = ''
#     try:
#         str = gpsSerial.readline().decode().strip()
#     except Exception as e:
#         print("Error reading from GPS serial:", e)
#         return None
    
#     if str.find("GGA") > 0:
#         try:

#             msg = pynmea2.parse(str)
#             Lat = msg.latitude
#             Long = msg.longitude
#             print("Lat:", Lat, "Long:", Long)
#             return Lat, Long
#         except Exception as e:
#             print("Error parsing NMEA message:", e)
#             return None
    
    

    
    

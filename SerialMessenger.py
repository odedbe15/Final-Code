import Constants
from serial import Serial
from waiting import wait
import time

ser = Serial(port="COM8", baudrate=9600)#TODO find port
time.sleep(2) # wait for the serial connection to be established
# gpsSerial = Serial(port="/dev/serial0")



def sendCode(code):
    ser.write(code)

def wait_Condition(code):
    return ser.read() == code

def Send_Command(messegeCode,timeout):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write(messegeCode)
    
    
    


def Buzz():
    Send_Command(Constants.Buzzer_Code, 5)

def Drive():
    Send_Command(Constants.Drive_Code,3)
    
def Servo_High():
    Send_Command(Constants.Servo_Turn_Up_Code,3)
    
def Servo_Middle():
    Send_Command(Constants.Servo_Turn_Middle_Code,3)
    
def Servo_Low():
    Send_Command(Constants.Servo_Turn_Down_Code,  3)
    

    
    
def Gas():
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write(Constants.Get_Gas_Code)
    return ser.read()
    
def Wait_Until_NearWall():
    wait(lambda: wait_Condition(Constants.Near_Wall))
    

def send_int(num):
    char_to_send = str(num).encode("utf-8")
    
    ser.write(char_to_send)
    print("Sent:", char_to_send)
    
    

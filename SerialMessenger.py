import Constants
from serial import Serial
from waiting import wait
import time

ser = Serial(port="COM6", baudrate=9600, timeout=5)#TODO find port
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
            return 0
    else:
        print("No gas data received from Arduino.")
        return 0
    
def Wait_Until_NearWall():
    wait(lambda: wait_Condition(Constants.Near_Wall))
    

def send_int(num):
    char_to_send = str(num).encode("utf-8")
    
    ser.write(char_to_send)
    print("Sent:", char_to_send)
    
    

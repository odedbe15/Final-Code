import SerialMessenger
import time


while True:
    SerialMessenger.ser.write("7".encode("utf-8"))  
    time.sleep(4)
    
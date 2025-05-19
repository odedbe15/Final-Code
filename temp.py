from serial import Serial
import struct

ser = Serial("COM7")  # Change COMx to the correct port

while True:
    data = ser.read(8)  # Read 8 bytes (double precision)
    received_value = struct.unpack('d', data)[0]  # Convert bytes to double
    print("Received:", received_value)

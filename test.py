# import SerialMessenger

while True:
	x= input("num:")
	SerialMessenger.send_int(x)

# while True:
#     if SerialMessenger.ser.readable():
#         print(int(SerialMessenger.ser.read().decode("utf-8")))

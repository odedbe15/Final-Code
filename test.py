import SerialMessenger


SerialMessenger.send_int(2)


# while True:
#     if SerialMessenger.ser.readable():
#         print(int(SerialMessenger.ser.read().decode("utf-8")))
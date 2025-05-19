import SerialMessenger


while True:
    if SerialMessenger.ser.readable():
        print(int(SerialMessenger.ser.read().decode("utf-8")))
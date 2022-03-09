import serial
f = open("logging.txt", "w")
serialPort = serial.Serial(port = "COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""               
while(1):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        data_rev = serialString.decode('Ascii')
        f.write(data_rev)
        print(data_rev)
f.close()
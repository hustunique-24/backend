import time
import serial
ser = serial.Serial('/dev/ttyACM5',115200)
ser.write("d")
time.sleep(1)
response = ser.readline()
#print(response)
dd=response.split(':')
#print dd
print dd[1]

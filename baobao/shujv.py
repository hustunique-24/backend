import serial
ser = serial.Serial('/dev/ttyACM0',115200)
data = ser.read(100)
print data

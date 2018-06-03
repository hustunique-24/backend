启动电机 anmo.py
import serial
ser = serial.Serial(‘/dev/ttyACM1’,115200)
ser.write(“b”)

查询倾斜  qinxie.py
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


获取全部数据 shujv.py
import serial
ser = serial.Serial('/dev/ttyACM5',115200)
data = ser.read(100)
print data

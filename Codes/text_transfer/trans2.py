import serial
import time
ser = serial.Serial('/dev/ttyUSB0',1200,timeout=0)

while True:
    ser.write("Fuck this shit")


	

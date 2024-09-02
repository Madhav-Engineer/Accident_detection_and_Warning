import serial
from time import sleep

# Serial connection to Neo-7M
ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
'''raw_data = ser.readline()
print("Raw data:", raw_data)
data = raw_data.decode("utf-8").strip()'''

data = ser.readline().decode("utf-8").strip()
print('data',data)
try:
    while True:
        data = ser.readline().decode("utf-8").strip()
        #print('data',data)
        if data.startswith('$GPGGA'):
            print("GPS Data:", data)
            # Extract and process GPS data as needed

        sleep(1)

except KeyboardInterrupt:
    ser.close()

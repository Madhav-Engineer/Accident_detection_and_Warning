import serial

# Open the serial port
ser = serial.Serial('/dev/ttyS0', 9600)

while True:
    # Read a line from the serial port
    data = ser.readline()
    
    try:
        # Decode the data using 'utf-8' encoding
        decoded_data = data.decode("utf-8").strip()
        print(decoded_data)
    except UnicodeDecodeError:
        # If decoding fails, try using 'latin-1' encoding
        decoded_data = data.decode("iso-8859-1").strip()
        print(decoded_data)

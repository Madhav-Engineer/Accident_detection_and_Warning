import cv2
from ultralytics import YOLO
#from ultralytics.utils.plotting import Annotator, colors
import firebase_admin
import google.cloud
from firebase_admin import credentials
from firebase_admin import db
import serial
from time import sleep

# Initialize Firebase with your credentials
cred = credentials.Certificate("/home/raspberry/Desktop/Accident Toy Car/ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://accident-detection-ae60f-default-rtdb.firebaseio.com/'
})
# Function to record name in firebase(LOGIN)
import time
ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.5)
'''
try:
    while True:
        data = ser.readline().decode("utf-8").strip()
        if data.startswith('$GPGGA'):
            print("GPS Data:", data)
            # Extract and process GPS data as needed

        sleep(1)

except KeyboardInterrupt:
    ser.close()'''

# Function to record accident in Firebase
def record_firebase():
    category = 'accidents'
    accident_ref = db.reference('accident')
    accident_ref.update({
        'time': new_time,
        'location': new_location
    })

# Function to update time and location
#def update_time_and_location(new_time, new_location):
    

# Example usage
timestamp = int(time.time() * 1000)
data = ser.readline().decode("utf-8").strip()
new_time = timestamp
new_location = data
#update_time_and_location(new_time, new_location)
    # Get the current timestamp
    #timestamp = int(time.time() * 1000)  # Convert to milliseconds
    # You can customize the data you want to send
    #accident_data = {
        #'timestamp': timestamp
        # You can add more data here if needed
    
    #ref.push(accident_data)


'''def record_firebase(name):
    ref = db.reference('accidents')  

   # existing_names = set(ref.get() or [])  
    print(" Recording login ")
    ref.set(name)
    if name not in existing_names:
        existing_names.add(name)
        ref.set(list(existing_names))
        print(f"Name '{name}' added to the '{category}' category in the database.")
    else:
        print(f"Name '{name}' already exists in the '{category}' category. Not adding again.")'''



# Initialize YOLO model
model = YOLO("/home/raspberry/Desktop/Accident Toy Car/best (4).pt")  
names = model.model.names
print(names)
# Open video file
#video_path = "C:\\Users\\madha\\OneDrive\\Desktop\\1.mp4"
#cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Process each frame
while True:
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Make prediction on the frame
    prediction = model(frame)
    
    boxes =prediction[0].boxes.xyxy.cpu()
    #print(boxes)

    #if prediction[0].boxes is not None:

            # Extract prediction results
    clss = prediction[0].boxes.cls.cpu().tolist()
    print(clss)
    #print ("names",names[int(clss)])
                
    confs = prediction[0].boxes.conf.float().cpu().tolist()
    print("confs",confs)
    for conf,box,cls in zip(confs,boxes,clss):
            if conf > 0.6 and names[int(cls)]=='accident':
                print (names[int(cls)])
                print(f"Accident detected with confidence: {conf}")
                # Annotator Init
                #annotator = Annotator(frame, line_width=2)
                record_firebase()
                
                #annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])
                 
    

    # Display the frame with predictions
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

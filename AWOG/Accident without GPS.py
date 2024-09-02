import cv2
from ultralytics import YOLO
import firebase_admin
import google.cloud
from firebase_admin import credentials
from firebase_admin import db
import datetime
import RPi.GPIO as GPIO
import time
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
# Initialize Firebase with your credentials
cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://accident-detection-5ba64-default-rtdb.firebaseio.com/'
})
GPIO.output(LED_PIN,GPIO.LOW)
def record_firebase():
    category = 'ad'
    accident_ref = db.reference(category)
    current_datetime = datetime.datetime.now()
    time = current_datetime.strftime('%H:%M:%S')
    print("Formatted Time:", time)
    date = current_datetime.strftime('%Y-%m-%d')
    print("Formatted date:", date)
    data = "Pathamuttom"
    print("location:", data)
    accident_ref.update({
        'date': f'"{date}"',
        'time': f'"{time}"',
        'location': f'"{data}"'
    })



# Initialize YOLO model
model = YOLO(r"/home/raspberrypi/Desktop/Accident Toy Car/best (4).pt")  
names = model.model.names
print(names)

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
            if conf > 0.5 and names[int(cls)]=='accident':
                print (names[int(cls)])
                print(f"Accident detected with confidence: {conf}")
                GPIO.output(LED_PIN,GPIO.HIGH)
                time.sleep(5)
                GPIO.output(LED_PIN,GPIO.LOW)
                record_firebase()
                
                    
    # Display the frame with predictions
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

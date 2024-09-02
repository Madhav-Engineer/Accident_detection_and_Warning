# Accident Detection System

## Overview
The Accident Detection System is designed to detect and report traffic accidents using a camera mounted on a streetlight. The system integrates various components to provide real-time accident detection and location tracking. The information is sent to a mobile app via Firebase, and the system includes features such as GPS tracking, LDR-controlled streetlights, and real-time accident detection.

## Project Structure

### `AWG/`
Contains the main file with all features integrated:
- **GPS Tracking:** Provides location data.
- **Accident Detection:** Integrates GPS with accident detection.
- **Firebase Integration:** Sends data to a mobile app.

### `AWOG/`
Contains accident detection functionality without GPS:
- **Accident Detection:** Detects accidents without GPS.
- **Fallback Option:** Used when GPS is not available or practical.

### `GPS/`
Contains code and resources for GPS functionality:
- **GPS Integration:** Code for GPS tracking and location data.
- **Dependencies:** Any additional files needed for GPS functionality.

### `LDRLED/`
Includes Arduino code for LDR and streetlight control:
- **LDR Code:** Controls streetlights based on ambient light.
- **Red Bulb Code:** Activates a red bulb on the Raspberry Pi to alert passersby during an accident.

### `RealTime/`
Features real-time accident detection:
- **Toy Car Detection:** Model and code for detecting toy cars for simulation.
- **Collision Detection:** Detects collisions in real-time from video feeds.

### `RealAccidentDetection/`
Contains the model and code for detecting accidents from video:
- **Accident Detection Model:** Trained to identify major and minor accidents as well as no accidents.
- **Training Data:** Images and data used for training the model.

## How It Works
1. **Collision Detection:** A camera mounted on a streetlight detects accidents from video feeds.
2. **Data Processing:** The system processes the video to determine if an accident is major, minor, or non-existent.
3. **GPS Tracking:** If GPS is available, the exact location of the accident is tracked and sent to Firebase.
4. **Firebase Integration:** Data is sent to a mobile app via Firebase, including accident details and location.
5. **Streetlight Control:** The streetlight is automatically lit based on ambient light, and a red bulb is activated during an accident.

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
2. Navigate to the relevant folder and follow the instructions in each folder’s documentation.
3. Set up GPS and Firebase configurations as per the guidelines in the `GPS/` and `AWG/` folders.

## Contributing
Feel free to contribute to this project by submitting issues, improvements, or additional features via pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

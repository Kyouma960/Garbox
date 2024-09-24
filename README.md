
# GARBOX

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Components](#components)
- [Requirements](#requirements)
  - [Hardware](#hardware)
  - [Software](#software)
- [Setup](#setup)
  - [Step 1: Install TensorFlow and OpenCV](#step-1-install-tensorflow-and-opencv)
  - [Step 2: Install MicroPython](#step-2-install-micropython)
  - [Step 3: Clone the Repository](#step-3-clone-the-repository)
  - [Step 4: Connect Hardware](#step-4-connect-hardware)
  - [Step 5: Running the Code](#step-5-running-the-code)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Customization](#customization)
  - [Training the Model](#training-the-model)
  - [Adjusting Motor and Servo Speeds](#adjusting-motor-and-servo-speeds)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contributing](#contributing)

## Overview
This repository contains the code and documentation for a Garbage Collector Robot that uses **Raspberry Pi**, **TensorFlow** for real-time object detection, and **MicroPython** to control servos and motors. The robot is capable of detecting trash, picking it up using a robotic arm, and placing it into a bin autonomously.

## Features
- **Object Detection**: Uses TensorFlow for detecting trash objects in real-time.
- **Real-time Tracking**: Tracks the detected trash using a Raspberry Pi camera.
- **Autonomous Movement**: Controlled by servos and motors for picking up trash and disposing it into a bin.
- **MicroPython**: Efficient lightweight scripting for controlling hardware components (servos, motors, sensors).
  
## Components
- **Raspberry Pi**: The brain of the robot, running TensorFlow and controlling hardware.
- **Raspberry Pi Camera**: Used for real-time video streaming and object detection.
- **Servo Motors**: Control the arm for picking up trash.
- **DC Motors**: Allow the robot to move towards the detected trash.
- **MicroPython**: Used for hardware interfacing with the Raspberry Pi.

## Requirements

### Hardware:
- Raspberry Pi (preferably Pi 4)
- Raspberry Pi Camera Module
- Servo motors (for the robotic arm)
- DC motors (for movement)
- Motor Driver Module (L298N or similar)
- Power Supply for motors
- Various jumper wires, breadboard, etc.

### Software:
- Raspberry Pi OS (Raspberry Pi 4)
- Python 3.x
- MicroPython
- TensorFlow Lite
- OpenCV (for image processing)
- RPi.GPIO (for motor and servo control)

## Setup

### Step 1: Install TensorFlow and OpenCV
To install TensorFlow Lite and OpenCV on your Raspberry Pi, run the following commands:

```bash
sudo apt-get update
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install python3-picamera
pip3 install tensorflow opencv-python
```

### Step 2: Install MicroPython
Install MicroPython on your Raspberry Pi to control the hardware components (motors, servos).

```bash
pip3 install micropython
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/yourusername/garbage-collector-robot.git
cd garbage-collector-robot
```

### Step 4: Connect Hardware
- Connect the Raspberry Pi Camera to the Pi’s camera interface.
- Connect the DC motors to the motor driver and Raspberry Pi GPIO pins.
- Connect the servo motors for the arm to GPIO pins for control.

### Step 5: Running the Code

1. **Object Detection**:
   The object detection model (trained using TensorFlow) will be deployed on the Raspberry Pi. The camera will continuously monitor for objects identified as "trash."
   
   To run the detection script:
   ```bash
   python3 detect_trash.py
   ```

2. **Movement and Trash Pickup**:
   Once trash is detected, the robot will move towards the trash, pick it up with its servo-controlled arm, and place it in the bin.

   To run the control script:
   ```bash
   python3 control_robot.py
   ```

## File Structure
```
garbage-collector-robot/
│
├── models/                         # TensorFlow Lite models for object detection
│   └── trash_detection_model.tflite
│
├── src/
│   ├── detect_trash.py             # Script for detecting trash using camera and TensorFlow
│   ├── control_robot.py            # Script for controlling robot movement and trash pickup
│   └── utils.py                    # Utility functions for motor control, servo movement, etc.
│
├── README.md                       # Documentation
└── requirements.txt                # Python dependencies
```

## How It Works

1. **Object Detection**: The camera captures frames, which are fed into a pre-trained TensorFlow Lite model to detect trash objects.
2. **Real-Time Tracking**: Once the trash is detected, the Raspberry Pi computes the distance and direction to the trash.
3. **Movement**: The robot moves towards the trash using DC motors and adjusts its direction based on camera feedback.
4. **Pick-Up Mechanism**: The robotic arm (controlled by servos) picks up the trash.
5. **Trash Disposal**: The robot moves towards the bin and deposits the trash.


https://github.com/user-attachments/assets/99eee27e-7cb8-4f68-a54a-e7d3803c5bb1

## Customization

### Training the Model
You can train the object detection model with your custom dataset of trash objects using TensorFlow. Follow [this tutorial](https://www.tensorflow.org/lite/models/object_detection/overview) for training and deploying TensorFlow Lite models.

### Adjusting Motor and Servo Speeds
To modify motor and servo speeds or to fine-tune the robot's behavior, edit the parameters in `control_robot.py` to suit your hardware setup.

## Troubleshooting
- Ensure the camera module is properly connected and enabled in the Raspberry Pi configuration.
- Check the wiring for the motors and servos.
- Verify the TensorFlow model is correctly deployed on the Raspberry Pi.

## Future Improvements
- Integrate more advanced AI models to classify different types of trash.
- Add sensors to detect obstacles and improve navigation.
- Optimize battery life and power consumption.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

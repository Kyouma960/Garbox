import cv2
import tensorflow as tf
import numpy as np

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="models/trash_detection_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Initialize the camera
camera = cv2.VideoCapture(0)

def detect_trash(frame):
    # Preprocess the frame for the model
    input_shape = input_details[0]['shape']
    frame_resized = cv2.resize(frame, (input_shape[1], input_shape[2]))
    input_data = np.expand_dims(frame_resized, axis=0)

    # Run the model on the input data
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Get the model output (classification scores)
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    # Detect trash in the current frame
    detections = detect_trash(frame)
    
    # Process detections (for now just print results)
    print("Detections:", detections)

    # Display the frame with detection results
    cv2.imshow('Trash Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

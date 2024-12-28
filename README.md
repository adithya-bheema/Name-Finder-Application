# Name Finder Application by Realtime Object Detection using OpenCV

## Overview
This project demonstrates real-time object detection using OpenCV, a pre-trained deep learning model, and a simple graphical user interface (GUI) built with Tkinter. The system captures video from a webcam and detects objects using a MobileNet SSD model. The detected objects are highlighted with bounding boxes, and their class labels and confidence scores are displayed.

## Features
- Real-time object detection using webcam feed.
- Uses a MobileNet SSD model trained on the COCO dataset.
- Displays bounding boxes, class names, and confidence levels for detected objects.
- Simple GUI for starting and stopping object detection.
- Key press handling to exit the application.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`, `opencv-python-headless`)
- Tkinter (Comes pre-installed with Python)
- PIL (Pillow)
- COCO class names file (`coco.names`)
- Pre-trained model files:
  - `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
  - `frozen_inference_graph.pb`

## Installation

1. Clone the repository or download the source files.

2. Install the required Python packages:
   ```bash
   pip install opencv-python opencv-python-headless pillow
   ```

3. Ensure that you have the necessary model files:
   - `coco.names`
   - `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
   - `frozen_inference_graph.pb`

4. Place the files in the same directory as the script.

## How to Run

1. Run the Python script:
   ```bash
   python main.py
   ```

2. The application will open a window with two buttons: `Start Detection` and `Stop Detection`.
   - Press `Start Detection` to begin object detection in real-time.
   - Press `Stop Detection` to pause the detection process.

3. Press the `q` key on the keyboard to exit the application.

## Code Explanation

- **Video Capture**: The webcam is opened using OpenCV's `VideoCapture(0)`, where `0` is the default camera index.
  
- **Model Loading**: A pre-trained MobileNet SSD model is loaded using the configuration and weight files.
  
- **Tkinter GUI**: The application GUI is built using Tkinter. It contains two buttons for starting and stopping the object detection.
  
- **Object Detection**: The objects are detected in real-time from the video stream, and bounding boxes, class names, and confidence scores are drawn on the video frames.

- **Image Display**: The frames are updated in the Tkinter window by converting the OpenCV image (BGR format) to RGB and using `ImageTk` to display it.

## Key Functionality

- **start_detection**: Begins the object detection process and continuously updates the video stream.
- **stop_detection**: Stops the detection process but keeps the video feed running.
- **on_key_press**: Listens for keypress events, particularly the `q` key, to quit the application.

## Future Improvements

- Allow users to choose between different object detection models.
- Add functionality to save detected objects or results to a file.
- Enhance the GUI for more user interactions and customization.

## License
This project is licensed under the MIT License.

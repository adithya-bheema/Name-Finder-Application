Name Finder Application

Name Finder Application is a real-time object detection system that uses OpenCV and MobileNet SSD for identifying objects and displaying their names. This project includes a user-friendly web interface built with Flask and HTML, designed to help users learn the names of various objects in English.

Features

Real-Time Object Detection: Identifies objects in real-time using a MobileNet SSD model.

Object Name Identification: Displays the names of recognized objects in English.

Web Interface: A simple and interactive web interface for ease of use.

Future Enhancements

Audio Feedback: Pronounce the names of detected objects.

Multi-Language Translation: Translate object names into multiple languages.

Improved Accuracy: Enhance the model to detect any object accurately.

File Structure

coco.names: Contains 93 object names used by the model for detection.

mobilenet_ssd: The pre-trained MobileNet SSD model used for object detection.

main.py: The main Python script that handles object detection and integrates with the Flask web application.

frozenset: Used for efficient lookup and storage of object names.

templates/: Contains the HTML files for the web interface:

index.html: The page where users interact with the object detection functionality.

start.html: The main landing page of the application.

Installation

Clone this repository:

git clone https://github.com/your-username/name-finder-application.git
cd name-finder-application

Install the required dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Open your browser and go to http://127.0.0.1:5000 to access the web interface.

Usage

Upload an image or use your webcam to detect objects in real-time.

The application will display the detected objects and their names.

Use the web interface to interact with the application.

Prerequisites

Python 3.7 or higher

OpenCV

Flask

Screenshots

(Add screenshots of your application in action here)

Contributing

Contributions are welcome! If you have ideas for improvement or new features, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or suggestions, feel free to contact me at [adithyabheema369@gmail.com].


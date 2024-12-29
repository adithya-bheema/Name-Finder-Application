from flask import Flask, render_template, Response, jsonify, redirect, url_for
import cv2

app = Flask(__name__)

thres = 0.50  # Confidence threshold
is_detection_running = False  # Toggle detection state

# Load class names from the coco.names file
classNames = []
with open('coco.names', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load the pre-trained model
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Initialize VideoCapture object
cap = None  # Initialize later to avoid issues during app launch

def start_camera():
    """Start the camera and set its properties."""
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, 70)
    return cap

def generate_frames():
    """Generate frames for the video feed."""
    global is_detection_running
    cap = start_camera()
    
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Failed to capture image.")
            break

        if is_detection_running:
            # Perform object detection
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            if len(classIds) != 0:
                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    if 0 <= classId < len(classNames):
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1].upper(), 
                                    (box[0] + 10, box[1] + 30),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(img, f"{round(confidence * 100, 2)}%", 
                                    (box[0] + 200, box[1] + 30),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        # Yield frame for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_detection', methods=['POST'])
def start_detection():
    """Start object detection."""
    global is_detection_running
    is_detection_running = True
    return jsonify({"status": "detection_started"})

@app.route('/stop_detection', methods=['POST'])
def stop_detection():
    """Stop object detection."""
    global is_detection_running
    is_detection_running = False
    return jsonify({"status": "detection_stopped"})

if __name__ == "__main__":
    app.run(debug=True)

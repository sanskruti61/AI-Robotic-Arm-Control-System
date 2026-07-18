# AI-Robotic-Arm-Control-System
An AI-powered robotic arm control system built with Python, OpenCV, YOLOv8, PyQt6, QR &amp; ArUco detection, and computer vision for real-time object detection and robotic automation.

---

## 📸 Project Preview
<img width="1740" height="980" alt="Screenshot 2026-07-18 171042" src="https://github.com/user-attachments/assets/f1d4e1d9-5ca9-4d43-9217-4311df2a0bd6" />
<img width="1740" height="980" alt="Screenshot 2026-07-18 171042" src="https://github.com/user-attachments/assets/156b8acd-2c17-4d26-9661-e209369073a1" />
<img width="1740" height="980" alt="Screenshot 2026-07-18 171042" src="https://github.com/user-attachments/assets/400a3c26-60cc-4f32-9b25-7dd291daaf39" />
<img width="1740" height="980" alt="Screenshot 2026-07-18 171042" src="https://github.com/user-attachments/assets/6942146a-6532-43b6-8e55-b8a7319963d7" />




---

## ✨ Features

### 📷 Camera Module
- Live webcam feed
- Real-time FPS display
- Center crosshair overlay
- Professional PyQt6 interface

### 🎨 Color Detection
- Detects:
  - 🔴 Red
  - 🟢 Green
  - 🔵 Blue
  - 🟡 Yellow
- Bounding box around detected object
- Object center coordinates
- Object area calculation

### 🧠 Object Detection
- YOLOv8-powered object detection
- Confidence score display
- Bounding boxes
- Center point tracking
- Coordinate extraction
- Real-time visualization

### 🔳 QR Code Detection
- Detect QR codes
- Decode QR content
- Display detected data
- Bounding box visualization

### 🏷️ ArUco Marker Detection
- Detect ArUco markers
- Marker ID recognition
- Pose visualization
- Marker tracking

### 📊 Information Panel
Displays live information including:
- Current Mode
- FPS
- Resolution
- Detected Object
- Detected Color
- Confidence Score
- Center Coordinates
- Object Area
- QR Data
- ArUco Marker ID
- Robot Connection Status

### 🖥️ Professional GUI
- Dark theme
- Sidebar navigation
- Live camera display
- Status bar
- Console logs
- Modular architecture

---

# 🏗 Project Structure

```text
AI-Robotic-Arm-Control-System
│
├── camera/
│   ├── camera_manager.py
│   ├── color_detection.py
│   ├── object_detection.py
│   ├── qr_detection.py
│   └── aruco_detection.py
│
├── ui/
│   ├── main_window.py
│   ├── camera_widget.py
│   ├── sidebar.py
│   ├── info_panel.py
│   ├── console.py
│   └── styles.py
│
├── utils/
│   ├── fps.py
│   └── helpers.py
│
├── assets/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Technologies Used

- Python 3.11+
- PyQt6
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- pyzbar
- cv2.aruco

---
---

# 🚀 Future Improvements

- Robot arm serial communication
- ESP32 integration
- Pick-and-place automation
- Hand gesture control
- Face recognition
- Voice commands
- Multi-object tracking
- Distance estimation
- AI path planning
- Camera calibration
- Database integration
- Cloud monitoring

---

# 💻 Author

**Sanskruti M. Tapale**




# 📜 License

This project is licensed under the **MIT License**.

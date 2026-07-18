# AI-Robotic-Arm-Control-System
An AI-powered robotic arm control system built with Python, OpenCV, YOLOv8, PyQt6, QR &amp; ArUco detection, and computer vision for real-time object detection and robotic automation.

---

## 📸 Project Preview
<img width="1740" height="980" alt="Screenshot 2026-07-18 171042" src="https://github.com/user-attachments/assets/f1d4e1d9-5ca9-4d43-9217-4311df2a0bd6" />
<img width="1919" height="1009" alt="Screenshot 2026-07-18 170944" src="https://github.com/user-attachments/assets/3969483b-24b6-4b65-9bc8-04548de39eff" />
<img width="1911" height="1009" alt="Screenshot 2026-07-18 170743" src="https://github.com/user-attachments/assets/e14c70f3-2007-4300-81a3-762718158074" />
<img width="1915" height="1011" alt="Screenshot 2026-07-18 170529" src="https://github.com/user-attachments/assets/df1158b2-d4cd-4404-a0f9-bcc147a2ae5d" />







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

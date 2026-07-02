# 🐱 CercaGatti

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)](https://opencv.org/)
[![Ultralytics](https://img.shields.io/badge/YOLO-v8-red)](https://github.com/ultralytics/ultralytics)

**CercaGatti** is an autonomous robot software project designed to detect a cat using a camera, recognize it with YOLO, and decide which direction to move in order to chase it.

> ⚠️ **Current status:** The project is in its early development stages. The physical robot has not been built yet; the software is exclusively tested using a webcam.

---

## 📋 Features

### ✅ Implemented

- **Video capture** — Frame acquisition from the webcam via OpenCV.
- **Camera configuration** — Resolution and FPS settings.
- **Video stream display** — Live window using `cv2.imshow()`.
- **Graceful shutdown** — Exit the application by pressing `q` or clicking the window's close button.
- **Object detection with YOLO** — Real-time object detection in frames using YOLOv8.
- **Result parsing** — Extraction of YOLO detections into a Python data structure (list of dictionaries with bounding boxes, class name, and confidence score).
- **Bounding box drawing** — Visualization of rectangles and class names directly on the frame.
- **Image area division** — Demarcation lines at 40% and 60% of the width to split the frame into left, center, and right areas (test functions for circle and rectangle).

### 🗺️ Roadmap (Planned)

- [ ] Filter detections to exclusively identify cats.
- [ ] Calculate the center of the detected cat.
- [ ] Decide robot direction based on which area the cat belongs to.
- [ ] Motor control for chasing.
- [ ] Cat tracking across consecutive frames.
- [ ] Target loss handling.
- [ ] Performance optimization (FPS, latency reduction).
- [ ] Integration with robot hardware.

---

## 🛠️ Technologies

| Technology | Usage |
| --- | --- |
| **Python 3.8+** | Core language |
| **OpenCV** | Video capture, frame processing, graphical drawing |
| **Ultralytics YOLOv8** | Real-time object detection |
| **NumPy** | Array handling and numerical operations |
| **Supervision** | Computer vision utilities |
| **Git** | Version control |

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/alberellooo/CercaGatti.git
   cd CercaGatti
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the project**

   ```bash
   python show_result.py
   ```

   *(Press `q` to exit the video window)*

---

## 📁 Project structure

```text
CercaGatti/
├── camera.py          # Camera management: initialization,
│                      # frame reading, line drawing, video output and shutdown
├── yolo.py            # YOLO model initialization, object
│                      # detection and result parsing
├── show_result.py     # Result visualization: bounding box
│                      # and class name drawing on the frame
├── config.py          # Project configuration (in development)
├── main.py            # Main entry point (in development)
├── requirements.txt   # Project dependencies
├── README.md          # Documentation (Italian)
├── README_EN.md       # Documentation (English)
└── .gitignore         # Git ignored files
```

### Module responsibilities

- **`camera.py`** — Handles the entire video acquisition pipeline: initializes the webcam, reads frames, retrieves dimensions, draws image division lines, displays the video feed, and manages program exit.

- **`yolo.py`** — Loads the pre-trained YOLOv8 model, performs object detection on a frame, and returns the results in an organized data structure (a list of objects with position, name, and confidence).

- **`show_result.py`** — Takes YOLO results and displays them graphically on the frame by drawing rectangles around detected objects and writing the class name.

- **`main.py`** — Intended to become the main entry point coordinating all modules (currently under development).

---

## 🚦 Project status

The project is in **alpha / early development** stage. Currently the software can:

- Capture real-time video from the webcam.
- Detect generic objects using YOLOv8.
- Display results graphically.
- Divide the image into areas for future directional decisions.

The next step is to filter detections to recognize only cats and begin implementing the decision-making logic for robot movement.

---

## 🤝 Contributing

This is a personal learning and development project. Suggestions, ideas, and feedback are welcome!

---

## 📄 License

Distributed under the MIT License. See the `LICENSE` file for more information.

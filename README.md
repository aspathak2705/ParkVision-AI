# 🚗 ParkVision AI — Smart Parking Detection System

## 🧠 Overview

ParkVision AI is a real-time computer vision system that detects vehicle presence and determines parking slot occupancy using video input. The system leverages deep learning and object tracking to automate parking monitoring and provide live occupancy insights.

It is designed for deployment in smart parking environments such as malls, offices, and urban infrastructure systems.

---

## 🎯 Problem Statement

* Manual parking monitoring is inefficient and not scalable
* Lack of real-time visibility of available parking slots
* Increased congestion due to vehicles searching for parking

---

## 💡 Solution

This system:

* Detects vehicles using deep learning
* Tracks vehicles across frames
* Maps vehicles to parking slots
* Determines slot occupancy in real time

---

## ⚙️ System Architecture

### 🔹 Input

* CCTV / Parking lot video feed

### 🔹 Processing Pipeline

1. Frame extraction using OpenCV
2. Vehicle detection using YOLOv8
3. Object tracking using SORT
4. Slot mapping using polygon-based spatial logic
5. Occupancy detection using centroid-based approach

### 🔹 Output

* Real-time parking slot status
* Total occupied and available slots
* Visual overlay on video

---

## 🧪 Core Modules

### 1. Detection Module

* Model: YOLOv8 (Ultralytics)
* Detects vehicles (cars, bikes, trucks)

### 2. Tracking Module

* Algorithm: SORT (Simple Online and Realtime Tracking)
* Assigns unique IDs to vehicles
* Maintains temporal consistency

### 3. Slot Mapping Module

* Parking slots defined as polygons
* Uses centroid-based spatial mapping
* Applies polygon shrinking for better accuracy

### 4. Visualization Module

* Color-coded slots:

  * 🟢 Green → Empty
  * 🔴 Red → Occupied
* Overlay rendering using OpenCV

---

## 🧰 Tech Stack

* Python
* OpenCV
* NumPy
* YOLOv8 (Ultralytics)
* SORT (Kalman Filter + Hungarian Algorithm)

---

## 📁 Project Structure

```
parkvision-ai/
│
├── main.py
├── detector.py
├── tracker.py
├── slot_mapper.py
├── slot_annotator.py
│
├── config/
│   └── slots.json
│
├── input/
│   └── input.mp4
│
└── output/
```

---

## 🚀 How to Run

### 1. Install Dependencies

```
pip install ultralytics opencv-python numpy filterpy lap
```

### 2. Add Input Video

Place your video inside:

```
input/input.mp4
```

### 3. Annotate Parking Slots

Run:

```
python slot_annotator.py
```

* Click 4 points per slot
* Press **S** to save

### 4. Run Main System

```
python main.py
```

---

## 🎯 Key Features

* Real-time vehicle detection and tracking
* Dynamic parking slot configuration
* Accurate occupancy detection using refined spatial logic
* Clean and intuitive visualization

---

## ⚠️ Limitations

* Performance may drop in low-light or extreme occlusion
* Detection accuracy depends on camera angle and resolution
* Axis-aligned bounding boxes may not perfectly align with angled parking slots

---

## 🚀 Future Improvements

* Multi-camera integration
* Edge deployment (Raspberry Pi)
* Web dashboard for monitoring
* Parking availability prediction using ML

---

## 🎤 Interview Explanation

> “This project uses YOLOv8 for real-time vehicle detection and SORT for tracking. I implemented a polygon-based slot mapping system where each parking slot is defined manually, and occupancy is determined using centroid logic within a refined region. The system provides real-time parking insights and can be deployed in smart infrastructure environments.”

---

## 📌 Author

**Atharva Pathak**

---

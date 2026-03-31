# 🛣️ Smart Road Crack Detection using Image Processing

A Computer Vision project that detects cracks in road surface images using classical image processing techniques (no deep learning). Built using Python and OpenCV as part of a university course project.

---

## 📌 Problem Statement

India has one of the largest road networks (~6.4 million km), but a significant portion suffers from poor maintenance.

Cracked roads lead to:
- 🚧 Accidents (especially for two-wheelers)
- 🚗 Vehicle damage (tyres, suspension)
- 💰 Increased maintenance costs
- 🌧️ Water seepage and road weakening

Manual inspection is:
- Slow
- Expensive
- Inconsistent

👉 This project provides an **automated image-based crack detection system** to assist authorities in identifying and prioritizing repairs.

---

## ✨ Features

| # | Feature | Description |
|--|--------|------------|
| 1 | Image Loading | Supports single and batch processing |
| 2 | Grayscale Conversion | Simplifies image processing |
| 3 | Noise Removal | Gaussian Blur for smoothing |
| 4 | Contrast Enhancement | CLAHE improves visibility |
| 5 | Edge Detection | Canny detects crack boundaries |
| 6 | Thresholding | Adaptive thresholding |
| 7 | Morphological Ops | Clean and refine crack regions |
| 8 | Contour Detection | Identify crack areas |
| 9 | Crack Highlighting | Draw cracks in red |
| 10 | Severity Classification | LOW / MEDIUM / HIGH |
| 11 | Visual Pipeline | Shows all intermediate stages |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Computer Vision:** OpenCV (cv2)
- **Numerical Computing:** NumPy
- **Visualization:** Matplotlib

---
## 🛠️ Tech Stack
- Python
- OpenCV
- NumPy
- Pandas

## ⚙️ Setup Instructions

1. Install dependencies:
pip install opencv-python numpy pandas pillow

2. Run dataset collection:
python face_dataset.py

3. Train model:
python train_model.py

4. Start attendance system:
python recognize.py

## 📊 Output
- Attendance saved in attendance.csv

## 📌 Future Improvements
- Deep Learning models (FaceNet)
- Cloud-based attendance storage
- GUI dashboard


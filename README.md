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

## 📁 Folder Structure
road-crack-detection/
├── data/                  # Input road images
│   ├── sample1.jpg
│   └── sample2.jpg
├── src/                   # Source code
│   ├── main.py            # Entry point — runs the pipeline
│   ├── preprocessing.py   # Grayscale, blur, CLAHE, thresholding
│   ├── detection.py       # Edge detection, morphology, contours
│   └── utils.py           # Load/save images, display, reporting
├── outputs/               # Generated output images
├── requirements.txt       # Python dependencies
├── PROJECT_REPORT.md      # Detailed project report
└── README.md              # This file


#  Virtual Painter using OpenCV

This project is a **Virtual Painter** built using **OpenCV and Python**, allowing you to draw in the air using a colored marker and your webcam. The drawing happens on the screen by detecting objects of specific colors in real-time using HSV color thresholds.

Use the **HSV Calibration Tool** (provided as a separate script) to determine accurate HSV values for any color you want to track.

---

##  Features

- Real-time object detection and tracking using HSV color ranges
- Paint virtually on your webcam feed using a colored marker
- Custom HSV calibration tool to determine color values accurately
- Simple keyboard control (`q` to quit)
- Easily customizable color palette

---


---

##  Demo



---

##  How It Works

1. **HSV Calibration (`color_pick.py`)**  
   Use this tool to tune HSV values using interactive trackbars. It lets you see:
   - The original webcam feed
   - The color mask generated from HSV thresholds
   - The result after applying the mask

   This helps in finding the best HSV values for your object.

2. **Drawing App (`virtual_painter.py`)**  
   Once you have the HSV range:
   - Add the range to the `colors` list
   - Add the corresponding BGR value to `color_values`
   - The script detects the object and draws where it moves

---

##  Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/virtual-painter.git
cd virtual-painter
```
2. **Install the dependencies**
```bash   
 pip install opencv-python numpy
```

---

##  Future Ideas

  - Add gesture recognition to switch colors or clear screen
  - Option to save the drawing to file
  - Use hand-tracking instead of color




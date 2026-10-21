```python
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found")
        return

    colors = ("b", "g", "r")

    for i, color in enumerate(colors):
        hist = cv2.calcHist(
            [img], [i], None, [256], [0, 256]
        )
        plt.plot(hist, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.show()

analyze_histogram("image.jpg")
```
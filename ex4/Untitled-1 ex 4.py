
import cv2
import matplotlib.pyplot as plt

# Read the original image in grayscale
img = cv2.imread("input.jpg", 0)

if img is None:
    print("Error: Image not found!")
else:
    # Apply histogram equalization
    equalized = cv2.equalizeHist(img)

    # Display original and equalized images
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Equalized Image")
    plt.axis("off")

    # Original histogram
    plt.subplot(2, 2, 3)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title("Original Histogram")

    # Equalized histogram
    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.show()

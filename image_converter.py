import numpy as np
import imageio.v3 as imageio
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    """Converts an RGB image to grayscale (0-255)."""
    height, width, _ = image.shape  
    grayscale_image = np.zeros((height, width), dtype=np.uint8)  

    for i in range(height):  
        for j in range(width):  
            r, g, b = image[i, j]  
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)  # Convert to grayscale using the luminance formula
            grayscale_image[i, j] = gray  

    return grayscale_image  

def grayscale_to_binary(image, threshold=128):
    """Converts a grayscale image to binary (black & white)."""
    height, width = image.shape  # Get image dimensions
    binary_image = np.zeros((height, width), dtype=np.uint8)  

    for i in range(height): 
        for j in range(width):  
            binary_image[i, j] = 255 if image[i, j] > threshold else 0  # Assign 255 (white) or 0 (black) based on threshold

    return binary_image  

# Load the image
image = imageio.imread('./image/alpine_car.jpg')

# Convert to grayscale
gray_image = rgb_to_grayscale(image)

# Convert to binary (black & white)
binary_image = grayscale_to_binary(gray_image)

# Display images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original image
axes[0].imshow(image)
axes[0].set_title("Original Image")
axes[0].axis("off")  

# Grayscale image
axes[1].imshow(gray_image, cmap="gray")
axes[1].set_title("Grayscale Image")
axes[1].axis("off")

# Binary image
axes[2].imshow(binary_image, cmap="gray")
axes[2].set_title("Binary Image (Black & White)")
axes[2].axis("off")

plt.show()

# Save the processed images
imageio.imwrite("grayscale_image.jpg", gray_image)
imageio.imwrite("binary_image.jpg", binary_image)

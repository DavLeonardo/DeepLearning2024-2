import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena_gray_512.tif", cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float64)
height, width = img.shape
matriz_zero = np.zeros((height, width))

#! sin intensidad
for i in range(height):
    for j in range(width):
        if (i - height / 2) ** 2 + (j - width / 2) ** 2 < 150**2:
            matriz_zero[i, j] = 1

img_crop = img * matriz_zero

#! con intesidad
for i in range(height):
    for j in range(width):
        if (i - height / 2) ** 2 + (j - width / 2) ** 2 < 150**2:
            matriz_zero[i, j] = 1
        else:
            matriz_zero[i, j] = 0.5

img_intensity = img * matriz_zero

#! mostrar imagen

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_crop, cmap="gray")
plt.axis("off")
plt.title("Imagen cortada")

plt.subplot(1, 2, 2)
plt.imshow(img_intensity, cmap="gray")
plt.axis("off")
plt.title("Imagen sin intensidad")

plt.show()

#! Guardar imagen

cv2.imwrite("image_crop.png", img_crop)
cv2.imwrite("image_intesidad.png", img_intensity)

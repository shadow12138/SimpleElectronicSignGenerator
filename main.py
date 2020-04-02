import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('sign.png')
rows, cols, channels = image.shape

th = 0.5
new_image = np.ones((rows, cols))
for i in range(rows):
    for j in range(cols):
        if channels == 4:
            r, g, b, a = image[i][j]
        else:
            r, g, b = image[i][j]
        if r < th and g < th and b < th:
            new_image[i][j] = 0

plt.imsave('new_sign.png', new_image, cmap='gray')

plt.figure(2)
plt.subplot(211)
plt.axis('off')
plt.imshow(image)
plt.subplot(212)
plt.axis('off')
plt.imshow(new_image, cmap='gray')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('Image.jpg')
plt.imshow(img)
plt.axis('off')

# Cropped Image
cropped_img = img[100:400, 100:400]
plt.imshow(cropped_img)
plt.axis('off')
plt.show()
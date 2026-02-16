from PIL import Image
import numpy as np

img = Image.open("img1.jpg")
img = img.convert("L")
img = img.resize((128, 128))
img_array = np.array(img)
print(img_array)
img_array = img_array.astype("float32")/255.0
print(img_array)
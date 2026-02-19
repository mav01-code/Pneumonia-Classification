from PIL import Image
import numpy as np

img = Image.open("img1.jpg")
img = img.convert("L")
img = img.resize((128, 128))
img_array = np.array(img)
img_array = img_array.astype("float32")/255.0
features = img_array.flatten()
mean = img_array.mean()
std = img_array.std()
m = img_array.min()
M = img_array.max()
features = np.concatenate([features, [mean, std, m, M]])
X = features.reshape(1, -1)
Y = np.array([1])
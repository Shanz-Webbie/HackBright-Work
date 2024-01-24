import climage
from io import BytesIO
import numpy as np

# Converting downloaded file
from PIL import Image
import requests

response = requests.get('https://images.squarespace-cdn.com/content/v1/5f103e5123a13a598106a998/1594903465373-I1453DPQ758S6ORUZF5Z/fortune-cookie-21.jpg')
# Convert to RGB, as files on the Internet may be greyscale, which are not
# supported.
img = Image.open(BytesIO(response.content)).convert('RGB')
# Convert the image to 80col, in 256 color mode, using unicode for higher def.
converted = climage.convert_pil(img, is_unicode=True)
print(converted)

# Convert the image into 50px * 50px, as the convert_array function does not
# perform resizing.
smaller_img_image = img.resize((50, 40))
arr = np.array(smaller_img_image)
output = climage.convert_array(arr, is_unicode=True)
print(output)
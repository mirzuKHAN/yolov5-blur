import cv2
import torch
from PIL import Image, ImageFilter

# What do you want to blur?
keyword = 'person'

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Images
im1 = Image.open('bus.jpg')  # PIL image

# Inference
results = model(im1, size=640)  # batch of images

# Results
results.print()
results.show()  # or .show()

results.xyxy[0]  # im1 predictions (tensor)
print(results.pandas().xyxy[0].at[0, 'xmin'])  # im1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie

for res in results.pandas().xyxy:

    for index, row in res.iterrows():

        if row['name'] != keyword:
            continue

        x1 = round(row['xmin'])
        x2 = round(row['xmax'])
        y1 = round(row['ymin'])
        y2 = round(row['ymax'])

        crop = im1.crop((x1, y1, x2, y2))
        blur = crop.filter(ImageFilter.GaussianBlur(radius=4))
        im1.paste(blur, (x1, y1, x2, y2))

im1.show()
import torch
import pathlib

data_dir = 'test_imgs'
data_dir = pathlib.Path(data_dir)

# Get a list of all jpg files in the directory
cats = list(data_dir.glob('*.jpg'))

batch_size = 32
img_height = 227
img_width = 227
num_classes = 8
nb_epoch = 2

# Loading in yolov5s - you can switch to larger models such as yolov5m or yolov5l, or smaller such as yolov5n
model = torch.hub.load("ultralytics/yolov5", "yolov5s", device="cpu", _verbose=True)
img = 'https://i.ytimg.com/vi/q71MCWAEfL8/maxresdefault.jpg'
results = model(img)
results.save(save_dir='results')
results.crop()
print(results)
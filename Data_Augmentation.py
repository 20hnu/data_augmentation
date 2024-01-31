from keras.preprocessing import image
from  keras.preprocessing.image import ImageDataGenerator
import os
import matplotlib.pyplot as plt

datagen = ImageDataGenerator(
    rotation_range=30,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    width_shift_range=0.2,
    height_shift_range=0.2
)

path ='path to the original image'
for img in os.listdir(path):
  print(img)
  picture = image.load_img(os.path.join(path,img), target_size = (256,256))
  picture = image.img_to_array(picture)
  input_batch = picture.reshape(1,256,256,3)
  i=0
  for output in datagen.flow(input_batch,batch_size=1,save_to_dir = "destination folder"):
    i = i+1
    if i == 10:
      break

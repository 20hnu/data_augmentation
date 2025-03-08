# Data Augmentation Using Keras

## Overview
This project demonstrates data augmentation techniques using Keras' `ImageDataGenerator`. Data augmentation is useful for increasing the diversity of training datasets by applying transformations such as rotation, zooming, flipping, and shifting to images.

## Features
- Applies various augmentation techniques:
  - Rotation
  - Zoom
  - Shear
  - Horizontal flipping
  - Width and height shifting
- Saves augmented images to a specified directory
- Helps improve model generalization for deep learning tasks

## Installation
Ensure you have Python installed along with the required libraries:

```sh
pip install tensorflow keras matplotlib
```

## Usage
Modify the script with the correct paths before running.

### Run the script
```sh
python augment_images.py
```

## Script Breakdown
1. **Define augmentation techniques** using `ImageDataGenerator`.
2. **Loop through images in a directory**, apply transformations, and save the augmented images.
3. **Each image is augmented into 10 transformed versions** and saved in the destination folder.

## Project Structure
```
data_augmentation/
│── Data_Augmentation.py      # Main script for augmentation
│── README.md             # Project documentation
```

## Notes
- Adjust augmentation parameters in `ImageDataGenerator` as needed.
- This script is intended for educational purposes.


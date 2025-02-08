# Author: Worasit Sangjan
# Date: 8 Febuary 2025

import time
import os
from datetime import datetime
from picamera2 import Picamera2

# Set base directories
base_folder = "/home/pi/images"
rgb_folder = os.path.join(base_folder, "rgb")
nir_folder = os.path.join(base_folder, "nir")

# Get current date and time
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H%M%S")

# Create separate folders for rgb and noir images (by date)
rgb_save_folder = os.path.join(rgb_folder, current_date)
nir_save_folder = os.path.join(nir_folder, current_date)

os.makedirs(rgb_save_folder, exist_ok=True)
os.makedirs(nir_save_folder, exist_ok=True)

# Initialize cameras
picam0 = Picamera2(0) # rgb camera
picam1 = Picamera2(1) # noir camera

# Confuigure cameras
config0 = picam0.create_still_configuration()
config1 = picam1.create_still_configuration()

picam0.configure(config0)
picam1.configure(config1)

# Start cameras
picam0.start()
picam1.start()
time.sleep(2) # Allow cameras to adjust

# Define file paths
img_rgb_path = os.path.join(rgb_save_folder, f"rgb_{current_time}.jpg")
img_nir_path = os.path.join(nir_save_folder, f"nir_{current_time}.jpg")

# Capture and save images
picam0.capture_file(img_rgb_path)
picam1.capture_file(img_nir_path)

print(f"Images Captured:")
print(f"RGB Image: {img_rgb_path}")
print(f"NIR Image: {img_nir_path}")

# Stop cameras
picam0.stop()
picam1.stop()
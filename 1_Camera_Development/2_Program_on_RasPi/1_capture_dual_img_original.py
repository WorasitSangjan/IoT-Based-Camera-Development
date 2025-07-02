# Author: Worasit Sangjan
# Date: 8 Febuary 2022

import os
import time
from datetime import datetime
import picamera
from picamera import PiCamera
import cv2
import numpy as np

# Photo session settings
total_photos = 5             # Number of images to take
countdown = 15               # Interval for count-down timer, seconds
 
# Camera settimgs
cam_width = 1280              # Cam sensor width settings
cam_height = 624              # Cam sensor height settings

# Final image capture settings
scale_ratio = 2

# Camera resolution height must be dividable by 16, and width by 32
cam_width = int((cam_width+31)/32)*32
cam_height = int((cam_height+15)/16)*16

# Buffer for captured image settings
img_width = int (cam_width * scale_ratio)
img_height = int (cam_height * scale_ratio)
capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)

# Initialize the camera
camera = PiCamera(stereo_mode='side-by-side', stereo_decimate=False)
camera.resolution=(cam_width, cam_height)
camera.framerate = 20
camera.hflip = False

# Lets start taking photos! 
counter = 0
t2 = datetime.now()
print ("Starting photo sequence")
for frame in camera.capture_continuous(capture, format="bgra", use_video_port=True, resize=(img_width,img_height)):
    t1 = datetime.now()
    cntdwn_timer = countdown - int ((t1-t2).total_seconds())
    
    # If cowntdown is zero - let's record next image
    if cntdwn_timer == -1:
      counter += 1
      filename = '/media/pi/IOT11/image/'+str(t2.strftime("%d-%m-%Y_%H-%M-%S"))+'_'+str(counter) + '.png'
      img_rotate_180 = cv2.rotate(frame, cv2.ROTATE_180)
      cv2.imwrite(filename, img_rotate_180)
      print (' ['+str(counter)+' of '+str(total_photos)+'] '+filename)
      t2 = datetime.now()
      time.sleep(1)
      cntdwn_timer = 0      # To avoid "-1" timer display 
      next
    
    # Break the program when receiving all images
    if counter == total_photos:
      break

print ("Photo sequence finished")

src_dir = '/media/pi/IOT11/image'
up_img = [img for img in os.listdir(src_dir) if img.startswith(t2.strftime("%d-%m-%Y_%H")) and img.endswith('3.png')]

for img in up_img:
    image = cv2.imread(os.path.join(src_dir, img))
    filename = '/media/pi/IOT11/img_upload/' + str(t2.strftime("%d-%m-%Y_%H-%M-%S"))+'.png'
    cv2.imwrite(filename, image)

print('Finished')
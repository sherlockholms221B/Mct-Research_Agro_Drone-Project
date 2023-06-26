
import argparse
import os
import platform
import sys
from pathlib import Path

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode
import cv2,time,math
import numpy as np

# from mathplot import pyplot as plt
# import Jetson.GPIO as GPIO

class Processor:

      def calculate_green_vegetation_hsv(im0s):
            image = np.array(im0s)
            # Convert the image to the HSV color space
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower_green = np.array([30, 50, 50])
            upper_green = np.array([90, 255, 255])
            mask = cv2.inRange(hsv, lower_green, upper_green)
            green_pixels = cv2.countNonZero(mask)
            total_pixels = image.shape[0] * image.shape[1]
            green_vegetation_percentage = (green_pixels / total_pixels) * 100
            green_image = cv2.bitwise_and(image, image, mask=mask)

            return [green_vegetation_percentage,green_image]

      def calculate_green_vegetation_pix(im0s,txt_path,box_cords):

            # Calculate the green vegetation percentage
            img_R = im0s[:,:,0]
            img_G = im0s[:,:,1]
            img_B = im0s[:,:,2]

            #Calculating Excess Green
            img_ExG = (2 * img_G) - img_R - img_B

            #reading the predicted .txt labels
            with open(txt_path + '.txt') as f_labels:
                box_cords=[]
                for line_labels in f_labels:
                    strip_lines=line_labels.strip()
                    listli=strip_lines.split()
                    box_cords.append(listli)

            # masking bounding detected bounding boxes to background pixels, 225
            for ibx in range(len(box_cords)):
                #img_ExG[y:y+h,x:x+w]
                x = math.floor(((float(box_cords[ibx][1])) - (float(box_cords[ibx][3]))*0.5)*img_ExG.shape[1])
                y = math.floor(((float(box_cords[ibx][2])) - (float(box_cords[ibx][4]))*0.5)*img_ExG.shape[0])
                w = math.floor(float(box_cords[ibx][3])*img_ExG.shape[1])
                h = math.floor((float(box_cords[ibx][4]))*img_ExG.shape[0])

                img_ExG[y:y+h,x:x+w] = 255 #masking bounding box pixels with 255 values

            #thresholding the soil/vegetation image
            ret, thresh1 = cv2.threshold(img_ExG, 120, 255, cv2.THRESH_BINARY)

      
      #       green_pixels = np.sum((g > r) & (g > b))
      #       total_pixels = im0s.shape[0] * im0s.shape[1]
      #       print(green_pixels)
      #       green_vegetation_percentage = (green_pixels / total_pixels) * 100
      
      
            return [thresh1]

      
      def obj_class(names_class="Don't spray", obj_data_als=[],im0=[],n='',time_set='5s'):
            # GPIO.setmode(GPIO.MODE)
            # GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]] 
            if str(names_class)==str('person'):
                  total_area=0
                  for *xyxy, conf, cls in obj_data_als:
                        co_ordinate = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        x,y, width ,hieght = co_ordinate
                        area = width * hieght
                        total_area+= area
                  per_cent_csl =math.ceil(total_area * 100)
                  # c_video_frame_capture.capture_image('hello world')
                  test = per_cent_csl-36
                  if test < 20:
                        print(str(test)+'%')
                        # GPIO.output(18,GPIO.HIGH)
                        # time.sleep(per_cent_csl)
                        # GPIO.cleanup()
                  # elif per_cent_csl >= 5 and per_cent_csl < 10:
                  #       print(str(per_cent_csl)+'%')
                  #       # GPIO.output(18,GPIO.HIGH)
                  #       time.sleep(per_cent_csl)
                  #       # GPIO.cleanup()
                  # elif per_cent_csl >= 10 and per_cent_csl <20:
                  #       print(str(per_cent_csl)+'%')
                  #       # GPIO.output(18,GPIO.HIGH)
                  #       time.sleep(per_cent_csl)
                  #       # GPIO.cleanup()
                  # elif per_cent_csl >= 20 and per_cent_csl < 30:
                  #       print(str(per_cent_csl)+'%')
                  #       # GPIO.output(18,GPIO.HIGH)
                  #       time.sleep(per_cent_csl)
                  #       # GPIO.cleanup()
                  # else :
                  #       print(str(per_cent_csl)+'%')
                  #       # GPIO.output(18,GPIO.HIGH)
                  #       time.sleep(per_cent_csl)
                  #       # GPIO.cleanup()
    
            else:
                  print("Warning: the class is not defined")
                  
                  

import torch
import time
import math
import Jetson.GPIO as GPIO

from utils.general import ( xyxy2xywh)


class Processor:
      
      def obj_class(names_class="Don't spray", obj_data_als=[],im0=[],n='',time_set='5s'):
            GPIO.setmode(GPIO.MODE)
            GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]] 
            if str(names_class)==str('cassava'):
                  total_area=0
                  for *xyxy, conf, cls in obj_data_als:
                        co_ordinate = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        x,y, width ,hieght = co_ordinate
                        area = width * hieght
                        total_area+= area
                  per_cent_csl =math.ceil(total_area * 100)
                  
                  if per_cent_csl < 5:
                        print(str(per_cent_csl)+'%')
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(per_cent_csl)
                        GPIO.cleanup()
                  elif per_cent_csl >= 5 and per_cent_csl < 10:
                        print(str(per_cent_csl)+'%')
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(per_cent_csl)
                        GPIO.cleanup()
                  elif per_cent_csl >= 10 and per_cent_csl <20:
                        print(str(per_cent_csl)+'%')
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(per_cent_csl)
                        GPIO.cleanup()
                  elif per_cent_csl >= 20 and per_cent_csl < 30:
                        print(str(per_cent_csl)+'%')
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(per_cent_csl)
                        GPIO.cleanup()
                  else :
                        print(str(per_cent_csl)+'%')
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(time)
                        GPIO.cleanup()
    
            else:
                  print("Warning: the class is not defined")
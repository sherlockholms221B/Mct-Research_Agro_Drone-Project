import torch
import time
# import Jetson.GPIO as GPIO

from utils.general import ( xyxy2xywh)


class Processor:
      
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
                  if True:
                        print(total_area,'out of lope')
    
            else:
                  print("Warning: the class is not defined")
       
                        # print(cls) #this is the given class of the object detected
                        # GPIO.output(18,GPIO.HIGH)
                        # time.sleep(time)
                        # GPIO.cleanup()
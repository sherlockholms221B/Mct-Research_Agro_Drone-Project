import torch
import time
import Jetson.GPIO as GPIO

from utils.general import ( xyxy2xywh)


class Processor:
      
      def obj_class(names_class="Don't spray", obj_data_als=[],im0=[],n='',time='5s'):
            GPIO.setmode(GPIO.MODE)
            GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]] 
            for *xyxy, conf, cls in obj_data_als:
                  if str(names_class)==str('person'):  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist() #Getting the current width,hight and xy cord.add
                        #print(conf) #this is the confidence level
                        # print(cls) #this is the given class of the object detected
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(time)
                        print ('spraying completed')
                        GPIO.cleanup()

      def cal_ord_area(xywh):
                                    #area calculation function
       print(xywh,'cal_ord_area')
       
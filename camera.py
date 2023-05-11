  
    #capture images from videos
    # 
# Name:     c_video_frame_capture.py
# Date:     January 19, 2022
# Author:   Randy Runtsch
#
# Description:
#
# The c_video_frame_capture class displays video from a webcam.
# When the user presses "p" it writes the a frame to a file
# as a JPEG image.
# 
# This classes uses the opencv library to display video and write frames.

# opencv tutorial: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Import the opencv (cv2) and datetime libraries.
import cv2
from datetime import datetime

class c_video_frame_capture:

      def capture_image(text='text'):
            print(text)    
      
      def __init__(self, camera_id, img_file_nm_base):
            self.img_file_nm_base = img_file_nm_base

            #   Define the video capture object.
            self.vid_cap = cv2.VideoCapture(camera_id)

            if not (self.vid_cap.isOpened()):
                  print("Could not open camera.")
                  return

            self.capture_video()

#     def capture_video(self):

#         # Loop infinitely to view video.
#         # When "p" is pressed, save a picture to a file.
#         # When "q" is pressed, quit the program.

#         while(True):
      
#             # Capture the video, frame by frame
#             ret, frame = self.vid_cap.read()
  
#             # Display the resulting frame
#             cv2.imshow('Frame', frame)
      
#             # Handle key presses.
#             key = cv2.waitKey(1)

#             if key == 112:
#                 # Save frame when 'p' (ASCII code 112) is pressed.
#                 self.write_frame(frame)
#             elif key == 113:
#                 # Quit programe when 'q' (ASCII code 113) is pressed.
#                 return

#     def write_frame(self, frame):

#         # Write the video frame to a JPEG file.

#         now_string = self.get_now_string()
#         cv2.imwrite("%s_%s.jpg" % (self.img_file_nm_base, now_string), frame)

#     def get_now_string(self):

        # Return the current date time in this format: "YYYYMMDD_HHMMSS_microsecond".

      #   now = datetime.now()

      #   now_string = now.strftime("%Y") + now.strftime("%m") + now.strftime("%d") + '_' + now.strftime("%H") + now.strftime("%M") + now.strftime("%S") + '_' + now.strftime("%f")

      #   return now_string

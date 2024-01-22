import cv2
from collections import deque

class Stream():
    def __init__(self):
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
                   
    def main(self):
        while True:
            self.ret, self.frame = self.cap.read()
            # cv2.imshow('ca',self.frame)
            # if cv2.waitKey(1) == ord('q'):
            #     break              
    def get_data(self):
        return self.frame
    
def start():
    global video_camera
    video_camera = Stream()
    video_camera.main()
    
def give_data():
    return video_camera.get_data()
        
        
            
        
            
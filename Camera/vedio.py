from picamera import PiCamera
import time
camera = PiCamera()
camera.start_preview()
time.sleep(1)
date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
camera.start_recording('/home/pi/h264/%s.h264'% date) #视频存储路径/home/pi/h264,名称为拍摄时间
time.sleep(5)
camera.stop_recording()
camera.stop_preview()

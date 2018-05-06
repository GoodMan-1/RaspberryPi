from picamera import PiCamera
import time
camera = PiCamera()
camera.start_preview()
time.sleep(1)
date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
camera.capture('/home/pi/jpg/%s.jpg'% date)   #照片路径/home/pi/jpg,名称为拍照时间
camera.stop_preview()

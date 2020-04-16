from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()

camera.start_preview(alpha=150)
for x in range(5):
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y, %H:%M:%S")
    camera.capture('/home/pi/Desktop/{}.jpg'.format(date_time))
    sleep(5)

camera.stop_preview()

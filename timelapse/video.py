import time
from picamera import PiCamera
from os import system

camera = PiCamera()
camera.resolution = (1920, 1080)
# my camera was flipped and upside down - this fixes that


FrameCount = 0
FrameStop = 1 

WAIT = int(FrameStop)*int(SleepTimeL)/60
print('Photography will take approximately ' + str(WAIT) + ' minutes')
print('Taking photos now')
camera.start_preview(alpha = 100)

while (FrameCount < FrameStop):
    print('Picture:' + str(FrameCount) + ' of ' + str(FrameStop))
    camera.capture('image' + str(FrameCount).zfill(4) + '.jpg')
    time.sleep(SleepTimeL);
    FrameCount = FrameCount + 1
    
camera.stop_preview()

# create film
print('converting to film now')
system('ffmpeg -r 24 -i image%04d.jpg -vcodec libx264 -crf 20 -g 15 `date +%Y%m%d%H%M`timelapse.mp4')

# create film
print('moving completed mp4 file')
system('mv *.mp4 ~/timelapse/completed/')

print('done')


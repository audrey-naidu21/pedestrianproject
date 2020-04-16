import time
from os import system

print('converting to film now')
system('ffmpeg -r 24 -i image%04d.jpg -vcodec libx264 -crf 20 -g 15 `date +%Y%m%d%H%M`timelapse.mp4')

# create film
print('moving completed mp4 file')
system('mv *.mp4 ~/timelapse/completed/')


print('done')
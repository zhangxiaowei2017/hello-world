from django.http import HttpResponse
import json
import os
import uuid
import time
def cameraimage(request):
    imagename = str(uuid.uuid1())
    print("imagename---->",imagename)
    time.sleep(1)
    result = os.system("fswebcam -d /dev/video0 --no-banner -r 400*750 /home/pi/zhangxiaowei/Raspberry/weixin/static/" + imagename + ".jpg" );
    print("camera commond result:",result)
    return HttpResponse(imagename + ".jpg","text/plain");


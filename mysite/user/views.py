import time
import json


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import User, User_Profile

from django.http import HttpResponse,JsonResponse

def index(request):
    result={"code":200,"msg":"exec ok","success":True}
    id=time.time()
    print(int(id)+'')
    get=request.GET
    print('params is:',get)
    return JsonResponse(result)

def test(request):
    return HttpResponse('test')

def login(request):
    get=request.GET
    print('params is:',get)
    data=User.objects.all()
    for i in data:
        if(i.username==get['username']):
            result = {"code": 200, "msg": "exec ok", "success": True, "token": i.account_id}
            return JsonResponse(result)
    id = time.time()
    user=User(username=get['username'],password=get['password'],account_id=int(id))
    user.save()
    print('id is:' + str(int(id)))
    result={"code":200,"msg":"exec ok","success":True,"token":int(id)}
    return JsonResponse(result)

def getProfileData(request):
    get = request.GET
    print('params is:', get)
    data = User.objects.get(username='k')
    # print()
    profileData = User_Profile.objects.get(account_id=get['token'])
    if profileData:
        data={"nickName":profileData.nickName,"area":profileData.area,"monitor":profileData.monitor,"address":profileData.address}
        print(profileData.nickName)
        result = {"code": 200, "msg": "find token", "success": False, "data": data}
        return JsonResponse(result)
    else:
        return  {"code": 500, "msg": "not find token right", "success": False, "data":{} }

@csrf_exempt
def updateProfile(request):
    id=time.time()
    print('id is:' + str(int(id)))
    data=json.loads(request.body)
    nickname=data.get("nickName")
    area = data.get("area")
    monitor = data.get("monitor")
    address = data.get("address")
    token=data.get("token")

    profileData = User_Profile.objects.get(account_id=token)

    if profileData:
        User_Profile.objects.filter(account_id=token).update(nickName=nickname,area=area,monitor=monitor,address=address)
        result = {"code": 200, "msg": "profie exist profile ok", "success": True}

    else:
        print(nickname)
        print(area)
        print(monitor)
        print(address)
        profile=User_Profile(avatar='',nickName=nickname,area=area,monitor=monitor,address=address,account_id=token,profile_id=id)
        profile.save()
        result={"code":200,"msg":"create profile ok","success":True}

    if(request.method=='POST'):
        print('post')

    elif(request.method=='GET'):
        print('get')

    return JsonResponse(result)

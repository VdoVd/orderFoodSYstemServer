import time

from django.shortcuts import render
import uuid

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import User

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
    result={"code":200,"msg":"exec ok","success":True}
    get=request.GET
    print('params is:',get)
    id = time.time()
    user=User(username=get['username'],password=get['password'],account_id=int(id))
    user.save()
    print('id is:' + str(int(id)))
    return JsonResponse(result)
@csrf_exempt
def updateProfile(request):
    result={"code":200,"msg":"exec ok","success":True}
    id=time.time()
    print('id is:' + str(int(id)))
    nickname=request.POST.get("nickname")
    print(nickname)
    # return JsonResponse(result)

    if(request.method=='POST'):
        print('post')
    elif(request.method=='GET'):
        print('get')
    return JsonResponse(result)
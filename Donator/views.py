import base64
from django.conf import settings
from django.http import JsonResponse
from Denee.models import Login,Doner
from django.http.response import HttpResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from Login.serializers import LoginDetailsSerializer 
from .serializers import DonerDetailsSerializer 

@csrf_exempt
class DonatorDetailsList(APIView):

    def postSave(request):
        usname = request.POST.get('userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position = 'Doner'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=Doner()
        prod.doner_userName = usname
        prod.doner_name = request.POST.get('doner_name')
        prod.doner_mobileNumber = request.POST.get('doner_mobileNumber')
        prod.doner_email = request.POST.get('doner_email')
        prod.doner_address = request.POST.get('doner_address')
        prod.doner_adharcardNumber = request.POST.get('doner_adharcardNumber')
        # image=request.POST['image'],
        # print(image[0])
        # imgdata = base64.b64decode(image[0])
        # print(usname)
        # path = settings.MEDIA_ROOT + '/Doner_images/' + usname + '.jpeg'
        # print(path)
        # with open(path, 'wb') as f:
        #     f.write(imgdata)
        # prod.doner_image='/Doner_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
  

    
# Defining the function for Change Password
    @csrf_exempt
    def changePassword(request):
        userNme=request.POST.get('userName')
        print(userNme)
        LoginDetails1=Login.objects.filter(userName=userNme).all()
        serializer = LoginDetailsSerializer(LoginDetails1, many = True)
        total_LoginDetails1 = json.dumps(serializer.data)
        total_LoginDetails = json.loads(total_LoginDetails1)
        print(total_LoginDetails)
        #checking given input is matching with databse or not if yes then give permission to going on next page else login failure
        if len(total_LoginDetails) > 0:
            prod=Login()
            password = request.POST.get('oldPassword')
            print(password)
            for item in total_LoginDetails: 
                print(item)
                sha_salt = item['salt']
                Encrypted_Password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes(sha_salt, 'utf-8'), 100000)
                print(Encrypted_Password)
                if item['password'] == str(Encrypted_Password):
                    prod.userName=userNme
                    sha_salt = os.urandom(32)
                    prod.salt = sha_salt
                    new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
                    prod.password= new_key
                    print(new_key)
                    Login.objects.filter(userName = userNme).update(password=new_key,salt = sha_salt)
                    print("s")
                    return HttpResponse("Success")
        return HttpResponse("failure")
        
     # Getting  College Details from database 
    @csrf_exempt
    def DonerDetails(request):
        doner_userName = request.POST.get('doner_userName')
        print(doner_userName)
        DonerDetails1=Doner.objects.filter(doner_userName = doner_userName).all()
        serializer = DonerDetailsSerializer(DonerDetails1, many = True)
        total_DonerDetails1 = json.dumps(serializer.data)
        total_DonerDetails = json.loads(total_DonerDetails1)
        data = {'DonerDetails':total_DonerDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        Doner.objects.filter(doner_userName = request.POST.get('doner_userName')).update(
        doner_name = request.POST.get('doner_name'),
        doner_mobileNumber = request.POST.get('doner_mobileNumber'),
        doner_email = request.POST.get('doner_email'),
        doner_address = request.POST.get('doner_address'),
        doner_adharcardNumber = request.POST.get('doner_adharcardNumber'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
        usname=request.POST.get('doner_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/Doner_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
       
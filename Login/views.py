from Denee.models import Login
from django.http.response import HttpResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from Login.serializers import LoginDetailsSerializer
 

@csrf_exempt
class LoginDetailsList(APIView):

    @csrf_exempt
    def postSave(request):
        prod=Login()
        prod.userName=request.POST.get('userName')
        sha_salt = os.urandom(32)
        prod.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        prod.password = new_key
        prod.save()
        return HttpResponse("Success")

    
    #Function for Login
    @csrf_exempt
    def login(request):
        userName=request.POST.get('userName')
        password=request.POST.get('password')
        print(userName)
        print(password)
        StudentLoginDetails1=Login.objects.all().filter(userName=userName) 
        serializer = LoginDetailsSerializer(StudentLoginDetails1, many = True)
        total_LoginDetails1 = json.dumps(serializer.data)
        total_LoginDetails = json.loads(total_LoginDetails1)
        #print(HODLoginDetails1)
        for item in total_LoginDetails:
            print("s")
            #checking given input is matching with databse or not if yes then give permission to going on next page else login failure
            sha_salt = item['salt']
            Encrypted_Password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes(sha_salt, 'utf-8'), 100000)
            if item['password'] == str(Encrypted_Password):
                print("Success Password")
                if item['position'] == 'Admin':
                    print("Admin")
                    return HttpResponse("Admin")
                print("Doner")
                return HttpResponse("Success")
        return HttpResponse("Failure")

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
        
        
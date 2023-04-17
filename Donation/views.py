import base64
from django.http import JsonResponse
from Denee.models import Donation
from django.http.response import HttpResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import DonationDetailsSerializer 

@csrf_exempt
class DonationDetailsList(APIView):

    def postSave(request):
        prod=Donation()
        prod.doner_userName = request.POST.get('doner_userName')
        prod.admin_userName = request.POST.get('admin_userName')
        prod.date = request.POST.get('date')
        prod.amount = request.POST.get('amount')
        prod.status = request.POST.get('status')
        # image=request.POST['image'],
        # print(image[0])
        # imgdata = base64.b64decode(image[0])
        # print(usname)
        # path = settings.MEDIA_ROOT + '/Donation_images/' + usname + '.jpeg'
        # print(path)
        # with open(path, 'wb') as f:
        #     f.write(imgdata)
        # prod.recipt_image='/Donation_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
  
    # Getting  College Details from database 
    @csrf_exempt
    def DonationDetails(request):
        admin_userName = request.POST.get('admin_userName')
        print(admin_userName)
        DonationDetails1=Donation.objects.filter(admin_userName = admin_userName).all()
        serializer = DonationDetailsSerializer(DonationDetails1, many = True)
        total_DonationDetails1 = json.dumps(serializer.data)
        total_DonationDetails = json.loads(total_DonationDetails1)
        data = {'DonationDetails':total_DonationDetails}
        return JsonResponse(data)
    
    @csrf_exempt
    def DonationList(request):
        DonationDetails1=Donation.objects.all()
        serializer = DonationDetailsSerializer(DonationDetails1, many = True)
        total_DonationDetails1 = json.dumps(serializer.data)
        total_DonationDetails = json.loads(total_DonationDetails1)
        data = {'DonationDetails':total_DonationDetails}
        return JsonResponse(data)
  
    
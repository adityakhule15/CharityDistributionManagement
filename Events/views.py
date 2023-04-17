import base64
from django.http import JsonResponse
from Denee.models import Event
from django.http.response import HttpResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import EventDetailsSerializer 

@csrf_exempt
class LoginDetailsList(APIView):

    def postSave(request):
        prod=Event()
        prod.admin_userName = request.POST.get('admin_userName')
        prod.event_name = request.POST.get('event_name')
        prod.event_address = request.POST.get('event_address')
        prod.date = request.POST.get('date')
        prod.status = request.POST.get('status')
        
        # image=request.POST['image'],
        # print(image[0])
        # imgdata = base64.b64decode(image[0])
        # print(usname)
        # path = settings.MEDIA_ROOT + '/Event_images/' + usname + '.jpeg'
        # print(path)
        # with open(path, 'wb') as f:
        #     f.write(imgdata)
        # prod.event_banerImage='/Event_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
  
    # Getting  College Details from database 
    @csrf_exempt
    def EventDetails(request):
        admin_userName = request.POST.get('admin_userName')
        print(admin_userName)
        EventDetails1=Event.objects.filter(admin_userName = admin_userName).all()
        serializer = EventDetailsSerializer(EventDetails1, many = True)
        total_EventDetails1 = json.dumps(serializer.data)
        total_EventDetails = json.loads(total_EventDetails1)
        data = {'EventDetails':total_EventDetails}
        return JsonResponse(data)
    
    @csrf_exempt
    def EventList(request):
        EventDetails1=Event.objects.all()
        serializer = EventDetailsSerializer(EventDetails1, many = True)
        total_EventDetails1 = json.dumps(serializer.data)
        total_EventDetails = json.loads(total_EventDetails1)
        data = {'EventDetails':total_EventDetails}
        return JsonResponse(data)
  
    
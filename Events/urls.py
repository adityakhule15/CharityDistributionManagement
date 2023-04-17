from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('postSave/', views.EventDetailsList.postSave, name="postSave"),
        path('EventDetails/', views.EventDetailsList.EventDetails, name="EventDetails"),
        path('EventList/', views.EventDetailsList.EventList, name="EventList"),
    ]
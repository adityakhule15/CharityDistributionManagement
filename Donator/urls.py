from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('postSave/', views.DonatorDetailsList.postSave, name="postSave"),
        path('changePassword/', views.DonatorDetailsList.changePassword, name="changePassword"),
        path('donerDetails/', views.DonatorDetailsList.DonerDetails, name="donerDetails"),
        path('update/', views.DonatorDetailsList.update, name="update"),
        path('updateImage/', views.DonatorDetailsList.updateImage, name="updateImage"),
    ]
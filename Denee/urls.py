from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('postSave/', views.AdminDetailsList.postSave, name="postSave"),
        path('changePassword/', views.AdminDetailsList.changePassword, name="changePassword"),
        path('adminDetails/', views.AdminDetailsList.AdminDetails, name="adminDetails"),
        path('update/', views.AdminDetailsList.update, name="update"),
        path('updateImage/', views.AdminDetailsList.updateImage, name="updateImage"),
    ]
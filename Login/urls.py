from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('postSave/', views.LoginDetailsList.postSave, name="postSave"),
        path('login/', views.LoginDetailsList.login, name="login"),
        path('forgotPassword/', views.LoginDetailsList.forgotPassword, name="forgotPassword"),
    ]
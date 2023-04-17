from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('postSave/', views.DonationDetailsList.postSave, name="postSave"),
        path('donationDetails/', views.DonationDetailsList.DonationDetails, name="donationDetails"),
        path('donationList/', views.DonationDetailsList.DonationList, name="donationList"),
    ]
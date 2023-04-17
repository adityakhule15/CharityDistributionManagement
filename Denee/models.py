from django.db import models


''' Models for Login Details '''
class Login(models.Model):
    userName = models.CharField(max_length=100, primary_key = True)
    password = models.CharField(max_length=1000)
    salt = models.CharField(max_length=1000, default= '')
    position = models.CharField(max_length=1000, default='False')
    active = models.CharField(max_length=100, default='False') 
    class Meta:
        db_table = "login";


class Admin(models.Model):
    admin_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    admin_name = models.CharField(max_length=1000) 
    admin_mobileNumber = models.CharField(max_length=200) 
    admin_email = models.CharField(max_length=1000) 
    admin_address = models.CharField(max_length=10000) 
    admin_detailsOfWorkAndWorking = models.CharField(max_length=10000) 
    admin_registrationNumber = models.CharField(max_length=200) #can we have this as username
    admin_image=models.CharField(max_length=10000,null=True)
    class Meta:
        db_table = "admin"


class Doner(models.Model):
    doner_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    doner_name = models.CharField(max_length=1000) 
    doner_mobileNumber = models.CharField(max_length=200) 
    doner_email = models.CharField(max_length=1000) 
    doner_address = models.CharField(max_length=10000) 
    doner_adharcardNumber = models.CharField(max_length=200) #can we have this as username
    doner_image=models.CharField(max_length=10000,null=True)
    class Meta:
        db_table = "doner"

''' Models for Donation Details '''
class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True)
    doner_userName = models.ForeignKey(Doner, default='unknown',on_delete=models.SET_DEFAULT)
    admin_userName = models.ForeignKey(Admin, default='unknown',on_delete=models.SET_DEFAULT)
    date = models.CharField(max_length=200) 
    amount = models.CharField(max_length=200) 
    status = models.CharField(max_length=200) 
    recipt_image=models.CharField(max_length=10000,null=True)

    class Meta:
        db_table = "donation"


''' Models for Event Details '''
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    admin_userName = models.ForeignKey(Admin, default= 'unknown', on_delete=models.SET_DEFAULT) 
    event_name = models.CharField(max_length=100)
    event_address = models.CharField(max_length=10000) 
    date = models.DateField()
    status = models.CharField(max_length=100, default="Coming")
    event_banerImage=models.CharField(max_length=10000,null=True)

    class Meta:
        db_table = "event"

 
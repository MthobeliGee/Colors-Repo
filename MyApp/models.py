from django.db import models

# Create your models here.
class Application(models.Model):
    ApplicationId = models.AutoField(primary_key=True)
    ApplicationStatus = models.CharField(max_length=255)
    EventName = models.CharField(max_length=255)
    StartDate = models.DateTimeField(max_length=255)
    EndDate = models.DateTimeField(max_length=255)
    HostCity = models.CharField(max_length=255)
    HostProvince =models.CharField(max_length=255)
    RepresatativeType = models.CharField(max_length=255)
    ReportSubmitAgreement = models.BooleanField(default=False)
    NumberOfTeam = models.IntegerField(max_length=255)
    MethodOfSelection = models.CharField(max_length=255)
    SelectionApprovedDate = models.DateField(max_length=255)
    TravelDateTime = models.DateTimeField(max_length=255)
    ModeOfTravel = models.CharField(max_length=255)
    

class Represantative(models.Model):
    RepresantativeId = models.AutoField(primary_key=True,)
    FirstName = models.CharField(max_length=255)
    Surname =models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Event = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Province = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)
    RepresanativeLeve = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    IDCopySiubmited = models.TextField(default= "null",blank=False,null=False)
    AcceptanceofTeamAppointment = models.TextField(default= "null",blank=False,null=False)
    

class SelctionOfCommittee(models.Model):
    
    MemberId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    
    


    
    

   
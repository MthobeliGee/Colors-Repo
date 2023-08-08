from django.shortcuts import render,redirect, get_object_or_404
from .models import Application,Represantative, SelctionOfCommittee, TeamOfficials
from django.contrib import messages



def Home(request):
    
   
    return render(request,'MyApp/Home.html')

def CreateApp(request):
    
    if request.method == 'GET':
        
        
        
        return render(request, 'MyApp/CreateApp.html')
    
    if request.method == 'POST':
        
        application = Application.objects.create(
        
                EventName = request.POST['EventName'],
                StartDate = request.POST['StartDate'],
                EndDate = request.POST['EndDate'],
                HostCity = request.POST['HostCity'],
                HostProvince = request.POST['HostProvince'],
                NumberOfTeam = request.POST['NumberOfTeam'],
                MethodOfSelection = request.POST['MethodOfSelection'],
                RepresatativeType= request.POST['RepresatativeType'],
                SelectionApprovedDate = request.POST['SelectionApprovedDate'],
                TravelDateTime = request.POST['TravelDateTime'],
                ModeOfTravel = request.POST['ModeOfTravel'],
        
       )
    messages.success(request, 'The information has been saved')
         
        
        
    return redirect("AddRepp", ApplicationId= application.ApplicationId)

def TeamOfficial_view(request, ApplicationId):
    if request.method =='GET':
    
     return render(request, 'MyApp/TeamOfficial_view.html')
 
    if request.method == 'POST':

        team = TeamOfficials.objects.create(
        TeamOffName = request.POST['TeamOffName'],
        TeamOffSurname = request.POST['TeamOffSurname'],
        TeamOfficialId = request.POST['TeamOfficialId'],
        Gender = request.POST['Gender'],
        Designation = request.POST['Designation'],
        
    )
    messages.success(request, 'The information has been saved')
    return redirect("MemberSelection", ApplicationId = team.ApplicationId)


def AddRepp(request,ApplicationId):
    
    application =get_object_or_404(Application, pk =ApplicationId )
        
    if request.method == 'GET':
        
        return render(request, 'MyApp/AddRepp.html')
        
    if request.method == 'POST':
            
            application = Represantative.objects.create(     
        
            FirstName = request.POST['FirstName'],
            Surname = request.POST['Surname'],
            Gender = request.POST['Gender'],
            PhoneNumber = request.POST['PhoneNumber'],
            Email = request.POST['Email'],
            RepresanativeLeve = request.POST['RepresanativeLeve'],
        )
            
    return redirect("AddRepp",ApplicationId=application.ApplicationId,)


def ViewDetails(request, ApplicationId):
    
    application = get_object_or_404(Application,pk=ApplicationId)
    print(application)
    
    return render(request, 'MyApp/ViewDetails.html',{"application":application})

def UpdateDetails(request, ApplicationId):
    application = get_object_or_404(Application, pk= ApplicationId)
    if request.method =='GET':
        
        return render(request, 'MyApp/UpdateDetails.html', {"application":application})
 

    if request.method =='POST':
        
        numUpdate = 0
        
        if request.POST["EventName"] != application.EventName:
            
            application.EventName =request.POST["EventName"]
            numUpdate += 1
            
        if request.POST["StartDate"] != application.StartDate:
            
            application.StartDate =request.POST["StartDate"]
            numUpdate += 1
            
        if request.POST["EndDate"] != application.EndDate:
            
            application.EndDate =request.POST["EndDate"]
            numUpdate += 1
            
        if request.POST["HostProvince"] != application.HostProvince:
            
            application.HostProvince =request.POST["HostProvince"]
            numUpdate += 1
            
        if request.POST["RepresatativeType"] != application.RepresatativeType:
            
            application.RepresatativeType =request.POST["RepresatativeType"]
            numUpdate += 1
            
        if request.POST["NumberOfTeam"] != application.NumberOfTeam:
            
            application.NumberOfTeam =request.POST["NumberOfTeam"]
            numUpdate += 1
            
        if request.POST["MethodOfSelection"] != application.MethodOfSelection:
            
            application.MethodOfSelection =request.POST["MethodOfSelection"]
            numUpdate += 1
            
        if request.POST["TravelDateTime"] != application.TravelDateTime:
            
            application.TravelDateTime =request.POST["TravelDateTime"]
            numUpdate += 1
            
        if request.POST["ModeOfTravel"] != application.ModeOfTravel:
            
            application.ModeOfTravel =request.POST["ModeOfTravel"]
            numUpdate += 1
            
            
        if numUpdate > 0 :
            application.save()
            messages.success(request, f'{numUpdate} changes made.')
        else:
            messages.success(request, ''+numUpdate +'changes made.')
            
        return redirect("UpdateDetails", ApplicationId = application.ApplicationId)
            
            


def Added_Represantative_list(request):
    queryset = Represantative.objects.all()
    context = {
        "Rep_List":queryset
    }
    return render(request,"MyApp/AddRepp.html", context)

def RepDetails(request, RepresantativeId):
    
    Rep =get_object_or_404(Represantative, pk= RepresantativeId)
    print(Rep)
    
    return render (request, 'MyApp/RepDetails.html',{"Rep":Rep}) 

def MemberSelection(request):
    
    if request.method == 'GET':
        
        return render(request, 'MyApp/MemberSelection.html')
    
    if request.method == 'POST':
        
        obj = SelctionOfCommittee.objects.create(
            
            MemberId = request.POST['MemberId'],
            Name = request.POST['Name'],
            Surname = request.POST['Surname'],
            Gender = request.POST['Gender'],
        )
        
    return redirect("CommitteeMemberDetails",MemberId=obj.MemberId)

def CommitteeMemberDetails(request, MemberId):
    
    obj = get_object_or_404(SelctionOfCommittee, pk= MemberId)
    print(obj)
    
    return render(request, 'MyApp/CommitteeMemberDetails.html', {"obj":obj})

def UpdateCommitteeDetails(request, MemberId):
    obj = get_object_or_404(SelctionOfCommittee, pk = MemberId)
    if request.method == 'GET':
        
        return render(request, 'MyApp/UpdateCommitteeDetails.html',{"obj":obj})
    
    if request.method == 'POST':
        
        numUpdate = 0
        
        if request.POST["MemberId"] != obj.MemberId:
            obj.MemberId = request.POST["MemberId"]
            numUpdate +=1
            
        if request.POST["Name"] != obj.Name:
            obj.Name = request.POST["name"]
            numUpdate +=2
            
        if request.POST["Surname"] != obj.Surname:
            request.POST["Gender"] = obj.Name
            numUpdate +=1
            
        if numUpdate > 0:
            obj.save()
            messages.success(request, f'{numUpdate} changes made')
        else:
            messages.success(request, '' +numUpdate + 'changes made.')
            return redirect("UpdateCommitteeDetails", MemberId = obj.MemberId)
    
    

def AddMember(request):
    if request.method == 'GET':
        
        return render(request, 'MyApp/MemberSelection.html')
    
         
         
            
            
        
            
            
            
        

    
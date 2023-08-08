from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home, name="Home"),
    path('CreateApp', views.CreateApp, name="CreateApp"),
    path('ViewDetails/<int:ApplicationId>', views.ViewDetails, name="ViewDetails"),
    path('UpdateDetails/<int:ApplicationId>', views.UpdateDetails,name="UpdateDetails"),
    path('AddRepp/<int:ApplicationId>', views.AddRepp, name="AddRepp"),
    path('RepDetails/<int:RepresantativeId>/', views.RepDetails,name="RepDetails"),
    path('MemberSelection', views.MemberSelection, name="MemberSelection"),
    path('CommitteeMemberDetails/<int:MemberId>/', views.CommitteeMemberDetails,name="CommitteeMemberDetails"),
    path('UpdateCommitteeDetails/<int:MemberId>/',views.UpdateCommitteeDetails, name="UpdateCommitteeDetails"),
    path('AddMember',views.AddMember,name="AddMember"),
]

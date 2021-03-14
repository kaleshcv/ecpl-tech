
from django.urls import path
from .views import *


urlpatterns = [
    path('home',homePage),
    path('signup',signup),
    path('loginview',loginView),
    path('inventory-home',inventoryHome),


    path('add-inv-cpu',addInvCpu),
    path('add-inv-desktop',addInvDesktop),

    path('inv-report/<int:pk>',invReport),


    path('assign-inv-cpu/<int:iid>,<int:pk>',assignInvCpu),
    path('service-inv-cpu/<int:iid>,<int:pk>',serviceCPU),
    path('return-inv-cpu/<int:pk>',returnCPU),
    path('return-from-agent',returnFromAgent),
    path('return-submit',returnSubmit),
    path('return-from-service/<int:pk>',retunFromService),


]


from django.urls import path
from .views import *


urlpatterns = [
    path('home',homePage),
    path('signup',signup),
    path('loginview',loginView),
    path('inventory-home',inventoryHome),


    path('add-inv-cpu',addInvCpu),

    path('inv-report-cpu',invReportCPU),


    path('assign-inv-cpu/<int:pk>',assignInvCpu),
    path('service-inv-cpu/<int:pk>',serviceCPU),



]

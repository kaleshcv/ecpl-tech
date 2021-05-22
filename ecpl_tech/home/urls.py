
from django.urls import path
from .views import *


urlpatterns = [
    path('',loginView),
    path('accounts/login/',loginView),
    path('home',homePage),
    path('signup',signup),
    path('loginview',loginView),
    path('logoutview',logout_view),
    path('inventory-home',inventoryHome),

    path('select-shift',chooseShift),
    path('data-collection/<str:shift>',dataCollection),
    path('employee-detailed-view',empDetailedView),
    path('employee-detailed-submit',submitDetails),
    path('employee-not-available',empNotAvailable),
    path('view-emp-data',viewEmployeeData),

    path('addtoUserModel',addtoUserModel),

   # path('statusChange',statusChange),


    path('add-inv-cpu',addInvCpu),
    path('add-inv-desktop',addInvDesktop),
    path('add-inv-monitor',addInvMonitor),
    path('add-inv-laptop',addInvLaptop),
    path('add-inv-fortiget',addFortiget),

    path('add-inv-router',addRouter),
    path('add-inv-switch',addSwitch),
    path('add-inv-access',addAccess),
    path('add-inv-printer',addPrinter),
    path('add-inv-mouse',addMouse),
    path('add-inv-keyboard',addKeyboard),
    path('add-inv-pendrive',addPendrive),
    path('add-inv-externaldvd',addExternalDvd),
    path('add-inv-cctv',addCctv),
    path('add-inv-converter',addConverter),
    path('add-inv-projector',addProjector),
    path('add-inv-biometric',addBiometric),
    path('add-inv-externalhdd',addExternalHdd),
    path('add-inv-speaker',addSpeaker),




    path('inv-report/<int:pk>',invReport),


    path('assign-inv-cpu/<int:iid>,<int:pk>',assignInvCpu),
    path('service-inv-cpu/<int:iid>,<int:pk>',serviceCPU),
    path('return-inv-cpu/<int:pk>',returnCPU),
    path('return-from-agent',returnFromAgent),
    path('return-submit',returnSubmit),
    path('return-from-service',returnFromService),
    path('return-service-submit',returnServiceSubmit),


   # path('return-from-service/<int:pk>',retunFromService),


]

import xlwt
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from . import forms
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # form to create user
        profile_form = forms.ProfileCreation(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # login(request,user)
            return render(request,'index.html')
    else:
        form = UserCreationForm()
        profile_form = forms.ProfileCreation()

    return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Login form
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            # redirecting

            return render(request,'index.html')
        else:
            form = AuthenticationForm()
            m='Invalid Credentials !'
            return render(request,'login.html',{'form':form,'m':m})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/loginview')


def homePage(request):
    return render(request,'index.html')
def inventoryHome(request):
    return render(request,'inventory-home.html')
def addInvCpu(request):
    if request.method == 'POST':
        in_date=request.POST['in_date']
        serial_no=request.POST['serial_no']
        ecpl_tag_name=request.POST['ecpl_tag']
        system_name=request.POST['system_name']
        processor=request.POST['processor']
        ram=request.POST['ram']
        hd_type=request.POST['hard_disc_type']
        hd_size=request.POST['hard_disc_size']
        hd_serial_no=request.POST['hard_disc_serial']
        make=request.POST['make']
        model=request.POST['model']
        vendor=request.POST['vendor']


        cpu=Cpu(in_date=in_date,serial_no=serial_no,ecpl_tag_name=ecpl_tag_name,processor=processor,
                ram=ram,hd_type=hd_type,hd_size=hd_size,hd_serial_no=hd_serial_no,make=make,model=model,
                system_name=system_name,vendor=vendor)

        cpu.in_stock=True
        cpu.save()

        return redirect('/inventory-home')

    else:

        return render(request,'add_inv_cpu.html')

def addInvDesktop(request):
    if request.method=='POST':

        desktop_form = forms.DesktopCreation(request.POST, request.FILES)

        if desktop_form.is_valid():

            df = desktop_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.DesktopCreation()
        return render(request, 'add_inv_desktop.html', {'form': form})

def addInvMonitor(request):
    if request.method=='POST':

        monitor_form = forms.MonitorCreation(request.POST, request.FILES)

        if monitor_form.is_valid():

            df = monitor_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.MonitorCreation()
        return render(request, 'add_inv_monitor.html', {'form': form})

def addInvLaptop(request):
    if request.method=='POST':

        item_form = forms.LaptopCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.LaptopCreation()
        return render(request, 'add_inv_laptop.html', {'form': form})


def addFortiget(request):
    if request.method=='POST':

        item_form = forms.FortigetCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.FortigetCreation()
        return render(request, 'add_inv_fortiget.html', {'form': form})

def addRouter(request):
    if request.method=='POST':

        item_form = forms.RouterCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.RouterCreation()
        return render(request, 'add_inv_router.html', {'form': form})

def addSwitch(request):
    if request.method=='POST':

        item_form = forms.SwitchCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.SwitchCreation()
        return render(request, 'add_inv_switch.html', {'form': form})

def addAccess(request):
    if request.method=='POST':

        item_form = forms.AccessCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.AccessCreation()
        return render(request, 'add_inv_access.html', {'form': form})

def addMouse(request):
    if request.method=='POST':

        item_form = forms.MouseCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.MouseCreation()
        return render(request, 'add_inv_mouse.html', {'form': form})

def addKeyboard(request):
    if request.method=='POST':

        item_form = forms.KeyboardCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.KeyboardCreation()
        return render(request, 'add_inv_keyboard.html', {'form': form})

def addPendrive(request):
    if request.method=='POST':

        item_form = forms.PendriveCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.PendriveCreation()
        return render(request, 'add_inv_pendrive.html', {'form': form})


def addPrinter(request):
    if request.method=='POST':

        item_form = forms.PrinterCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.PrinterCreation()
        return render(request, 'add_inv_printer.html', {'form': form})

def addExternalDvd(request):
    if request.method=='POST':

        item_form = forms.ExternalDvdCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.ExternalDvdCreation()
        return render(request, 'add_inv_extdvd.html', {'form': form})

def addCctv(request):
    if request.method=='POST':

        item_form = forms.CctvCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.CctvCreation()
        return render(request, 'add_inv_cctv.html', {'form': form})

def addProjector(request):
    if request.method=='POST':

        item_form = forms.ProjectorCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.ProjectorCreation()
        return render(request, 'add_inv_projector.html', {'form': form})

def addConverter(request):
    if request.method=='POST':

        item_form = forms.ConvertorCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.ConvertorCreation()
        return render(request, 'add_inv_converter.html', {'form': form})

def addBiometric(request):
    if request.method=='POST':

        item_form = forms.BiometricCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.BiometricCreation()
        return render(request, 'add_inv_biometric.html', {'form': form})

def addExternalHdd(request):
    if request.method=='POST':

        item_form = forms.ExternalHddCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.ExternalHddCreation()
        return render(request, 'add_inv_externalhdd.html', {'form': form})

def addSpeaker(request):
    if request.method=='POST':

        item_form = forms.SpeakerCreation(request.POST, request.FILES)

        if item_form.is_valid():

            df = item_form.save(commit=False)
            df.save()
            # login(request,user)
            return redirect('/inventory-home')
    else:
        form = forms.SpeakerCreation()
        return render(request, 'add_inv_speaker.html', {'form': form})


def invReport(request,pk):

    if pk == 1:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                cpu_obj=Cpu.objects.filter(serial_no=serial_no)
                if cpu_obj.count() >0 :
                    cpu_obj = Cpu.objects.get(serial_no=serial_no)
                    data={'cpu':cpu_obj,'id':1}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 1}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            cpu_obj_all=Cpu.objects.all()
            data={'cpu_obj_all':cpu_obj_all,'id':1}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 2:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Desktop.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Desktop.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':2}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 2}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Desktop.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':2}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 3:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Monitor.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Monitor.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':3}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 3}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Monitor.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':3}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 4:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Laptop.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Laptop.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':4}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 4}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Laptop.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':4}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 5:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Fortiget.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Fortiget.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':5}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 5}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Fortiget.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':5}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 6:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Router.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Router.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':6}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 6}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Router.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':6}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 7:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Switch.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Switch.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':7}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 7}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Switch.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':7}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 8:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=AccessControler.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = AccessControler.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':8}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 8}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=AccessControler.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':8}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 9:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Printer.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Printer.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':9}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 9}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Printer.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':9}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 10:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Mouse.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Mouse.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':10}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 10}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Mouse.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':10}
            return render(request,'cpu_inv_report.html',data)


    elif pk == 11:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Keyboard.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Keyboard.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':11}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 11}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Keyboard.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':11}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 12:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Pendrive.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Pendrive.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':12}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 12}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Pendrive.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':12}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 13:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=DvdWriter.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = DvdWriter.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':13}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 13}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=DvdWriter.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':13}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 14:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Cctv.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Cctv.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':14}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 14}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Cctv.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':14}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 15:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Converters.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Converters.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':15}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 15}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Converters.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':15}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 16:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Projector.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Projector.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':16}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 16}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Projector.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':16}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 17:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Biometric.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Biometric.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':17}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 17}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Biometric.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':17}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 18:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=ExternalHardDisc.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = ExternalHardDisc.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':18}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 18}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=ExternalHardDisc.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':18}
            return render(request,'cpu_inv_report.html',data)

    elif pk == 19:
        if request.method == 'POST':
                serial_no=request.POST['serial_no']
                desk_obj=Speaker.objects.filter(serial_no=serial_no)
                if desk_obj.count() >0 :
                    desk_obj = Speaker.objects.get(serial_no=serial_no)
                    data={'cpu':desk_obj,'id':19}
                    return render(request,'cpu_inv_report.html',data)
                else:
                    messages.info(request,'Not Found !!!')
                    data = {'id': 19}
                    return render(request, 'cpu_inv_report.html',data)
        else:
            desk_obj_all=Speaker.objects.all()
            data={'cpu_obj_all':desk_obj_all,'id':19}
            return render(request,'cpu_inv_report.html',data)



################### Assign

def assignInvCpu(request,iid,pk):

    if request.method == 'POST':

        date=request.POST['date']
        item=request.POST['item']
        item_serial=request.POST['serial_no']
        emp_id=request.POST['emp_id']
        emp_name=request.POST['emp_name']
        campaign=request.POST['campaign']
        assigned_by=request.POST['it_name']

        assigned=Assigned(date=date,item=item,item_serial=item_serial,emp_id=emp_id,emp_name=emp_name,
                          campaign=campaign,assigned_by=assigned_by)
        assigned.save()

        # function for changing status
        def changeStatus(item):
            obj = item.objects.get(serial_no=item_serial)
            obj.in_stock = False
            obj.assigned = True
            obj.save()

        if item=='CPU':
            changeStatus(Cpu)
        elif item=='DESKTOP':
            changeStatus(Desktop)
        elif item=='MONITOR':
            changeStatus(Monitor)
        elif item=='LAPTOP':
            changeStatus(Laptop)
        elif item=='FORTIGET':
            changeStatus(Fortiget)
        elif item=='ROUTER':
            changeStatus(Router)
        elif item=='SWITCH':
            changeStatus(Switch)
        elif item=='ACCESS':
            changeStatus(AccessControler)
        elif item=='PRINTER':
            changeStatus(Printer)
        elif item=='MOUSE':
            changeStatus(Mouse)
        elif item=='KEYBOARD':
            changeStatus(Keyboard)
        elif item=='PENDRIVE':
            changeStatus(Pendrive)
        elif item=='DVD':
            changeStatus(DvdWriter)
        elif item=='CCTV':
            changeStatus(Cctv)
        elif item=='CONVERTERS':
            changeStatus(Converters)
        elif item=='PROJECTOR':
            changeStatus(Projector)
        elif item=='BIOMETRIC':
            changeStatus(Biometric)
        elif item=='EHD':
            changeStatus(ExternalHardDisc)
        elif item=='SPEAKER':
            changeStatus(Speaker)


        return redirect('/inventory-home')

    else:

        item_id=iid
        if item_id ==1:
            cpu_obj=Cpu.objects.get(id=pk)
            data={'cpu_obj':cpu_obj}
            return render(request,'assign_inv_cpu.html',data)
        elif item_id ==2:
            cpu_obj = Desktop.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==3:
            cpu_obj = Monitor.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)

        elif item_id ==4:
            cpu_obj = Laptop.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==5:
            cpu_obj = Fortiget.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==6:
            cpu_obj = Router.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==7:
            cpu_obj = Switch.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==8:
            cpu_obj = AccessControler.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==9:
            cpu_obj = Printer.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==10:
            cpu_obj = Mouse.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==11:
            cpu_obj = Keyboard.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==12:
            cpu_obj = Pendrive.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==13:
            cpu_obj = DvdWriter.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==14:
            cpu_obj = Cctv.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==15:
            cpu_obj = Converters.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==16:
            cpu_obj = Projector.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==17:
            cpu_obj = Biometric.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==18:
            cpu_obj = ExternalHardDisc.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)
        elif item_id ==19:
            cpu_obj = Speaker.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'assign_inv_cpu.html', data)




def serviceCPU(request,iid,pk):

    if request.method == 'POST':
        item = request.POST['item']
        date=request.POST['date']
        it_name=request.POST['it_name']
        vendor=request.POST['vendor']
        desc=request.POST['desc']
        item_serial=request.POST['serial_no']

        serv_obj=ServiceCpu(date=date,it_name=it_name,vendor=vendor,desc=desc,item_serial=item_serial,item=item)
        serv_obj.save()

        def changeStatus(item):

            obj = item.objects.get(serial_no=item_serial)
            obj.in_stock = False
            obj.assigned = False
            obj.service = True
            obj.save()

        if item=='CPU':
            changeStatus(Cpu)
        elif item=='DESKTOP':
            changeStatus(Desktop)
        elif item=='MONITOR':
            changeStatus(Monitor)
        elif item=='LAPTOP':
            changeStatus(Laptop)
        elif item=='FORTIGET':
            changeStatus(Fortiget)
        elif item=='ROUTER':
            changeStatus(Router)
        elif item=='SWITCH':
            changeStatus(Switch)
        elif item=='ACCESS':
            changeStatus(AccessControler)
        elif item=='PRINTER':
            changeStatus(Printer)
        elif item=='MOUSE':
            changeStatus(Mouse)
        elif item=='KEYBOARD':
            changeStatus(Keyboard)
        elif item=='PENDRIVE':
            changeStatus(Pendrive)
        elif item=='DVD':
            changeStatus(DvdWriter)
        elif item=='CCTV':
            changeStatus(Cctv)
        elif item=='CONVERTERS':
            changeStatus(Converters)
        elif item=='PROJECTOR':
            changeStatus(Projector)
        elif item=='BIOMETRIC':
            changeStatus(Biometric)
        elif item=='EHD':
            changeStatus(ExternalHardDisc)
        elif item=='SPEAKER':
            changeStatus(Speaker)




        return redirect('/inventory-home')

    else:

        item_id = iid
        if item_id == 1:
            cpu_obj = Cpu.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id == 2:
            cpu_obj = Desktop.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id == 3:
            cpu_obj = Monitor.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id == 4:
            cpu_obj = Laptop.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id == 5:
            cpu_obj = Fortiget.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==6:
            cpu_obj = Router.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==7:
            cpu_obj = Switch.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==8:
            cpu_obj = AccessControler.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==9:
            cpu_obj = Printer.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==10:
            cpu_obj = Mouse.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==11:
            cpu_obj = Keyboard.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==12:
            cpu_obj = Pendrive.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==13:
            cpu_obj = DvdWriter.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==14:
            cpu_obj = Cctv.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==15:
            cpu_obj = Converters.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==16:
            cpu_obj = Projector.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==17:
            cpu_obj = Biometric.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==18:
            cpu_obj = ExternalHardDisc.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)
        elif item_id ==19:
            cpu_obj = Speaker.objects.get(id=pk)
            data = {'cpu_obj': cpu_obj}
            return render(request, 'service-cpu.html', data)



def returnCPU(request,pk):

    if request.method == 'POST':
        date=request.POST['date']
        it_name=request.POST['it_name']
        vendor=request.POST['vendor']
        desc=request.POST['desc']
        item_serial=request.POST['serial_no']

        ret_obj=ReturnCpu(date=date,it_name=it_name,vendor=vendor,desc=desc,item_serial=item_serial)
        ret_obj.save()

        cpu = Cpu.objects.get(serial_no=item_serial)

        cpu.in_stock = False
        cpu.assigned = False
        cpu.service = False
        cpu.out = True
        cpu.save()

        return redirect('/inventory-home')

    else:

        cpu_obj = Cpu.objects.get(id=pk)
        data = {'cpu_obj': cpu_obj}

        return render(request, 'return-cpu.html', data)

def returnFromAgent(request):

    if request.method == 'POST':

        serial=request.POST['serial_no']
        emp_id=request.POST['emp_id']

        item=Assigned.objects.filter(emp_id=emp_id) | Assigned.objects.filter(item_serial=serial)

        if item.count()>0:

            data={'item':item}

            return render(request,'agent-return.html',data)
        else:
            data = {'item': item}
            messages.info(request, 'Not Found !!!')
            return render(request, 'agent-return.html', data)


    item_obj=Assigned.objects.all()
    data={'items':item_obj}

    return render(request,'agent-return.html',data)


def returnSubmit(request):

    if request.method == 'POST':

        serial=request.POST['serial_no']
        emp_id=request.POST['emp_id']
        item=request.POST['item']

        item_obj=Assigned.objects.get(emp_id=emp_id,item_serial=serial)

        item_obj.return_status=True
        item_obj.save()

        def changeStatus(item):
            obj = item.objects.get(serial_no=serial)


            obj.in_stock = True
            obj.assigned=False
            obj.save()


        if item=='CPU':
           changeStatus(Cpu)
        elif item=='DESKTOP':
            changeStatus(Desktop)
        elif item=='MONITOR':
            changeStatus(Monitor)
        elif item=='LAPTOP':
            changeStatus(Laptop)
        elif item=='FORTIGET':
            changeStatus(Fortiget)
        elif item=='ROUTER':
            changeStatus(Router)
        elif item=='SWITCH':
            changeStatus(Switch)
        elif item=='ACCESS':
            changeStatus(AccessControler)
        elif item=='PRINTER':
            changeStatus(Printer)
        elif item=='MOUSE':
            changeStatus(Mouse)
        elif item=='KEYBOARD':
            changeStatus(Keyboard)
        elif item=='PENDRIVE':
            changeStatus(Pendrive)
        elif item=='DVD':
            changeStatus(DvdWriter)
        elif item=='CCTV':

            changeStatus(Cctv)
        elif item=='CONVERTERS':
            changeStatus(Converters)
        elif item=='PROJECTOR':
            changeStatus(Projector)
        elif item=='BIOMETRIC':
            changeStatus(Biometric)
        elif item=='EHD':
            changeStatus(ExternalHardDisc)
        elif item=='SPEAKER':
            changeStatus(Speaker)


        messages.info(request, 'Returned successfully !')

        return render(request, 'agent-return.html')
    else:
        pass


def returnFromService(request):

    if request.method == 'POST':
        serial=request.POST['serial_no']
        item=ServiceCpu.objects.filter(item_serial=serial)
        if item.count()>0:
            data={'item':item}
            return render(request,'service-return.html',data)
        else:
            data = {'item': item}
            messages.info(request, 'Not Found !!!')
            return render(request, 'service-return.html', data)

    item_obj=ServiceCpu.objects.all()
    data={'items':item_obj}

    return render(request,'service-return.html',data)

def returnServiceSubmit(request):

    if request.method == 'POST':
        serial=request.POST['serial_no']
        item=request.POST['item']
        item_obj=ServiceCpu.objects.get(item_serial=serial,service_status=True)
        item_obj.service_status=False
        item_obj.save()

        def changeStatus(item):
            obj = item.objects.get(serial_no=serial)
            obj.in_stock = True
            obj.service=False
            obj.save()

        if item=='CPU':
           changeStatus(Cpu)
        elif item=='DESKTOP':
            changeStatus(Desktop)
        elif item=='MONITOR':
            changeStatus(Monitor)
        elif item=='LAPTOP':
            changeStatus(Laptop)
        elif item=='FORTIGET':
            changeStatus(Fortiget)
        elif item=='ROUTER':
            changeStatus(Router)
        elif item=='SWITCH':
            changeStatus(Switch)
        elif item=='ACCESS':
            changeStatus(AccessControler)
        elif item=='PRINTER':
            changeStatus(Printer)
        elif item=='MOUSE':
            changeStatus(Mouse)
        elif item=='KEYBOARD':
            changeStatus(Keyboard)
        elif item=='PENDRIVE':
            changeStatus(Pendrive)
        elif item=='DVD':
            changeStatus(DvdWriter)
        elif item=='CCTV':
            changeStatus(Cctv)
        elif item=='CONVERTERS':
            changeStatus(Converters)
        elif item=='PROJECTOR':
            changeStatus(Projector)
        elif item=='BIOMETRIC':
            changeStatus(Biometric)
        elif item=='EHD':
            changeStatus(ExternalHardDisc)
        elif item=='SPEAKER':
            changeStatus(Speaker)

        messages.info(request, 'Returned successfully !')

        return render(request, 'service-return.html')
    else:
        pass

@login_required
def chooseShift(request):
    employee_completed = Employees.objects.filter(data_collected=True).order_by('emp_id')
    data = {'employees':employee_completed}
    return render(request,'choose-shift.html',data)


@login_required
def dataCollection(request,shift):

    shift=shift

    employees = Employees.objects.filter(data_collected=False,number_error=False,shift_error=False,other_error=False,shift=shift).order_by('emp_name')
    emp_phone = Employees.objects.filter(number_error=True, shift=shift).order_by('emp_name')
    emp_shift = Employees.objects.filter(shift_error=True, shift=shift).order_by('emp_name')
    emp_other = Employees.objects.filter(other_error=True, shift=shift).order_by('emp_name')

    resigned_returned = Employees.objects.filter(employee_resigned=True,system_returned=True,shift=shift)
    resigned_not_returned = Employees.objects.filter(employee_resigned=True, system_returned=False,shift=shift)


    employees_shift_count = Employees.objects.filter(data_collected=False,shift=shift).count()
    done_shift_count = Employees.objects.filter(data_collected=True, shift=shift).count()
    employees_count = Employees.objects.filter(data_collected=False).count()

    em_done = Employees.objects.filter(data_collected=True)
    em_done_count = Employees.objects.filter(data_collected=True).count()
    emp_wise = Employees.objects.filter(data_collected=True).values('called_by').annotate(dcount=Count('called_by'))

    data={'employees':employees,'em_done':em_done,'employees_count':employees_count,'em_done_count':em_done_count,
          'emp_wise':emp_wise,'shift_count':employees_shift_count,'shift':shift,'shift_count_done':done_shift_count,
          'emp_phone':emp_phone,'emp_shift':emp_shift,'emp_other':emp_other,
          'resigned_returned':resigned_returned,'resigned_not_returned':resigned_not_returned
          }

    return render(request,'employees-details.html',data)

@login_required
def empDetailedView(request):

    if request.method == 'POST':
        id=request.POST['id']
        employee = Employees.objects.get(id=id)
        data={'employee':employee}
        return render(request,'employee-detailed-view.html',data)
    else:
        pass

@login_required
def submitDetails(request):
    from datetime import date
    today = date.today()

    if request.method == 'POST':
        id=request.POST['id']

        e = Employees.objects.get(id=id)
        e.no_of_systems = request.POST['no_of_systems']
        e.pc_or_lap = request.POST['system_type']
        e.make = request.POST['make']
        e.model = request.POST['model']
        e.serial = request.POST['serial_no']
        e.ram = request.POST['ram']
        e.hard_disc = request.POST['hard_disc']
        e.system_remarks = request.POST['system_remarks']

        e.inch_18 = request.POST['18inch']
        e.inch_19 = request.POST['19inch']
        e.inch_20 = request.POST['20inch']
        e.inch_24 = request.POST['24inch']
        e.monitor_remarks = request.POST['monitor_remarks']

        e.head_company = request.POST['headset_company']
        e.head_own = request.POST['own']
        e.head_remarks = request.POST['headset_remarks']

        e.keyboard = request.POST['keyboard']
        e.mouse = request.POST['mouse']
        e.webcam = request.POST['webcam']
        e.other_remarks = request.POST['other_remarks']

        e.sophos = request.POST['sophos']
        e.connectwise = request.POST['connectwise_id']
        e.vpn = request.POST['vpn']
        e.vpn_id = request.POST['vpn_id']

        e.call_date = today
        e.called_by = request.POST['user_name']
        e.called_by_id = request.POST['user_id']
        e.emp_remarks = request.POST['emp_remarks']
        e.email_id = request.POST['email']
        personal = request.POST['personal']

        if personal == 'Yes':
            e.personal_laptop = True
        else:
            e.personal_laptop = False

        e.data_collected = True
        e.number_error = False
        e.shift_error = False
        e.other_error = False

        e.save()
        messages.info(request,'Information Updated !!!')
        return redirect('/select-shift')
    else:
        pass

@login_required
def empNotAvailable(request):

    if request.method=='POST':
        emp_id = request.POST['emp_id']
        reason = request.POST['reason']
        remarks = request.POST['remarks']

        e=Employees.objects.get(emp_id=emp_id)

        if reason == 'phone':
            e.number_error = True
            e.other_error = False
            e.shift_error = False
            e.other_error_remarks = remarks
            e.data_collected = False

            e.called_by = request.POST['user_name']
            e.called_by_id = request.POST['user_id']

            e.save()

        elif reason == 'shift':
            e.shift_error = True
            e.number_error = False
            e.other_error = False
            e.other_error_remarks = remarks
            e.data_collected = False

            e.called_by = request.POST['user_name']
            e.called_by_id = request.POST['user_id']

            e.save()
        elif reason == 'resigned':
            e.data_collected = True
            e.employee_resigned = True
            e.system_returned = True
            e.shift_error = False
            e.number_error = False
            e.other_error = False
            e.other_error_remarks = remarks

            e.called_by = request.POST['user_name']
            e.called_by_id = request.POST['user_id']

            e.save()
        elif reason == 'resigned-not':
            e.data_collected = True
            e.employee_resigned = True
            e.system_returned = False
            e.shift_error = False
            e.number_error = False
            e.other_error = False
            e.other_error_remarks = remarks

            e.called_by = request.POST['user_name']
            e.called_by_id = request.POST['user_id']

            e.save()

        else:
            e.other_error = True
            e.shift_error = False
            e.number_error = False
            e.other_error_remarks = remarks
            e.data_collected = False

            e.called_by = request.POST['user_name']
            e.called_by_id = request.POST['user_id']

            e.save()
        messages.info(request, 'Agent has been moved to Not Available List !!!')
        return redirect('/select-shift')
    else:
        pass

@login_required
def viewEmployeeData(request):

    employees = Employees.objects.filter(data_collected=True).order_by('call_date')

    data = {'employees':employees}
    return render(request,'view-employee-data.html',data)

'''def statusChange(request):

    id_list = [4812,5561,5780,6403,6531,6699]

    for i in id_list:

        e = Employees.objects.get(id=i)
        e.data_collected = False
        e.save()
'''


def addtoUserModel(request):

    empobj=ProfileAdd.objects.all()

    for i in empobj:
        user = User.objects.create_user(id=i.emp_id,username=i.emp_id,password=i.password)
        profile = Profile(id=i.emp_id,emp_name=i.emp_name,emp_id=i.emp_id,email=i.email,user_id=i.emp_id,phone=999999999)
        profile.save()



def viewEmployeeDetailsAll(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        employee = Employees.objects.get(emp_id = emp_id)
        data = {'employee':employee}
        return render(request,'employee-detail.html',data)


def exportData(request):

    if request.method == 'POST':

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['emp_id','emp_name','shift','doj','status','gender','process','emp_desi','personal_no',
                   'emergency_no','aadhar_no','email_id','address','no_of_systems','pc_or_lap',
                   'make','model','serial','ram','hard_disc','system_remarks','inch_18','inch_19','inch_20',
                   'inch_24','monitor_remarks','head_company','head_own','head_remarks','keyboard',
                   'mouse','webcam','other_remarks','sophos','connectwise','vpn','vpn_id','call_date',
                   'called_by','called_by_id','emp_remarks','data_collected','agent_remarks','number_error',
                   'shift_error','other_error','other_error_remarks','employee_resigned','personal_laptop',
                   'system_returned'
                   ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Employees.objects.all().values_list('emp_id','emp_name','shift','doj','status','gender','process','emp_desi','personal_no',
                   'emergency_no','aadhar_no','email_id','address','no_of_systems','pc_or_lap',
                   'make','model','serial','ram','hard_disc','system_remarks','inch_18','inch_19','inch_20',
                   'inch_24','monitor_remarks','head_company','head_own','head_remarks','keyboard',
                   'mouse','webcam','other_remarks','sophos','connectwise','vpn','vpn_id','call_date',
                   'called_by','called_by_id','emp_remarks','data_collected','agent_remarks','number_error',
                   'shift_error','other_error','other_error_remarks','employee_resigned','personal_laptop',
                   'system_returned')

        import datetime
        rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                rows]

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response

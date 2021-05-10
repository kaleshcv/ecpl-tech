from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from . import forms
from .models import *

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
            messages.info(request,'Invalid Credentials !')
            return render(request,'login.html',{'form':form})
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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
                    return render(request, 'cpu_inv_report.html')
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


'''def retunFromService(request,pk):
    if request.method=='POST':

        serial = request.POST['serial_no']

        cpu = Cpu.objects.get(serial_no=serial)
        cpu.service= False
        cpu.in_stock = True
        cpu.save()

        messages.info(request, 'Added to Stock successfully !')
        return redirect('/inv-report-cpu')

    else:
        cpu_obj = Cpu.objects.get(id=pk)
        data = {'cpu_obj': cpu_obj}
        return render(request,'service-return.html',data)'''




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
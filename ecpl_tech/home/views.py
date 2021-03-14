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
            data={'cpu_obj_all':cpu_obj_all}
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
            data={'cpu_obj_all':desk_obj_all}
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



def serviceCPU(request,iid,pk):

    if request.method == 'POST':
        item = request.POST['item']
        date=request.POST['date']
        it_name=request.POST['it_name']
        vendor=request.POST['vendor']
        desc=request.POST['desc']
        item_serial=request.POST['serial_no']

        serv_obj=ServiceCpu(date=date,it_name=it_name,vendor=vendor,desc=desc,item_serial=item_serial)
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
        data={'item':item}

        return render(request,'agent-return.html',data)

    item_obj=Assigned.objects.all()
    data={'items':item_obj}

    return render(request,'agent-return.html',data)



def returnSubmit(request):

    if request.method == 'POST':

        serial=request.POST['serial_no']
        emp_id=request.POST['emp_id']

        item=Assigned.objects.get(emp_id=emp_id,item_serial=serial)
        item.return_status=True
        item.save()
        cpu=Cpu.objects.get(serial_no=serial)
        cpu.in_stock=True
        cpu.save()

        messages.info(request, 'Returned successfully !')

        return render(request, 'agent-return.html')
    else:
        pass
def retunFromService(request,pk):
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
        return render(request,'service-return.html',data)

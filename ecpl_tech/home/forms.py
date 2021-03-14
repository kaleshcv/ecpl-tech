from django import forms
from .models import Profile,Desktop
from django.contrib.auth.models import User


class ProfileCreation(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('email','emp_name','emp_id','phone')


class DesktopCreation(forms.ModelForm):
    class Meta:
        model=Desktop
        fields=('in_date','serial_no','ecpl_tag_name','processor','ram','hd_type','hd_size','hd_serial_no','make','model','vendor','system_name')


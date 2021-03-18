from django import forms
from .models import Profile,Desktop,Monitor,Laptop,Fortiget,Router
from .models import *

from django.contrib.auth.models import User


class ProfileCreation(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('email','emp_name','emp_id','phone')


class DesktopCreation(forms.ModelForm):
    class Meta:
        model=Desktop
        fields=('in_date','serial_no','ecpl_tag_name','processor','ram','hd_type','hd_size','hd_serial_no','make','model','vendor','system_name')


class MonitorCreation(forms.ModelForm):
    class Meta:
        model=Monitor
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name','screen_size')

class LaptopCreation(forms.ModelForm):
    class Meta:
        model=Laptop
        fields=('in_date','serial_no','ecpl_tag_name','processor','ram','hd_type','hd_size','hd_serial_no','battery_serial_no','make','model','vendor','system_name')

class FortigetCreation(forms.ModelForm):
    class Meta:
        model=Fortiget
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')

class RouterCreation(forms.ModelForm):
    class Meta:
        model=Router
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')

class SwitchCreation(forms.ModelForm):
    class Meta:
        model=Switch
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')

class AccessCreation(forms.ModelForm):
    class Meta:
        model=AccessControler
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')

class PrinterCreation(forms.ModelForm):
    class Meta:
        model=Printer
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name','type')
class MouseCreation(forms.ModelForm):
    class Meta:
        model=Mouse
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')

class KeyboardCreation(forms.ModelForm):
    class Meta:
        model=Keyboard
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class PendriveCreation(forms.ModelForm):
    class Meta:
        model=Pendrive
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name','size')
class ExternalDvdCreation(forms.ModelForm):
    class Meta:
        model=DvdWriter
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class CctvCreation(forms.ModelForm):
    class Meta:
        model=Cctv
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class ConvertorCreation(forms.ModelForm):
    class Meta:
        model=Converters
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class ProjectorCreation(forms.ModelForm):
    class Meta:
        model=Projector
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class BiometricCreation(forms.ModelForm):
    class Meta:
        model=Biometric
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class ExternalHddCreation(forms.ModelForm):
    class Meta:
        model=ExternalHardDisc
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
class SpeakerCreation(forms.ModelForm):
    class Meta:
        model=Speaker
        fields=('in_date','serial_no','ecpl_tag_name','model_no','brand_name')
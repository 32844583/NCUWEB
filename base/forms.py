from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Report, Image
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['topic', 'host', 'participants']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'Subject', 'gender', 'real_first_name', 'real_last_name', 'email', 'Self_Intro']

class ReportForm(forms.ModelForm):
    class Meta: 
        model = Report
        fields = ['name']
        widgets = {'name': forms.RadioSelect}

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image', 
        widget = forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model=Image
        fields = ["image"]

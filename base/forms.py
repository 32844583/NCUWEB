from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Report, Image
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def clean_email(self):
        User.email = self.cleaned_data.get('email', '')
        if User.email.endswith("@g.ncu.edu.tw"):
            return User.email
        elif User.email.endswith("@cc.ncu.edu.tw"):
            return User.email
        elif User.email.endswith("@mgt.ncu.edu.tw"):
            return User.email
        else:
            raise forms.ValidationError('invalid.domain')
            
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['topic', 'host', 'participants']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'Subject', 'gender', 'real_first_name', 'real_last_name', 'email', 'bio']

class ReportForm(forms.ModelForm):
    class Meta: 
        model = Report
        fields = ['name']
    
        CHOICES = [
            ('Spam', 'Spam'),
            ('Terrorism', 'Terrorism'),
            ('Discrimination', 'Discrimination'),
            ('Misinformation', 'Misinformation'),
            ('Public Shaming', 'Public Shaming'),
            ('Illegal or Dangerous', 'Illegial or Dangerous'),
            ('Sexual Harrassment', 'Sexual Harassment'),
            ('Else', 'Else'),
        ]
        
        # name = forms.ChoiceField(
        #     widget=forms.RadioSelect,
        #     choices=CHOICES,
        # )
        
        widgets = {'name': forms.RadioSelect}

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        label='Image', 
        widget = forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model=Image
        fields = ["image"]
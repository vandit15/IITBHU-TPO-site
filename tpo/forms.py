from django.forms import *
from tpo.models import *
from django.contrib.auth.models import User


class LeaveForm(ModelForm):
    class Meta:
        model = LeavePage
        fields = '__all__'


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class StartChat(Form):
    Name = forms.CharField(max_length=100)
    Email = forms.CharField(max_length=100)


'''class CmpnyForm(ModelForm):

    class Meta:
        model = CmpnyProfile
        fields = '__all__'
        widget = {'Industry_Sector': forms.CheckboxSelectMultiple}'''


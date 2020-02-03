from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import StudentProfile, Report, StudentUnit

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_email', 'placeholder': 'Email programme', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password1','placeholder':'Password', 'required': 'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password2','placeholder':'Confirm Password', 'required': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password', 'placeholder':'Password','required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class StudentProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
    sirname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'sirname', 'required': 'true'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
    adm_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'adm_number', 'required': 'true'}))
    study_method = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'study_method','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    school = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'school','tabIndex': '-1', 'readonly': 'true',  'required': 'true'}))
    programme = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'programme','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    accademic_year = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'accademic_year','tabIndex': '-1', 'readonly': 'true','required': 'true'}))
    year_of_study = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'year_of_study', 'pattern': '-?[0-9]*(\.[0-9]+)?', 'required': 'true'}))
    profile_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'profile_photo', 'accept':'image/*', 'required': 'true'}))
    class Meta:
        model = StudentProfile
        fields = ['first_name','last_name','sirname','profile_photo','accademic_year','adm_number','school','study_method','year_of_study','programme']



class ReportForm(forms.ModelForm):
    """Form definition for Report."""
    student = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'student', 'required': 'true'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'message', 'row': '4', 'required': 'true'}))
    class Meta:
        """Meta definition for Reportform."""

        model = Report
        fields = ['user', 'student', 'message']
class StudentUnitForm(forms.ModelForm):
    student_unit = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'student_unit','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    
    class Meta:
        model = StudentUnit
        fields = ['student_unit']

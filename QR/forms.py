from django import forms
from .models import Autogen

class AutogenForm(forms.ModelForm):
    student_full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'student_full_name', 'placeholder':'Student Full Name', 'required': 'true'}))
    adm_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'adm_number', 'placeholder':'Admission Number', 'required': 'true'}))
    exam_card_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'exam_card_number', 'placeholder':'Fake Exam Card Number', 'required': 'true'}))

    class Meta:
        model = Autogen
        fields = [
            'student_full_name',
            'adm_number',
            'exam_card_number',
        ]
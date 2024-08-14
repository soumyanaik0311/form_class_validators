from django import forms
from app.models import *

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField()
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        email=self.cleaned_data['email']
        remail=self.cleaned_data['remail']
        if email!=remail:
            raise forms.ValidationError('Email Mismatch !!')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>=1:
            raise forms.ValidationError('Bot detected !!')
from django import forms
from django.forms import fields,widgets


class Fibunacci(forms.Form):
    number=forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Enter number"}))



class Ackermann(forms.Form):
    number1=forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Enter m value "}))
    number2=forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Enter n value"}))
    

class Factorial(forms.Form):
    number=forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Enter n value"}))
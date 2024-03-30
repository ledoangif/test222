from django import forms
from .models import BenhNhan
from datetime import date
class MyForm(forms.Form):
    number_field = forms.IntegerField(label='nhập phần tử',widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
class NhapBN(forms.Form):
    NameBN = forms.CharField(label="Tên bệnh nhân",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),max_length = 200)
    Date = forms.DateField(label="Ngày sinh",widget=forms.DateInput(attrs={'type': 'date','class': 'form-control form-control-sm'}))
    DateK = forms.DateField(label="Ngày khám",widget=forms.DateInput(attrs={'type': 'date','class': 'form-control form-control-sm'}), initial=date.today)
    CCCD = forms.CharField(label="Số CCCD",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),max_length=20)
    UT = forms.BooleanField(label="Ưu tiên",widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False);
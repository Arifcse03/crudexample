from django import forms  
from KhawaDawaApp.models import Khawadawa  
class KhawadawaForm(forms.ModelForm):  
    class Meta:  
        model = Khawadawa  
        fields = "__all__"  
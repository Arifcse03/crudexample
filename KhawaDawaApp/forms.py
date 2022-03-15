from django import forms  
from KhawaDawaApp.models import Khawadawa  
class DateInput(forms.DateInput):
    input_type = 'date'

class KhawadawaForm(forms.ModelForm):  
    class Meta:  
        model = Khawadawa  
        fields = "__all__" 
        widgets = {
            'program_date': DateInput(),
        } 
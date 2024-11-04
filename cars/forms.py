from django import forms
from .models import Car
from datetime import datetime

class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({
                'class': 'form-control'
            })
                        
            if k == 'brand':
                v.widget.attrs.update({
                    'placeholder': 'Brand',
                    'aria-label': 'Brnad'
                })
            
            elif k == 'value':
                v.widget.attrs.update({
                    'aria-label': "Amount (to the nearest dollar)"
                })

            elif k == 'factory_year':
                v.widget.attrs.update({
                    'aria-label': 'Factory year'
                })
                
            elif k == 'model_year':
                v.widget.attrs.update({
                    'aria-label': 'Model year'
                })
                    
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        
        if factory_year is not None:
            if factory_year < 1926:
                self.add_error('factory_year', 'It is not possible to register cars with a factory year before 1926.')
            elif factory_year > int(datetime.now().year):
                self.add_error('factory_year', 'It is not possible to register cars with a factory year after current year.')
        return factory_year
            
    def clean_model_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        model_year = self.cleaned_data.get('model_year')
                
        if factory_year is not None and model_year is not None:
            if -1 <= (int(factory_year) - int(model_year)) <= 1:
                return model_year
            else:
                self.add_error('factory_year', 'The factory year and model year must be no more than one year apart.')
        else:
            return model_year
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None:
            if int(value) < 10000:
                self.add_error('value', 'The value of the car must be greater than R$10,000.')
        return value

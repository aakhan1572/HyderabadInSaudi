from django import forms
from expads.validators import allow_only_images_validator
from .models import Bbgproject
from expads.models import Category, Countrycode,Expatad, CityCode


class BbgprojectForm(forms.ModelForm):
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    Description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Bbgproject
        fields = '__all__'
        widgets = {'countrycode': forms.Select(attrs={ 'class': 'form-select' }),
            'citycode': forms.Select(attrs={ 'class': 'form-select' }),
            'cover_photo' : forms.FileInput(attrs={'class':'form-control mb-3'})
        }    

    def __init__(self, *args, **kwargs):
        super(BbgprojectForm, self).__init__(*args, **kwargs)
        self.fields['citycode'].queryset = CityCode.objects.none()
        if 'countrycode' in self.data:
            try:
                countrycode = self.data.get('countrycode')
                self.fields['citycode'].queryset = CityCode.objects.filter(countrycode_id=countrycode).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.countrycode:
            self.fields['citycode'].queryset = CityCode.objects.filter(countrycode_id=self.instance.countrycode).order_by('name')

from django import forms
from datetime import date as dt
from workadays import workdays as wd
from .models import PegarInfo


class PegarInfoForm(forms.ModelForm):
    class Meta:
        model = PegarInfo
        fields = ['nome_moeda','data_inicio', 'data_fim']

#A função clean é a utilizada para fazer validações personalidades de modo geral no FORM
    def clean(self):
        datainicio = self.cleaned_data.get('data_inicio')
        datafim = self.cleaned_data.get('data_fim')
        today = dt.today()
#Criei a condição em dias úteis e não contando feriados (country=None)
        if wd.networkdays(datainicio, datafim, country=None) <= 5 and wd.networkdays(datainicio, datafim, country=None) >= 1:
            if datainicio <= today or datafim <= today:
                return self.cleaned_data
#Houve a necessidade de validar se os dias eram iguais pois isso poderia gerar erro
        elif datainicio == datafim:
            self.add_error('data_inicio', "As duas datas não pode ser iguais")
#Criei a condição pois a data inicio sendo superior ou igual a data de hoje a data fim seria maior
        elif datainicio >= today:
            self.add_error('data_inicio',"A data inicio não pode ser maior ou igual a hoje")
        else:
            self.add_error('data_inicio', 'Selecione no máximo 5 dias úteis')

from .models import PegarInfo
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import PegarInfoForm

#Utilizei os class based views por ser mais ágil e eficiente na utilização


class PegarInfoList(ListView):
    model = PegarInfo


class PegarInfoDetail(DetailView):
    model = PegarInfo

#Criei o form class para utilizar as validações personalizadas no FORM


class PegarInfoCreate(CreateView):
    model = PegarInfo
    form_class = PegarInfoForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class PegarInfoUpdate(UpdateView):
    model = PegarInfo
    form_class = PegarInfoForm
    #Não utilizei o Reverse Lazy pois estou enviando diretamente para a raiz da url
    success_url = '/'


class PegarInfoDelete(DeleteView):
    model = PegarInfo
    # Não utilizei o Reverse Lazy pois estou enviando diretamente para a raiz da url
    success_url = '/'

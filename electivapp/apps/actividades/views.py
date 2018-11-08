from django.views.generic import FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse

from .models import TipoActividad
from .forms import TipoActividadForm

# Create your views here.

class TiposActividadFormView(LoginRequiredMixin, FormView):
    template_name = 'users/user_form.html'
    form_class = TipoActividadForm

class TiposActividadListView(LoginRequiredMixin, ListView):
    template_name = 'actividades/tipoactividad_list.html'
    model = TipoActividad
    context_object_name = 'tipos'

class TiposActividadDeleteView(LoginRequiredMixin, ListView):
    template_name = 'account/signup.html'
    model = TipoActividad
    context_object_name = 'tipos'

class Test(FormView):
    template_name = 'users/user_form.html'
    form_class = TipoActividadForm
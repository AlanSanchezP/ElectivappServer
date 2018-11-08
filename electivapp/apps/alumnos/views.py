from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .models import Alumno

# Create your views here.
class AlumnosListView(LoginRequiredMixin, TemplateView):
    template_name = 'alumnos/alumno_list.html'
    # model = Alumno
    # context_object_name = 'alumno'
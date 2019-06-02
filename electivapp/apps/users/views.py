from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, ListView, RedirectView, UpdateView, FormView
from django.http import HttpResponseRedirect

from .forms import UserCreationForm
from electivapp.core.mixins import AdminStaffRequiredMixin

User = get_user_model()

class HomepageView(AdminStaffRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(AdminStaffRequiredMixin, ListView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()

class UserFormView(AdminStaffRequiredMixin, FormView):
    model = User
    template_name = 'users/user_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user.is_superuser = True
        user.is_staff = True
        user.save()
        messages.add_message(
                self.request, 
                messages.SUCCESS, 
                "Usuario {0} dado de alta con éxito.".format(user.username),
            )

        return HttpResponseRedirect(self.get_success_url())

user_form_view = UserFormView.as_view()


class UserUpdateView(AdminStaffRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(AdminStaffRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

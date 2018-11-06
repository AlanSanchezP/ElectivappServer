from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse

# Create your views here.

class Test(View):
    @staticmethod
    def get(request):
        return HttpResponse('test')
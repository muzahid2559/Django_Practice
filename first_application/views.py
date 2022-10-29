from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.

# function base view
# def index_test(request):
#     return HttpResponse("Hello World")

# class base view
# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("Hello World")


class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simple_text_1'] = 'simple_text_1'
        context['simple_text_2'] = 'simple_text_2'
        return context

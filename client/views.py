from django.shortcuts import render
from django.views.generic.base import View

class BasePage(View):
    
    def get(self, request):
        context = {'name': 'John'}

        return render(request, 'base.html', context)

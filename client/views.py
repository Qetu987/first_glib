from django.shortcuts import render
from django.views.generic.base import View
from client.models import Task

class IndexPage(View):
    
    def get(self, request):
        tasks_list = Task.objects.all()
        
        context = {
            'name': 'John', 
            'title': 'Index', 
            'tasks': tasks_list,
        }

        return render(request, 'test_pages/index.html', context)


class SubPagePage(View):
    
    def get(self, request):
        context = {'name': 'Bob', 'title': 'Sub page'}

        return render(request, 'test_pages/sub_page.html', context)
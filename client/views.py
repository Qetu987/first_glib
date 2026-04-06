from django.shortcuts import render
from django.views.generic.base import View

class IndexPage(View):
    
    def get(self, request):
        context = {'name': 'John'}

        return render(request, 'test_pages/index.html', context)


class SubPagePage(View):
    
    def get(self, request):
        context = {'name': 'Bob'}

        return render(request, 'test_pages/sub_page.html', context)
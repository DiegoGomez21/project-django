from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse


class HelloWorld(View):
    def get(self, request):
        data = {
            'name' : 'diego siu',
            'years' : '19',
            'codes' : ['python', 'django', 'React']
        }
        return render(request, 'posts/hello_world.html', context=data)


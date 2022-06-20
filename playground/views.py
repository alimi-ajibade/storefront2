from django.shortcuts import render
import requests


def say_hello(request):
    requests.get('http://httpbin.org/delay/2')
    return render(request, 'hello.html', {'name': 'David'})

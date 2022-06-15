from django.shortcuts import render
from playground.tasks import notify_customers


def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'David'})

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def main(request: WSGIRequest) -> object:
    return render(request, 'mainapp/mainpage.html')


def about(request: WSGIRequest) -> object:
    return render(request, 'mainapp/aboutpage.html')

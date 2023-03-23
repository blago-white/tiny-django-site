from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def main(request: WSGIRequest) -> object:
    page_data = dict(
        title='main page',
        text_values=['some', 'hello', '123']
    )

    return render(request, 'mainapp/mainpage.html', page_data)


def about(request: WSGIRequest) -> object:
    return render(request, 'mainapp/aboutpage.html')

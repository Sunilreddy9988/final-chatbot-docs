from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import FAQ


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    print("Fetching Home")
    return render(request, "Try2.html")

def getData(request):
    print("Entered getData")
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            print("Entered GET Request")
            user_input = request.GET["qData"]
            faqs = FAQ.objects.filter(question__contains=user_input)
            if faqs:
                answer = faqs[0].answer
            else:
                answer = "I'm sorry, I couldn't find an answer to that question."
            return JsonResponse({'Answer': answer})
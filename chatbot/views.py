from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import FAQ
from django.forms.models import model_to_dict

interactionList = []

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

def chatbot(request):
    if request.method == 'POST':

        global interactionDict
        user_input = request.POST['user_input']
        faqs = FAQ.objects.filter(question__contains=user_input)
        if faqs:
            answer = faqs[0].answer
        else:
            answer = "I'm sorry, I couldn't find an answer to that question."
        interactionList.append([user_input, answer])
        return redirect(chatbot)
        
    if request.method == 'GET':
        return render(request, 'try.html', {'interactionList': interactionList})



def chatbot_ajax(request):

    global interactionDict
    if request.method == 'POST':

    # if request.is_ajax():
        question = request.POST.get('user_input')
        faqs = FAQ.objects.filter(question__contains=question)
        if faqs:
            answer = faqs[0].answer
        else:
            answer = "I'm sorry, I couldn't find an answer to that question."
        return HttpResponse({'answer': answer})
    else:
        return render(request, 'try.html')



def faq_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        faqs = FAQ.objects.filter(question__contains=question)
        if faqs:
            answer = faqs[0].answer
        else:
            answer = "I'm sorry, I couldn't find an answer to that question."
        return render(request, 'faq.html', {'answer': answer})
    else:
        return render(request, 'faq.html')
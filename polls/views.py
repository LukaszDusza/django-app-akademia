from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    # output = ', '.join([q.question_text for q in question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'question_list' : question_list
        # jest to dict i mozna dodac wiele kluczy i wartosci
        }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Wybrałeś pytanie: %s." % question_id)

def results(request, question_id):
    response = "Wybrałeś rezultat: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Zagłosowałeś na pytanie: %s." % question_id)
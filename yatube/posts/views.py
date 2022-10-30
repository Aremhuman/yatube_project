from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request):
    return HttpResponse('Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
                        'если у тебя нет правильных <s>вопросов</s> запросов.')

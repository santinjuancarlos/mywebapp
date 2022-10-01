from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
#import json
from .models import Question,Choice
from django.template import loader

# Create your views here.
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'mensaje': 'Lista de preguntas',
        'ultimas_preguntas': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
'''
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'ultimas_preguntas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Lista de preguntas'
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        query=Question.objects.order_by('-pub_date')[:5]
        return query

'''def hola_dos(request):
    return HttpResponse(str(datetime))'''

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'mensaje': 'Detalle de la pregunta','question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

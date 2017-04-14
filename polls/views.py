from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext,loader
# in line 1 shortcuts can be written to the long path ie.django.db.models.query.QuerySet.get


def index(request):
    latest_question_list = Question.objects.order_by('date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
           'latest_question_list':latest_question_list})     
    return HttpResponse(template.render(context))

#in latest_question_text we are makin an object with 5 qns
#in output we are setting up the the output of the qns as there will be (,) saperated
#in result, all qns will be in uordered list and a link goes to /polls/qn_id which triggers the detail method defined in url.py


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id )
    return render(request, 'polls/details.html', {'question': question})

def result(request, question_id):
    return HttpResponse("youre watching the result of question no. %s" % question_id)

def vote(request, question_id):
    return HttpResponse("youre voting the question no. %s" % question_id)

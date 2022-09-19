from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import Question, Choice

# Display all the question 
def index(request):
	# latest_question_list = Question.objects.order_by('pub_date')
	# a shortcut get_list_or_404
	latest_question_list = get_list_or_404(Question)
	
	'''output = [question.question_text for question in latest_question_list]
	return HttpResponse(output)'''

	'''template = loader.get_template('polls/index.html')
	context = {'latest_question_list':latest_question_list}
	return HttpResponse(template.render(context, request))'''
	# a shortcut render
	return render(request, 'polls/index.html', {'latest_question_list':latest_question_list}, content_type='text/html')

class HomeView(generic.ListView):
	queryset = Question.objects.order_by('pub_date')
	context_object_name = 'latest_question_list'
	template_name = 'polls/index.html'

# display the detail of the question
def detail(request, question_id):
	'''
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('No question with that id available')
	'''
	# a shortcut get_object_or_404
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})	


class QuestionDetail(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

# The voting logic
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question':question, 
			'error_message':"You did not select any choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		'''Always return a HttpResponseRedirect after successfully dealing with a POST data
		This prevents the data from being posted twice if the user hits the back button'''
		# return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

		# redirect (a shortcut for HttpResponseRedirect)
		return redirect(question)

# Display the result
def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question':question})	

# Let the users add some question.
def add_question(request):
	if request.method == 'POST':
		question = Question(question_text=request.POST['question_text'])
		question.save()
		choice1 = question.choice_set.create(choice_text=request.POST['choice_text1'])
		choice2 = question.choice_set.create(choice_text=request.POST['choice_text2'])
		choice3 = question.choice_set.create(choice_text=request.POST['choice_text3'])
		choice4 = question.choice_set.create(choice_text=request.POST['choice_text4'])
	return render(request, 'polls/add_question.html')

from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from qna.models import Question, Answer
from .forms import UserForm
from django.template import RequestContext


def public_profile(request,user_name):
    uname = User.objects.get(username=user_name)
    user_questions = uname.question_set.all()
    user_answers = uname.answer_set.all()
    context = {
         'uname': uname.username,
         'my_questions': user_questions,
         'my_answers': user_answers}
    return render(request,'profiles/user_home.html',context)

def register_user(request):
    registered = False
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response('profiles/register.html',
                          {'user_form':user_form, 'registered':registered},context)
        
        
@login_required
def home(request):
    my_questions = Question.objects.questions_for_user(request.user)
    my_answers = Answer.objects.answers_for_user(request.user)
    context = {
        'my_questions': my_questions,
        'my_answers': my_answers}
    return render(request,'profiles/home.html', context)

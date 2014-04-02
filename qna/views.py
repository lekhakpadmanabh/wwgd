from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from qna.models import Question, Vote, Answer, AnswerVote
from .forms import QuestionForm, AnswerForm, VoteForm, AnswerVoteForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


@login_required
def new_question(request):
    if request.method == 'POST':
        asker = Question(submitter = request.user)
        form = QuestionForm(data=request.POST, instance = asker)
        if form.is_valid():
            new_qtn = form.save()
            return HttpResponseRedirect(reverse('qna_detail',args=(new_qtn.pk,)))
        else:
            form = QuestionForm()
            return render(request, 'qna/new_question.html',{'form':form})
    else:
        form = QuestionForm()
        return render(request, 'qna/new_question.html',{'form':form})

@login_required
def new_answer(request,pk):
    if request.method == 'POST':
        ans_question = Question.objects.get(pk=pk)
        answering_user = Answer(answerer = request.user,question = ans_question)
        
        form = AnswerForm(data=request.POST, instance = answering_user)
        if form.is_valid():
            new_ans = form.save()
            return HttpResponseRedirect(reverse('qna_detail',args=(new_ans.question.pk,)))
        else:
            form = AnswerForm()
            return render(request,'qna/new_answer.html',{'form':form})
    else:
        form = AnswerForm()
        return render(request,'qna/new_answer.html',{'form':form})

from django.views.generic.edit import FormView

class VoteFormView(FormView):
    form_class = VoteForm
    def form_valid(self,form):
        question = get_object_or_404(Question,pk = form.data['question'])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user,question=question)
        has_voted = ( prev_votes.count() > 0)
        if not has_voted and user != question.submitter:
            v = Vote.objects.create(voter=user, question=question)
            print("voted")
        return redirect('qna_home')
    def form_invalid(self, form):
        print("invalid")
        return redirect("qna_home")

class AnswerVoteFormView(FormView):
    form_class = AnswerVoteForm
    def form_valid(self,form):
        answer = get_object_or_404(Answer,pk = form.data['answer'])
        user = self.request.user
        prev_votes = AnswerVote.objects.filter(voter=user,answer=answer)
        has_voted = ( prev_votes.count() > 0)
        if not has_voted and user != answer.answerer:
            v = AnswerVote.objects.create(voter=user, answer=answer)
            print("voted")
        return redirect('qna_home')
    def form_invalid(self, form):
        print("invalid")
        return redirect("qna_home")


class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.all()
    total_qtns = Question.objects.count()
    total_users = User.objects.count()
    total_ans = Answer.objects.count()

    paginate_by = 15
    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context.update({'total_qtns': self.total_qtns, 'total_users': self.total_users, 'total_ans':self.total_ans,})
        return context

def question_detail(request,pk):
    question = Question.objects.get(pk=pk)
    answer_list = question.answer_set.all()
    vote_list = Vote.objects.filter(question=pk)
    context = {'question':question,
               'answer_list':answer_list,
               'vote_list':vote_list}
    return render(request,'qna/question_detail.html',context)

"""class QuestionDetailView(DetailView):
    model = Question"""



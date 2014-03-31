from django.forms import ModelForm
from .models import  Question, Answer, Vote, AnswerVote

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('submitter','rank_score')


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('answerer','question')

class VoteForm(ModelForm):
    class Meta:
        model = Vote

class AnswerVoteForm(ModelForm):
    class Meta:
        model = AnswerVote

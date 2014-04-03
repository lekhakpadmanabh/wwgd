from django.forms import ModelForm
from .models import  Question, Answer, Vote, AnswerVote
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class QuestionForm(ModelForm):
    detail = forms.CharField(widget = SummernoteWidget())
    class Meta:
        model = Question
        exclude = ('submitter','rank_score')
    def __init__(self, *args, **kwargs):
        super(QuestionForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'Succint title for your question...'})
        self.fields['tags'].widget.attrs.update({'class':'form-control','placeholder':'Enter one or more tags as csv(required)'})


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

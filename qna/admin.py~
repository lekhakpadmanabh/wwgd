from django.contrib import admin
from qna.models import Question, Vote, Answer
from django_summernote.admin import SummernoteModelAdmin

class QuestionAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)

class AnswerAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)



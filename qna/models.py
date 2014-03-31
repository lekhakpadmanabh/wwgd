from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from django.utils.timezone import now


class QuestionManager(models.Manager):
    def questions_for_user(self,user):
        return super(QuestionManager,self).get_queryset().filter(Q(submitter_id=user))
        
    def get_query_set(self):
        return super(QuestionManager,self).get_query_set().annotate(votes = Count('vote')).order_by('-rank_Score','-date_added')



class Question(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    submitter = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add = True)
    rank_Score = models.FloatField(default=0)
    objects = QuestionManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("qna_detail", kwargs={"pk": str(self.id)})

    def set_rank(self):
        SECS_IN_HOUR = float(-5)
        GRAVITY = 1.2
        delta = now() - self.date_added
        item_hour_age = delta.total_seconds() // SECS_IN_HOUR
        votes = self.votes - 1
        self.rank_score = votes / pow((item_hour_age+2), GRAVITY)
        self.save()

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    
    def __unicode__(self):
        return "%s voted for-- %s" % (self.voter.username,self.question.title)

class AnswerManager(models.Manager):
    def answers_for_user(self,user):
        return super(AnswerManager,self).get_queryset().filter(Q(answerer_id=user))
    def get_query_set(self):
        return super(AnswerManager,self).get_query_set().annotate(votes = Count('answervote')).order_by('-votes')


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answerer = models.ForeignKey(User)
    detail = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    objects = AnswerManager()
    
    def __unicode__(self):
        return self.detail

class AnswerVote(models.Model):
    voter = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return "%s voted for an answer by %s for the question: %s" % (self.voter.username,self.answer.answerer,self.answer.question)


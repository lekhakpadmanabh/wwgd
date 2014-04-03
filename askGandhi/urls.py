from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qna.views import QuestionListView, VoteFormView, AnswerVoteFormView, new_question, question_detail, new_answer
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'askGandhi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',QuestionListView.as_view(),name='qna_home'),
    url(r'^(?P<pk>\d+)/$',question_detail,name='qna_detail'),
    url(r'^ask$',new_question,name='qna_ask'),
    url(r'^(?P<pk>\d+)/answer$',new_answer,name='qna_answer'),
    url(r'^vote$',login_required(VoteFormView.as_view()),name='vote'),
    url(r'^answervote$',login_required(AnswerVoteFormView.as_view()),name='answervote'),
    url(r'^people/',include('profiles.urls')),
    url(r'^tags/',include('qnatags.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    
    url(r'^login/$','login',
    {'template_name':'login.html'},
    name='qna_login'),
    
    url(r'^logout/$','logout',
    {'next_page':'qna_home'},
    name='qna_logout'),
    )


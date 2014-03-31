from django.shortcuts import render
from taggit.models import Tag
from qna.models import Question

def all_tags(request):
    tags = Tag.objects.all()
    context = {'tags':tags}
    return render(request, 'qnatags/all_tags.html',context)

def tag_details(request,tag_name):
    question_list = Question.objects.filter(tags__name = tag_name)
    context = { 'question_list': question_list}
    return render(request,'qnatags/tag_detail.html',context)

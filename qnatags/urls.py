from django.conf.urls import patterns, include, url

urlpatterns = patterns('qnatags.views',
    url(r'^all/$','all_tags',name='all_tags_home'),
    url(r'^(?P<tag_name>.+)/$','tag_details',name = 'tag_details'),
    )

from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views',
    url(r'^me/$','home',name='profile_home'),
    url(r'^user/(?P<user_name>[\w]+)/$','public_profile',name='user_public_profile'),
    url(r'^signup/$','register_user',name='signup')
    )

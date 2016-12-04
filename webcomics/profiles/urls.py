from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url('^login/$', views.login_or_signup),
    url(r'^logout/', logout),

    url('^register/$', views.register),
    url(r'^authenticate/', views.authenticate_user),

    url(r'^preferences/$', views.preferences),
    # url(r'^user/(?P<slug>[^\.]+)/preferences$', views.UserEdit.as_view()),    
    url(r'^update-password/$', views.update_password),

    url(r'^user/(?P<username>[^\.]+)/about$', views.about),        

    url(r'^user/(?P<username>[^\.]+)/subscribe', views.subscribe),
    url(r'^user/(?P<username>[^\.]+)/unsubscribe', views.unsubscribe),    
]

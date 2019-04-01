from django.conf.urls import url
from basictempapp import views

# for template tagging ou have to do
app_name = 'basictempapp'

urlpatterns = [
    url(r'^relurltemp/$',views.relurltemp,name = 'relurltemp'),
    url(r'^other/$',views.other,name = 'other'),

]

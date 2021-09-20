
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post/$', views.PostView.as_view(), name='get all view'),
]

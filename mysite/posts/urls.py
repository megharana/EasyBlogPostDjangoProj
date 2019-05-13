from . import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('blogs/', views.index, name="blog-posts"),
    url('^details/(?P<id>\d+)/$', views.details, name='blog-details')
]

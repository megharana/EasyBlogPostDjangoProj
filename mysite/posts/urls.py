from . import views
from django.urls import path, include

urlpatterns = [path('blogs/', views.index, name="blog-posts")]

from django.urls import path
from blog.views import showBlog

urlpatterns =[
    path('', showBlog, name='showBlog')
]
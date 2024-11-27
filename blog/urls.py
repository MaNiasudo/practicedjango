from django.urls import path
from blog.views import *

urlpatterns = [
    path("blogs/",blogs,name="blogs"),
    path("blogsingle/",blogsingle,name="blogsingle")
]
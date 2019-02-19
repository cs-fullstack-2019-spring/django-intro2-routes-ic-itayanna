
# importhing the files to put response on the paths

from django.urls import path
from . import views


# linking the paths to the response pages

urlpatterns = [
    path('', views.index, name='index'),
    path('mycity/', views.mycity, name='mycity'),
    path('myeats/', views.myeats, name='myeats')
]

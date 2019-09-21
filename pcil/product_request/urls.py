
from django.urls import include,path,re_path
from . import views


app_name = 'product_request'

urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    # path('', views.home, name='form_details'),# if we dont navigate anywhere from music app(music homepage which displays all albums)
    # re_path(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),# to navigate to all the albums(one by one click on albums, hence we need ids coz albums displayed are nothing but ids)
    path('', views.index, name='index'),
    re_path(r'^(?P<product_id>[0-9]+)/$', views.details, name='details'),# to navigate to all the albums(one by one click on albums, hence we need ids coz albums displayed are nothing but ids)
	re_path(r'^(?P<product_id>[0-9]+)/favorite', views.favorite, name='favorite')
]

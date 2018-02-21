from django.conf.urls import url
from herberg import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^post$', views.post_image, name="post"),
    url(r'^(?P<page>[\d]+)$', views.home, name="images-page"),
    url(r'^delete/(?P<pk>[\d]+)$', views.delete_image, name="delete-image")

]
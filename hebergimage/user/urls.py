from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'},
        name="login"),

    url(r'^logout/$', auth_views.logout_then_login,
        name="logout"),
    url(r'registration', views.registration, name="registration")

]
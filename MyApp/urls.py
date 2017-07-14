"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Credit import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html', 'redirect_authenticated_user': True},
        name='login'),
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'},  name='logout'),
    url(r'^card/detail/(?P<pk>\d+)/$', views.CardDetailView.as_view(), name='card-detail'),
    url(r'^card/list/$', views.CardListView.as_view(), name='card-list'),
    url(r'^card/update/(?P<pk>\d+)/$', views.CardUpdateView.as_view(), name='card-update'),
    url(r'^card/delete/(?P<pk>\d+)/$', views.CardDeleteView.as_view(), name='card-delete'),
    url(r'^card/create/$', views.CardCreateView.as_view(), name='card-create'),
]

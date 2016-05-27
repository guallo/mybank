'''
Created on May 25, 2016

@author: eacuesta
'''

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard_view, name='dashboard-view'),
    url(r'^profile$', views.profile_view, name='profile-view'),
    url(r'^accounts$', views.accounts_view, name='accounts-view'),
    url(r'^saving_boxes$', views.saving_boxes_view, name='saving-boxes-view'),
    url(r'^moves$', views.moves_view, name='moves-view'),
    url(r'^logout$', auth_views.logout, {'next_page': 'login-view', 'redirect_field_name': None}, name='logout-view'),
    url(r'^(?:login)?$', auth_views.login, {'template_name': 'presentation/login.html'}, name='login-view'),
]
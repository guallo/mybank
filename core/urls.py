'''
Created on May 9, 2016

@author: eacuesta
'''

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'accounts', views.AccountViewSet, base_name='account')
router.register(r'currency_types', views.CurrencyTypeViewSet)
router.register(r'saving_boxes', views.SavingBoxViewSet, base_name='savingbox')
router.register(r'causes', views.CauseViewSet)
router.register(r'moves', views.MoveViewSet, base_name='move')

urlpatterns = [
    url(r'^', include(router.urls)),
]
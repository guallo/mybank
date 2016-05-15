from django.contrib.auth import models as auth_models
from rest_framework import viewsets as rest_viewsets
from rest_framework import permissions as rest_permissions

from . import models
from . import serializers
from . import permissions

# Create your views here.


class UserViewSet(rest_viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AuthenticatedUserCanChangePassword, )
    
    def get_serializer_class(self):
        if not self.request.user.is_staff and self.request.method == 'PUT':
            return serializers.ChangeUserPasswordSerializer
        return super(self.__class__, self).get_serializer_class()
    
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return auth_models.User.objects.none()
        if self.request.user.is_staff:
            return auth_models.User.objects.all()
        return auth_models.User.objects.filter(pk=self.request.user.pk)


class AccountViewSet(rest_viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer
    permission_classes = (permissions.IsAdminUserOrAuthenticated, )
    
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return models.Account.objects.none()
        if self.request.user.is_staff:
            return models.Account.objects.all()
        return models.Account.objects.filter(user=self.request.user)


class CurrencyTypeViewSet(rest_viewsets.ModelViewSet):
    queryset = models.CurrencyType.objects.all()
    serializer_class = serializers.CurrencyTypeSerializer
    permission_classes = (rest_permissions.IsAdminUser, )


class SavingBoxViewSet(rest_viewsets.ModelViewSet):
    serializer_class = serializers.SavingBoxSerializer
    permission_classes = (permissions.IsAdminUserOrAuthenticated, )
    
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return models.SavingBox.objects.none()
        if self.request.user.is_staff:
            return models.SavingBox.objects.all()
        return models.SavingBox.objects.filter(account__user=self.request.user)


class CauseViewSet(rest_viewsets.ModelViewSet):
    queryset = models.Cause.objects.all()
    serializer_class = serializers.CauseSerializer
    permission_classes = (permissions.IsAdminUserOrAuthenticated, )


class MoveViewSet(rest_viewsets.ModelViewSet):
    serializer_class = serializers.MoveSerializer
    permission_classes = (rest_permissions.IsAuthenticated, )
    
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return models.Move.objects.none()
        if self.request.user.is_staff:
            return models.Move.objects.all()
        return models.Move.objects.filter(saving_box__account__user=self.request.user)
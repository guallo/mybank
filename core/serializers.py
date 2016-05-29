'''
Created on May 8, 2016

@author: eacuesta
'''

from django.contrib.auth import models as auth_models
from rest_framework import serializers as rest_serializers

from . import models


class UserSerializer(rest_serializers.HyperlinkedModelSerializer):
    account_set = rest_serializers.HyperlinkedRelatedField(view_name='account-detail', 
                                                           many=True, 
                                                           read_only=True)
    
    class Meta:
        model = auth_models.User
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 
                  'email', 'is_staff', 'is_active', 'account_set', )


class ChangeUserPasswordSerializer(rest_serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = auth_models.User
        fields = ('password', )


class AccountSerializer(rest_serializers.HyperlinkedModelSerializer):
    savingbox_set = rest_serializers.HyperlinkedRelatedField(view_name='savingbox-detail', 
                                                            many=True, 
                                                            read_only=True)
    
    class Meta:
        model = models.Account
        fields = ('url', 'uuid', 'user', 'savingbox_set', )


class CurrencyTypeSerializer(rest_serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CurrencyType
        fields = ('url', 'name', )


class SavingBoxSerializer(rest_serializers.HyperlinkedModelSerializer):
    currency_type_name = rest_serializers.ReadOnlyField(source='currency_type.name')
    move_set = rest_serializers.HyperlinkedRelatedField(view_name='move-detail', 
                                                        many=True, 
                                                        read_only=True)
    
    class Meta:
        model = models.SavingBox
        fields = ('url', 'currency_type', 'currency_type_name', 'account', 
                  'move_set', 'balance', )


class CauseSerializer(rest_serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cause
        fields = ('url', 'name', 'description', )


class MoveSerializer(rest_serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Move
        fields = ('url', 'typee', 'description', 'date', 'cause', 
                  'saving_box', 'amount', )
    
    def get_fields(self, *args, **kwargs):
        fields = super(self.__class__, self).get_fields(*args, **kwargs)
        fields['saving_box'].queryset = fields['saving_box'].queryset.filter(
                             account__user=self.context['view'].request.user)
        return fields
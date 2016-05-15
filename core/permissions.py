'''
Created on May 12, 2016

@author: eacuesta
'''

from rest_framework import permissions


class IsAdminUserOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        return request.method in permissions.SAFE_METHODS or request.user.is_staff


class AuthenticatedUserCanChangePassword(IsAdminUserOrAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_authenticated() and request.method == 'PUT':
            return True
        return super(self.__class__, self).has_permission(request, view)
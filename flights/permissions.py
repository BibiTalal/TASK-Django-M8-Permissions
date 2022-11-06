from rest_framework.permissions import BasePermission
from datetime import timedelta,date
from django.utils import timezone

class IsBookingOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user


class IsMoreThan3Days(BasePermission):
    message = "Too close to flight date"

    def has_object_permission(self, request, view, obj):
        return (obj.date - date.today()).days> 3
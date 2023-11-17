from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

def check_permission(permission_name, request):
    for group in request.user.groups.all():
        if group.permissions.filter(codename = permission_name):
            return True
    return False

def object_is_exist(pk, model):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise ValidationError({'Error' : 'This object not found'})
    
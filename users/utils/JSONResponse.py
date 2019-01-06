from django.http import HttpResponse
from django.core import serializers


def jsonResponse(obj):
    data = serializers.serialize('json', obj)
    return HttpResponse(data, content_type="application/json")

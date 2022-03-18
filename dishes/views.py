from dishes.models import Dish
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpRequest
from json import loads


def list_of_pizzas(request):
    queryset = Dish.objects.all()
    data = serializers.serialize("json", queryset=queryset, cls=DjangoJSONEncoder)
    return JsonResponse(data=loads(data), safe=False)

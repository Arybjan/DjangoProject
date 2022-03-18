from dishes.models import Dish
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpRequest
from json import loads


def list_of_pizzas(request):
    queryset = Dish.objects.all()
    data = serializers.serialize("json", queryset=queryset, cls=DjangoJSONEncoder)
    return JsonResponse(data=loads(data), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def create_pizza(request):
    data = loads(request.body.decode("UTF-8"))
    title = data.get("title")

    instance = Dish.objects.create(title=title)
    response = serializers.serialize("json", [instance])
    return JsonResponse(data=loads(response), safe=False)

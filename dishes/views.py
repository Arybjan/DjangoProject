from dishes.models import Dish, SizeType, DishSize
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
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


def list_of_dish_size_type(request):
    queryset = SizeType.objects.all()
    data = serializers.serialize("json", queryset=queryset, cls=DjangoJSONEncoder)
    return JsonResponse(data=loads(data), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def create_pizza_size_type(request):
    data = loads(request.body.decode("UTF-8"))
    name = data.get("name")

    instance = SizeType.objects.create(name=name)
    response = serializers.serialize("json", [instance])
    return JsonResponse(data=loads(response), safe=False)


def list_of_dish_size(request):
    queryset = DishSize.objects.all()
    data = serializers.serialize("json", queryset=queryset, cls=DjangoJSONEncoder)
    return JsonResponse(data=loads(data), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def create_dish_size(request):
    data = loads(request.body.decode("UTF-8"))
    size_value = data.get("size_value")
    weight = data.get("weight")
    price = data.get("price")
    dish_id = data.get("dish_id")
    size_type_id = data.get("size_type_id")

    instance = DishSize.objects.create(size_value=size_value, weight=weight,
                                       price=price, dish_id=dish_id,
                                       size_type_id=size_type_id)
    response = serializers.serialize("json", [instance])
    return JsonResponse(data=loads(response), safe=False)


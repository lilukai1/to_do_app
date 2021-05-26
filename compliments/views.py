from django.views import View
import json
from .models import Compliments
from django.utils.decorators import method_decorator

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ComplimentSerializer


@method_decorator(csrf_exempt, name='dispatch')
def compliment_list(request):
    """
    List all code compliments, or create a new compliment.
    """
    if request.method == 'GET':
        compliments = Compliments.objects.all()
        serializer = ComplimentSerializer(compliments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComplimentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
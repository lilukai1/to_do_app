from json import encoder
from django.views import View
import json
from .models import Compliments
from django.utils.decorators import method_decorator

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ComplimentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# @api_view(['GET', 'POST'])
def compliment_list(request, format=None):
    """
    List all code compliments, or create a new compliment.
    """
    if request.method == 'GET':
        compliments = Compliments.objects.all()
        anytime=[]
        morning=[]
        afternoon=[]
        evening=[]

        for row in compliments:
            if row.category =='anytime':
                anytime.append(f"{row.compliment} - {row.person} {row.created.strftime('%b,%d,%y')}")
            # serializer = ComplimentSerializer(compliments, many=True)
        time_key = {'anytime':anytime, 'morning':morning, 'afternoon':afternoon, 'evening':evening }
        serializer = json.dumps(time_key, indent=3, ensure_ascii=False)
        return JsonResponse(serializer, safe=False,)

    elif request.method == 'POST':
        serializer = ComplimentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
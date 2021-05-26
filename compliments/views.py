from django.views import View
from django.http import JsonResponse
import json
from .models import Compliments
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class ComplimentView(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        c_person = data.get('person')
        c_compliment = data.get('compliment')
        c_category = data.get('category')

        compliment_data = {
            'person': c_person,
            'compliment': c_compliment,
            'category': c_category,
        }

        Compliments.objects.create(**compliment_data)

        data = {
            "message": "New compliment added!"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items = Compliments.objects.all()
        items_data = []
        for item in items:
            items_data.append({
                'person': item.person,
                'compliment': item.compliment,
                'category': item.category,
                # 'time':item.created,
            })

        data = {
            'items': items_data,
        }

        return JsonResponse(data)
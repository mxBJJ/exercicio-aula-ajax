from django.shortcuts import render
import json
from django.http import HttpResponse
from random import randint

# Create your views here.


def home(request):
    return render(request, 'myApp/index.html')

def draw(request):
    if request.method == 'POST':
        totalNumbers = request.POST['totalNumbers']
        limit = request.POST['limit']
        arrayRandom = []

        for i in range(int(totalNumbers)):
            number = randint(0,int(limit))
            arrayRandom.append(number)

        data = {
            'drawed_numbers': arrayRandom,
        }

        myDraw = json.dumps(data)
        return HttpResponse(myDraw, content_type='application/json')
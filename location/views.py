from django.shortcuts import render, HttpResponse


# Create your views here.
def map(request):
    return render(request, 'location/map.template.html')
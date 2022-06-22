from django.shortcuts import render

# Create your views here.
def my_webpage(request):
    return render(request, 'page1.html',{'name': 'gareth'})


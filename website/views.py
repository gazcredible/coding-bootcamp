from django.shortcuts import render

# Create your views here.
def page_1(request):
    return render(request, 'website/page1.html',{'name': 'gareth'})

def page_2(request):
    return render(request, 'website/page2.html',{'name': 'gareth'})

from django.urls import path
import website.views

urlpatterns = [    
    path('', website.views.my_webpage)
]

from django.urls import path
import website.views

urlpatterns = [    
    path('page-1', website.views.page_1, name='website-page-1'),
    path('page-2', website.views.page_2, name='website-page-2')
]

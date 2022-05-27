from . import views
from django.urls import path



urlpatterns = [
    path('', views.General),# если поле чистое в ковычках то на первой странице будет указанная штмл
    path('gvardeitsev',views.Gvardeitsev),
    path('denis',views.Denis),
    path('tanya',views.Tanya),
]
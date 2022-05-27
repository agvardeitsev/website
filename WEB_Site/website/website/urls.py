
from django.contrib import admin
from django.urls import path, include
from webfilling.views import General
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webfilling.urls')),# если поле чистое в ковычках то на первой странице будет указанная штмл
]

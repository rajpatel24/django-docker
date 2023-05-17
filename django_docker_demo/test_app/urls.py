from django.urls import path
from .views import sample_fun

urlpatterns = [
    path('', sample_fun, name='sample_function')
]

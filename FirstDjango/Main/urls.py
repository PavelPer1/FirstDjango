from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_add, name='items'),
    path('<url>', views.basic)
]

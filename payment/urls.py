from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('success/', views.payment_completed, name="payment_completed"),
    path('fail/', views.payment_canceled, name='payment_canceled'),
]
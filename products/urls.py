from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products, name='products'),
    url(r'^order/$', views.order, name='order'),
]
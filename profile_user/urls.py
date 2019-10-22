from django.urls import path
from profile_user import views

urlpatterns = [
				path('', views.index, name='index'),
				path('create_data/', views.create_data, name='create_data'),
			  ]
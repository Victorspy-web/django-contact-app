from django.urls import path
from .views import contacts, create_contact,contact_info, contact_update, contact_delete

urlpatterns = [
	path('', contacts, name='contacts'),
	path('create/', create_contact, name='create'),
	path('info/<str:pk>/', contact_info, name='info'),
	path('update/<str:pk>/', contact_update, name='update'),
path('delete/<str:pk>/', contact_delete, name='delete'),
]
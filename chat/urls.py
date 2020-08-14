from django.urls import path

from .views import message_list

urlpatterns = [
	path('api/messages/<int:sender>/<int:receiver>/', message_list),
]

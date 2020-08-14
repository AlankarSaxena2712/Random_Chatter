from account import views
from django.urls import path

urlpatterns = [
	path('user/', views.UserView.as_view()),
	path('user/<int:pk>/', views.UserChanges.as_view())
]

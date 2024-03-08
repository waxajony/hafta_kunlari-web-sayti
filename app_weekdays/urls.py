from django.urls import path

from .views import weekend, uz_week, en_week, ru_week

urlpatterns = [
	path('weekdays/', weekend),
	path('uz/', uz_week),
	path('en/', en_week),
	path('ru/', ru_week),
]
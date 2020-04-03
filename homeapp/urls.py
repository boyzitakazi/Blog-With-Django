from django.urls import path
from .views import TemplatePage


urlpatterns = [
	# url dari views untuk ditampilkan pada browser (tampilan home)
	path('', TemplatePage.as_view(), name='home'),
]
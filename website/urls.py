from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # url dari user_profile untuk ditampilkan pada browser (tampilan untuk blog)
    path('', include('user_profile.urls')),

    # url dari homeapp untuk ditampilkan pada browser (tampilan home)
    path('', include('homeapp.urls')),

    # url untuk tampilan admin
    path('admin/', admin.site.urls),

]

from django.contrib import admin
from django.urls import path
from websocket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('command/', views.command),
]
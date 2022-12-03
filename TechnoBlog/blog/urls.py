from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('content/<str:pk>/', views.content, name="content"),
    path('contactus/',views.contact,name="contact")
]
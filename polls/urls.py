from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("demographics/", views.demographics, name="demographics"),
    path('instructions/', views.instructions, name='instructions'),
    path('main/', views.main, name='main'),
    path('main/end/<str:num>', views.end, name='end'),
    path('end/', views.thank, name='thank'),
    path('<str:query>/results/', views.handle, name='handle'),
]

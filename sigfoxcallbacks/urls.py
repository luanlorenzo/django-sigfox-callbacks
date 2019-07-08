from django.urls import path

from . import views

urlpatterns = [
  path('', views.callbacks_view, name='index'),
  path('sigfox/', views.sigfox_callback, name='sigfoxcallback')
]
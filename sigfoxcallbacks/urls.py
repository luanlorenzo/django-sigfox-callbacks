from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sigfoxcallbacks import views

urlpatterns = [
  path('', views.api_root, name='index'),
  path('callback/', views.CallbackList.as_view(), name='callback-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
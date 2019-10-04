from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from callbacks import views

urlpatterns = [
    path('', views.api_root, name='index'),
    path('callback/', views.get_post_callbacks, name='get_post_callbacks')
]

urlpatterns = format_suffix_patterns(urlpatterns)

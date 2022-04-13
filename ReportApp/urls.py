from . import views
from django.urls import path


urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('report', views.report, name='report'),
    path('city_commission', views.city_commission, name='city_commission'),
    path('error', views.error, name='error'),
]
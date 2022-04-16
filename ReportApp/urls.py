from .views import upload_view, report_view, city_commission_view, error_upload_view, error_report_view
from django.urls import path


urlpatterns = [
    path('upload', upload_view, name='upload'),
    path('report', report_view, name='report'),
    path('city_commission', city_commission_view, name='city_commission'),
    path('error_upload', error_upload_view, name='error_upload'),
    path('error_report', error_report_view, name='error_report'),
]
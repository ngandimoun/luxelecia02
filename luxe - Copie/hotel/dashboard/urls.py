from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'  # Add an app_name to specify the app namespace
urlpatterns = [
    path('create/', views.create_dashboard_item, name='create_dashboard_item'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download/<uuid:item_id>/', views.download_dashboard, name='download_dashboard'),  # Update the URL pattern to handle UUIDs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


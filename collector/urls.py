from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('c/<hostname>/<ip>/', views.get_command),
    path('f/<hostname>/<ip>/<data_type>/<data_hash>/<path:data_content>/', views.data_collection),
    path('<hostname>/<ip>/<data_type>/<path:data_content>/', views.data_collection),
    path('', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<hostname>/<ip>/<data_type>/<data>/<file_type>', views.index),
    path('<hostname>/<ip>/<data_type>/<data>', views.index),
    path('<hostname>/<ip>/<data_type>', views.index),
    path('<hostname>/<ip>/', views.index),
    path('<hostname>/', views.index),
    path('', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from app1 import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from app1.tests import uid
# router = DefaultRouter()
# router.register(r'permissions', views.PermissionViewSet)
# a = uid()
from django.views.generic import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/',include('app1.urls')),
    path('',views.index),
    path('<path:dummy>', TemplateView.as_view(template_name='index.html')),
    
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
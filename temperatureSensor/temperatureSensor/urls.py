from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView

urlpatterns = [
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
 path('account', TemplateView.as_view(template_name='index.html')),
]

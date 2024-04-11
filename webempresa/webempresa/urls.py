from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del Core
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    # Paths del Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django. conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

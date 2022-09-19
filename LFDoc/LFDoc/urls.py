from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('Examples/', include('Examples.urls')),
    path('polls/', include('polls.urls')),
    path('formsexample/', include('formsexample.urls')),

    path('modelrelationship/', include('ModelRelationship.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
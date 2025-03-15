from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('careers/', include('careers.urls')),
    path('mentors/', include('mentors.urls')),
    path('community/', include('community.urls')),
    path('events/', include('events.urls')),
    path('exams/', include('exams.urls')),
    path('blogs/', include('blogs.urls')),
    path('api/', include('careers.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
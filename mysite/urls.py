from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    url(r'', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

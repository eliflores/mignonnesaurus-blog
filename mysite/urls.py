from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

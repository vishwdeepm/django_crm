from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import IndexView, SignupView
from django.contrib.auth.views import ( 
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'), 
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
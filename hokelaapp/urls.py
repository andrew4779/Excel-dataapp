from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from hokelaapp import views
urlpatterns = [
    # path('',views.excel_upload, name='excel_upload'),
    path('', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    # path('profile/', views.profile, name='profile'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
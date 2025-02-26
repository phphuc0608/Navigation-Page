from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.user_view, name='user'),
    path('login/', views.login_view, name='login'),
    path('manage/', views.manage_view, name='manage'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:page_id>/', views.edit_view, name='edit'),
    path('delete/<int:page_id>/', views.delete_view, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update',views.user_update,name="update"),
    path('vendor-register/', views.vendor_register, name='vendor_register'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('travels/<int:vendor_id>/', views.travels_detail, name='travels_detail'),

]
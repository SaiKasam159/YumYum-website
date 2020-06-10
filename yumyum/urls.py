"""yumyum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fooddiary import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('current/', views.currentmeal, name='currentmeal'),
    path('', views.home, name='home'),
    path('create', views.createmeal, name='createmeal'),
    path('viewmeal/<int:meal_pk>', views.viewmeal, name='viewmeal'),
    path('viewmeal/<int:meal_pk>/delete', views.deletemeal, name='deletemeal'),
    path('createactivity', views.createactivity, name='createactivity'),
    path('physicalactivity', views.physicalactivity, name='physicalactivity'),
    path('viewactivity/<int:activity_pk>', views.viewactivity, name='viewactivity'),
    path('viewactivity/<int:activity_pk>/delete', views.deleteactivity, name='deleteactivity'),
    path('weekmeal', views.weekmeal, name='weekmeal'),
    path('favourite', views.favourite, name='favourite'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
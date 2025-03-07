
from django.contrib import admin
from django.urls import path
from Authentication import views


urlpatterns=[
    path('admin/',admin.site.urls),
    path('register/',views.RegisterView,name='register'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout')
]
  
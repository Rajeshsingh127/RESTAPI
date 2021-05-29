
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('details.urls')),
    path('token/',TokenObtainPairView.as_view(),name = "token_obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refesh"),

]

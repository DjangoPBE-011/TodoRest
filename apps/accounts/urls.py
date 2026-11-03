from django.urls import include, path
from rest_framework import urls

from apps.accounts.views import (
# ExampleView, 
# Example2View, 
   RegisterUser,
   Login,
   Logout,
)


urlpatterns = [
   # urls.path('example/', ExampleView.as_view(), name='example'),
   # urls.path('example2/<int:pk>/', Example2View.as_view(), name='example2'),
   
   urls.path('register/', RegisterUser.as_view(), name='register'),
   urls.path('login/', Login.as_view(), name='login'),
   urls.path('logout/', Logout.as_view(), name='logout'),
]
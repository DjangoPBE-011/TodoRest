from django.urls import include, path


from apps.accounts.views import (
# ExampleView, 
# Example2View, 

   # LoginView,
   # LogoutView,
   
   RegisterUser,
   
   # Login,
   # Logout,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('register/', RegisterUser.as_view(), name='register'),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   # path('login/', LoginView.as_view(), name='login'),
   # path('logout/', LogoutView.as_view(), name='logout'),
   
   # urls.path('login/', Login.as_view(), name='login'),
   # urls.path('logout/', Logout.as_view(), name='logout'),
   
   # urls.path('example/', ExampleView.as_view(), name='example'),
   # urls.path('example2/<int:pk>/', Example2View.as_view(), name='example2'),
]
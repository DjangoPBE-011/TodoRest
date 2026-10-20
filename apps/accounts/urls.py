from django.urls import include, path

from apps.accounts.views import ExampleView, Example2View



urlpatterns = [
   path('example/', ExampleView.as_view(), name='example'),
   path('example2/<int:pk>/', Example2View.as_view(), name='example2'),
]
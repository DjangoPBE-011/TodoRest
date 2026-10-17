from django.urls import include, path

from apps.accounts.views import ExampleView



urlpatterns = [
   path('example/', ExampleView.as_view(), name='example'),
]
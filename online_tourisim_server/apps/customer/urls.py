from django.urls import path
from apps.customer.views.customer_views import FirstApiView

urlpatterns =[
    path('',FirstApiView.as_view(),name='first-api-view')
]
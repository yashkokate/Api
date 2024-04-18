from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientView, ProjectView

from django.urls import path
from .views import ClientView, ProjectView

urlpatterns = [
    path('clients/', ClientView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientView.as_view(), name='client-detail'),
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project-detail'),
]

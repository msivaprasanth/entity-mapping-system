from django.urls import path   # type: ignore
from .views import CertificationListCreateAPIView,CertificationDetailAPIView

urlpatterns = [
    path('',CertificationListCreateAPIView.as_view(),name='certification-list-create'),
    path('<int:pk>/',CertificationDetailAPIView.as_view(),name='certification-detail'),
]
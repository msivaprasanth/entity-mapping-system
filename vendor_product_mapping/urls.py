from django.urls import path  # type: ignore
from .views import VendorProductMappingListCreateAPIView,VendorProductMappingDetailAPIView

urlpatterns = [
    path('',VendorProductMappingListCreateAPIView.as_view(),name='vendor-product-mapping-list-create'),
    path('<int:pk>/',VendorProductMappingDetailAPIView.as_view(),name='vendor-product-mapping-detail'),
]
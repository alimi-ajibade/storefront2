from cgitb import lookup
from email.mime import base
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product'
)

products_router.register(
    'reviews', views.ReviewViewset, basename='product-reviews'
)

urlpatterns = router.urls + products_router.urls


# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetails.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path(
#         'collections/<int:pk>/',
#          views.CollectionDetail.as_view(),
#          name='collection-detail',
#     ),
# ]

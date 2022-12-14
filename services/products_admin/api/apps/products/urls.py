from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet


router = DefaultRouter(trailing_slash=False)
router.register("", ProductViewSet, "products")

urlpatterns = [

] + router.urls

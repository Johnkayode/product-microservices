from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


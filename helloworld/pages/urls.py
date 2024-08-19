from django.urls import path
from .views import HomePageView, AboutPageView, ProductCreateView, ProductShowView
from .views import ProductIndexView, ProductCreateView
from .views import ContactPageView

# Define las rutas (URLs) para la aplicación
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),        # Ruta para la página principal
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show')
]

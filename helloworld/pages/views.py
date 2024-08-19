from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Daniel Cruz",
        })
        return context

from django.shortcuts import render
from django.views import View

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV PRICE: 399$", "price": 399},
        {"id": "2", "name": "iPhone", "description": "Best iPhone PRICE: 999$", "price": 999},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast PRICE: 49$", "price": 49},
        {"id": "4", "name": "Glasses", "description": "Best Glasses PRICE: 99$", "price": 99},
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {
            "title": "Products - Online Store",
            "subtitle": "List of products",
            "products": Product.products
        }
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}

        try:
            product = Product.products[int(id) - 1]
        except (IndexError, ValueError):
            return redirect('home')
        
        viewData["title"] = f"{product['name']} - Online Store"
        viewData["subtitle"] = f"{product['name']} - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)

from django import forms
from django.shortcuts import render, redirect
from django.views import View

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.DecimalField(min_value=0.01, max_digits=10, decimal_places=2)

class ProductCreateView(View):
    template_name = 'products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., save to the database)
            # For demonstration, we'll assume you want to redirect to a success page
            return redirect('success_page')  # Replace 'success_page' with your actual URL name or path
        else:
            if form.cleaned_data.get('price') == 0:
                form.add_error('price', 'El precio debe ser mayor a 0')
            viewData = {
                "title": "Create product",
                "form": form
            }
            return render(request, self.template_name, viewData)
        
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context.update({
            "title": "Contact us",
            "subtitle": "our contact information",
            "description": "email: dacruzj@eafit.edu.co number: 123456789 address: Medellin",
            "author": "Developed by: Daniel Cruz",
        })
        return context



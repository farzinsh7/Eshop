import itertools

from django.shortcuts import render
from django.views.generic import ListView

from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductsGallery
from django.http import Http404
from eshop_products_category.models import ProductCategory


# Create your views here.

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('دسته بندی مورد نظر یافت نشد')
        return Product.objects.get_product_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})

    product = Product.objects.get_by_id(selected_product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    product.visit_count += 1
    product.save()

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    grouped_related_products = list(my_grouper(3, related_products))

    galleries = ProductsGallery.objects.filter(product_id=selected_product_id)
    grouped_galleries = list(my_grouper(3, galleries))
    context = {
        'product': product,
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form
    }
    return render(request, 'products/product_detail.html', context)


class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 100

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)

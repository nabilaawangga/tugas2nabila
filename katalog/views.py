from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_wishlist = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Nabila Zahra Putri Awangga',
    'studentid': '2106703840',
    }
    return render(request, "katalog.html", context)
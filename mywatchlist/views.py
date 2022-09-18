from django.shortcuts import render
from mywatchlist.models import MywatchlistItem

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchwishlist = MywatchlistItem.objects.all()
    context = {
    'list_barang': data_watchwishlist,
    'nama': 'Nabila Zahra Putri Awangga',
    'studentid': '2106703840',
    }
    return render(request, "mywatchlist.html", context)

from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchwishlist = MywatchlistItem.objects.all()
    context = {
    'list_barang': data_watchwishlist,
    'nama': 'Nabila Zahra Putri Awangga',
    'studentid': '2106703840',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

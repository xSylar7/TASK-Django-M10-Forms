from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from stores import models


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)

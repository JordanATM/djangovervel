from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"


class ItemCreateView(CreateView):
    model = Item
    template_name = "items/item_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("item-list")


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "items/item_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("item-list")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "items/item_confirm_delete.html"
    success_url = reverse_lazy("item-list")

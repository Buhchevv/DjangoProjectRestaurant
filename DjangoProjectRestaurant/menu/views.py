from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views import generic as view
from django.shortcuts import render

from DjangoProjectRestaurant.menu.forms import MenuItemForm
from DjangoProjectRestaurant.menu.models import MenuItem

UserModel = get_user_model()


def menu_page(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items': menu_items
    }
    return render(request, 'menu/menu-page.html', context)


class CreateMenuItemView(LoginRequiredMixin, UserPassesTestMixin, view.CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/create_menu_item.html'
    success_url = reverse_lazy('menu page')

    def test_func(self):
        return self.request.user.is_staff


class MenuItemView(view.DetailView):
    model = MenuItem
    template_name = 'menu/menu_item_details.html'
    context_object_name = 'menu_item'


class EditMenuView(LoginRequiredMixin, UserPassesTestMixin, view.UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/edit_menu_item.html'
    success_url = reverse_lazy('menu page')

    def test_func(self):
        return self.request.user.is_staff


class DeleteMenuView(LoginRequiredMixin, UserPassesTestMixin, view.DeleteView):
    model = MenuItem
    template_name = 'menu/delete_menu_item.html'
    success_url = reverse_lazy('menu page')

    def test_func(self):
        return self.request.user.is_staff

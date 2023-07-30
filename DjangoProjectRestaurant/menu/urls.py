from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from DjangoProjectRestaurant.menu.views import menu_page, CreateMenuItemView, MenuItemView, EditMenuView, DeleteMenuView

urlpatterns = [
                  path('menu/', menu_page, name='menu page'),

                  path('create-menu-item/', CreateMenuItemView.as_view(), name='crete menu item'),

                  path('menu_item/<int:pk>/', include([
                      path('', MenuItemView.as_view(), name='details menu item'),
                      path('edit/', EditMenuView.as_view(), name='edit menu item'),
                      path('delete/', DeleteMenuView.as_view(), name='delete menu item'),
                  ])),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

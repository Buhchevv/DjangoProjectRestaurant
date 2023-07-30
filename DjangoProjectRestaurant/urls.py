from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('DjangoProjectRestaurant.core.urls')),
                  path('users/', include('DjangoProjectRestaurant.users.urls')),
                  path('review/', include('DjangoProjectRestaurant.review.urls')),
                  path('reservations/', include('DjangoProjectRestaurant.reservations.urls')),
                  path('contact/', include('DjangoProjectRestaurant.contact.urls')),
                  path('menu/', include('DjangoProjectRestaurant.menu.urls')),
                  path('subscribers/', include('DjangoProjectRestaurant.subscribers.urls')),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'DjangoProjectRestaurant.core.views.handler404'
handler403 = 'DjangoProjectRestaurant.core.views.handler403'

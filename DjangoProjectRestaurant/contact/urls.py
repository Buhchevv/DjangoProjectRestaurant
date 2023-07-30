from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from DjangoProjectRestaurant.contact.views import ContactView, ContactSuccessView

urlpatterns = [
                  path('contact/', include([
                      path('', ContactView.as_view(), name='contact page'),
                      path('success/', ContactSuccessView.as_view(), name='contact success page'),
                  ])),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

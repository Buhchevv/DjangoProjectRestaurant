from django.urls import path

from DjangoProjectRestaurant.subscribers.views import subscribe_newsletter, subscribers_list, subscription_success

urlpatterns = [
                  path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
                  path('subscribers/', subscribers_list, name='subscribers_list'),
                  path('success/', subscription_success, name='success_page'),

              ]
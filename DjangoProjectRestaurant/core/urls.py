from django.urls import path

from DjangoProjectRestaurant.core.views import home_page, about_page, specials_page, events_page, chefs_page, \
    gallery_page

urlpatterns = [
    path('', home_page, name='home page'),
    path('about/', about_page, name='about page'),
    path('specials/', specials_page, name='specials page'),
    path('events/', events_page, name='events page'),
    path('chefs/', chefs_page, name='chefs page'),
    path('gallery/', gallery_page, name='gallery page'),

]

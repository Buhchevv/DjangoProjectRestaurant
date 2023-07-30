from django.urls import path

from DjangoProjectRestaurant.review.views import CreateReviewView, review_page

urlpatterns = [

    path('reviews/', review_page, name='review page'),

    path('create-review/', CreateReviewView.as_view(), name='create review'),
]

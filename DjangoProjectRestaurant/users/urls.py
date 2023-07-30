from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from DjangoProjectRestaurant.users.views import \
    UserRegistrationView, UserLoginView, UserLogOutView, \
    ProfileDetailView, EditProfileView, DeleteProfileView, user_reviews_page, user_reservations_view

urlpatterns = [

    path('sign-up/', UserRegistrationView.as_view(), name='register'),
    path('sign-in/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),

    path('user-reviews-page/', user_reviews_page, name='user reviews page'),
    path('user-reservations/', user_reservations_view, name='user reservations'),

    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='profile details'),
        path('edit/', EditProfileView.as_view(), name='edit profile'),
        path('delete/', DeleteProfileView.as_view(), name='delete profile'),
    ])),
]

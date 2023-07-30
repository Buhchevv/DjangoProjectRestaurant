from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from DjangoProjectRestaurant.review.forms import ReviewForm
from DjangoProjectRestaurant.review.models import Review


def review_page(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews-page.html', context)


class CreateReviewView(LoginRequiredMixin, view.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create_review.html'
    success_url = reverse_lazy('review page')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.save()
        return super().form_valid(form)

from django.shortcuts import render, redirect

from DjangoProjectRestaurant.subscribers.forms import SubscribeForm
from DjangoProjectRestaurant.subscribers.models import Subscriber


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SubscribeForm()

    return render(request, 'base.html', {'form': form})


def subscribers_list(request):
    subscribers = Subscriber.objects.all()
    context = {
        'subscribers': subscribers
    }
    return render(request, 'core/subscribers_list.html', context)


def subscription_success(request):
    return render(request, 'core/success_page.html')

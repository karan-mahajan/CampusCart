from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FreeItemForm
from .models import FreeStuffItem
from django.contrib import messages
from notifications.signals import notify
from django.contrib.auth import get_user_model

@login_required
def index(request):
    items = FreeStuffItem.objects.all()
    return render(request, 'freestuff/home.html', {
        'items': items,
        'title': 'Free Stuff'
    })


@login_required
def upload_item(request):
    if request.method == 'POST':
        form = FreeItemForm(request.POST, request.FILES)
        if form.is_valid():
            free_item = form.save(commit=False)
            free_item.seller = request.user
            free_item.save()
            sender = get_user_model().objects.get(username=request.user)
            receiver = get_user_model().objects.exclude(username=request.user)
            description = f'<b>{free_item.title}</b> (Free {free_item.category} Item). Click <a href="/free/item-detail/{free_item.id}">here</a> to view.'
            notify.send(sender, recipient=receiver, verb='Upload', description=description)
            return redirect('freestuff:home')
    else:
        form = FreeItemForm()
    return render(request, 'freestuff/upload_item.html', {
        'form': form,
        'title': 'Upload your Item'
    })


@login_required
def item_detail(request, itemid):
    current_item = get_object_or_404(FreeStuffItem, pk=itemid)
    return render(request, 'freestuff/item_detail.html', {
        'title': current_item.title,
        'item': current_item,
    })


@login_required
def edit_item(request, itemid):
    my_item = get_object_or_404(FreeStuffItem, pk=itemid)
    if my_item.seller != request.user:
        messages.success(request, "You don't have the access to the Item", extra_tags='danger')
        return redirect('accounts:user-listing')
    if request.method == 'POST':
        if 'action' in request.POST:
            form = FreeItemForm(request.POST, request.FILES, instance=my_item)
            if form.is_valid():
                book = form.save(commit=False)
                book.save()
                return redirect('accounts:user-listing')
        else:
            my_item.delete()
            messages.success(request, "Your Item has been deleted", extra_tags='danger')
            return redirect('accounts:user-listing')
    else:
        form = FreeItemForm(instance=my_item)
    return render(request, 'freestuff/edit_item.html', {
        'form': form,
        'title': 'Edit Item'
    })

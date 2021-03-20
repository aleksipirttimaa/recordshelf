from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Artist, Possession, Record


def index(request):
    return redirect(records)



def records(request):
    artists = Artist.objects.order_by('name')
    records = Record.objects.order_by('name')
    return render(request, 'records/records.html', {
        'artists': artists,
        'records': records,
    }, content_type='text/html')



@login_required(login_url='/accounts/login')
def shelf(request):
    possessions = Possession.objects.filter(owner=request.user)
    return render(request, 'records/shelf.html', {
        'possessions': possessions,
    }, content_type='text/html')



@login_required(login_url='/accounts/login')
def possess(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    existing = Possession.objects \
        .filter(owner=request.user) \
        .filter(record=record)
    if not existing:
        new = Possession(record=record, owner=request.user)
        new.save()
    return redirect(records)



@login_required(login_url='/accounts/login')
def exorcise(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    existing = Possession.objects \
        .filter(owner=request.user) \
        .filter(record=record)
    if existing:
        existing.delete()
        if request.GET.get('next-shelf', False):
            return redirect(shelf)
        else:
            return redirect(records)
    else:
        raise Http404("You didn't possess this record")



def logout_and_redirect(request):
    logout(request)
    return redirect(records)

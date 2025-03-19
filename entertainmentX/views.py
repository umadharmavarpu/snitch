from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def movies(request):
    return render(request, 'movies.html')

def events(request):
    return render(request, 'events.html')

def sports(request):
    return render(request, 'sports.html')

def movie_booking(request):
    return render(request, 'mbooking.html')

def event_booking(request):
    return render(request, 'ebooking.html')

def sports_booking(request):
    context = {
        'event_title': request.GET.get('event_title', ''),
        'event_venue': request.GET.get('event_venue', ''),
        'event_date': request.GET.get('event_date', ''),
        'ticket_type': request.GET.get('ticket_type', ''),
        'num_tickets': request.GET.get('num_tickets', '1')
    }
    return render(request, 'sbooking.html', context)

def movie_payments(request):
    return render(request, 'mpayments.html')

def event_payments(request):
    return render(request, 'epayments.html')

def sports_payments(request):
    context = {
        'event_title': request.GET.get('event_title', ''),
        'event_venue': request.GET.get('event_venue', ''),
        'event_date': request.GET.get('event_date', ''),
        'ticket_type': request.GET.get('ticket_type', ''),
        'num_tickets': request.GET.get('num_tickets', '1'),
        'total_amount': request.GET.get('total_amount', '0')
    }
    return render(request, 'spayments.html', context)

def sports_confirmation(request):
    return render(request, 'sconf.html')

def test_sports_booking(request):
    return render(request, 'test-sbooking.html')

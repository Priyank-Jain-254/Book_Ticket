from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Show, Booking

# ------------------------ User Views ------------------------

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        return render(request, 'register.html', {'error': 'Invalid input'})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'show_list.html', {'shows': shows})


@method_decorator(login_required, name='dispatch')
class ShowDetailView(View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'show_detail.html', {'show': show})


@method_decorator(login_required, name='dispatch')
class BookShowView(View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'book_show.html', {'show': show})

    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        seats = int(request.POST.get('seats', 0))
        if seats > 0 and seats <= show.available_seats:
            Booking.objects.create(user=request.user, show=show, seat_count=seats)
            show.available_seats -= seats
            show.save()
            return redirect('booking_history')
        return render(request, 'book_show.html', {
            'show': show,
            'error': 'Invalid number of seats'
        })


@method_decorator(login_required, name='dispatch')
class BookingHistoryView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
        return render(request, 'booking_history.html', {'bookings': bookings})

# ------------------------ Admin Panel Views ------------------------

@method_decorator(login_required, name='dispatch')
class AdminPanelView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'admin_panel.html', {'shows': shows})


@method_decorator(login_required, name='dispatch')
class AddShowView(View):
    def get(self, request):
        return render(request, 'add_show.html')

    def post(self, request):
        title = request.POST.get('title')
        date = request.POST.get('date')
        venue = request.POST.get('venue')
        seats = request.POST.get('seats')

        if title and date and venue and seats:
            Show.objects.create(title=title, date=date, venue=venue, available_seats=int(seats))
            return redirect('admin_panel')

        return render(request, 'add_show.html', {'error': 'All fields are required'})


@method_decorator(login_required, name='dispatch')
class EditShowView(View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'edit_show.html', {'show': show})

    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        show.title = request.POST.get('title')
        show.date = request.POST.get('date')
        show.venue = request.POST.get('venue')
        show.available_seats = int(request.POST.get('seats'))
        show.save()
        return redirect('admin_panel')


@method_decorator(login_required, name='dispatch')
class DeleteShowView(View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        show.delete()
        return redirect('admin_panel')


@method_decorator(login_required, name='dispatch')
class AllBookingsView(View):
    def get(self, request):
        bookings = Booking.objects.all().order_by('-booking_time')
        return render(request, 'all_bookings.html', {'bookings': bookings})

from django.utils import timezone
from datetime import timedelta

def book_show(request, pk):
    show = get_object_or_404(Show, pk=pk)
    current_time = timezone.now()

    allow_booking = show.date > current_time + timedelta(hours=1)

    if request.method == "POST":
        if not allow_booking:
            return render(request, 'book_show.html', {
                'show': show,
                'error': "Booking is closed for this show.",
                'allow_booking': False
            })

        # your booking logic here...

    return render(request, 'book_show.html', {
        'show': show,
        'allow_booking': allow_booking
    })

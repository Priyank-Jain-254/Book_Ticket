from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('shows/', views.ShowListView.as_view(), name='shows'),
    path('show/<int:pk>/', views.ShowDetailView.as_view(), name='show_detail'),
    path('book/<int:pk>/', views.BookShowView.as_view(), name='book_show'),
    path('bookings/', views.BookingHistoryView.as_view(), name='booking_history'),
    path('shows/', views.ShowListView.as_view(), name='shows'),


    # Admin Panel
    path('admin-panel/', views.AdminPanelView.as_view(), name='admin_panel'),
    path('admin/add-show/', views.AddShowView.as_view(), name='add_show'),
    path('admin/edit-show/<int:pk>/', views.EditShowView.as_view(), name='edit_show'),
    path('admin/delete-show/<int:pk>/', views.DeleteShowView.as_view(), name='delete_show'),
    path('admin/bookings/', views.AllBookingsView.as_view(), name='all_bookings'),
]

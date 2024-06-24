from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('dashboard/', views.dashtwo, name='dashboard'),
    path('payouts/', views.payouts, name='payouts'),
    path('datatables/', views.datatables, name='datatables'),
    path('loans/', views.loans, name='loans'),
    path('invoices/', views.invoices, name='invoices'),
    path('profile/', views.profile, name='profile'),
    path('contactbook/', views.contactbook, name='contactbook'),
    path('cards/', views.cards, name='cards'),

]

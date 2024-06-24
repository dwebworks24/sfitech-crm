from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('dashtwo/', views.dashtwo, name='dashtwo'),
    path('datatables/', views.datatables, name='datatables'),
    path('loans/', views.loans, name='loans'),
    path('invoices/', views.invoices, name='invoices'),
    path('profile/', views.profile, name='profile'),
    path('contactbook/', views.contactbook, name='contactbook'),
    path('cards/', views.cards, name='cards'),

]

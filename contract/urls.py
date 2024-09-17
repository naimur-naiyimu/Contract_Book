from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contact_list, name='contact_list'),
    path('add/', views.Contact_add, name='add_contact'),
    path('<int:pk>/edit/', views.Contact_edit, name='edit_contact'),
    path('<int:pk>/delete/', views.Contact_delete, name='delete_contact'),
    # path('<int:pk>/', views.Contact__detail, name='contact_detail'),
    # path('search/', views.search_Contact, name='search_contacts'),
]
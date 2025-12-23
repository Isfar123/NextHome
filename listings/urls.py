from django.urls import path
from .views import dashboard
from . import views
from .views import add_listing
from .views import delete_account

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_listing, name='add_listing'),  
    path('my-listings/', views.my_listings, name='my_listings'),
    path('<int:pk>/', views.listing_detail, name='listing_detail'),
    path('delete_account/', delete_account, name='delete_account'),
   
    
    
]

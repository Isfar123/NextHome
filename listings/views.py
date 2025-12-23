from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Listing, ListingImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        
        # Delete all listings of the user
        Listing.objects.filter(user=user).delete()
        
        # Delete the user account
        user.delete()
        
        # Log out the user
        logout(request)
        
        
        
        # Redirect to home
        return redirect('home')
    else:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('home')




def dashboard(request):
    # Fetch query parameters
    search_query = request.GET.get('search', '')
    block_filter = request.GET.get('block', '')
    rent_filter = request.GET.get('rent', '')
    rooms_filter = request.GET.get('rooms', '')

    # Start with all listings
    listings = Listing.objects.all()

    # Apply filters based on user input
    if search_query:
        listings = listings.filter(description__icontains=search_query) | listings.filter(location__icontains=search_query)
    
    if block_filter:
        listings = listings.filter(block=block_filter)
    
    if rent_filter:
        listings = listings.filter(rent__lte=rent_filter)
    
    if rooms_filter:
        if rooms_filter == "4":
            listings = listings.filter(number_of_rooms__gte=4)
        else:
            listings = listings.filter(number_of_rooms=rooms_filter)

    # Pass filters back to template for persistence in the form
    context = {
        'listings': listings,
        'search_query': search_query,
        'block_filter': block_filter,
        'rent_filter': rent_filter,
        'rooms_filter': rooms_filter,
    }

    return render(request, 'listings/dashboard.html', context)


@login_required
def my_listings(request):
    listings = Listing.objects.filter(user=request.user)  # <-- Fetch listings of the logged-in user
    return render(request, 'listings/my_listings.html', {'listings': listings})



def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

@login_required
def add_listing(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        block = request.POST.get('block')
        rent = request.POST.get('rent')
        number_of_rooms = request.POST.get('number_of_rooms')
        description = request.POST.get('description')
        images = request.FILES.getlist('images')
        
        # Save the listing with the logged-in user attached
        listing = Listing.objects.create(
            user=request.user,             # <-- Attach the user here
            location=location,
            block=block,
            rent=rent,
            number_of_rooms=number_of_rooms,
            description=description
        )

        # Save the images
        for image in images:
            ListingImage.objects.create(listing=listing, image=image)

        messages.success(request, 'Listing added successfully!')
        return redirect('dashboard')

    return render(request, 'listings/add_listing.html')
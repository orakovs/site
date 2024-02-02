from django.shortcuts import render

# Create your views here.
def Home(request):
    
    
    context = {
        'current_page': 'home_url'
    }
    
    return render(request, 'home.html', context)
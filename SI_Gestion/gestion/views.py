from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .models import Account
# Create your views here.
def Choose(request):
    return render(request, 'choose.html')

def Create_form(request):
    return render(request, 'form.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')




def login_validation(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            # Account with this username does not exist
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        
        # Check if the provided password matches the hashed password in the database
        if check_password(password, account.password):
            # Password matches, login the user
            request.session['user_id'] = account.id
            return render(request, 'index.html')
        else:
            # Password does not match
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # GET request, show the login form
        return render(request, 'login.html')
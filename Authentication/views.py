from django.shortcuts import render,redirect

# Create your views here.


from django.contrib.auth.models import User
from django.contrib import auth


def RegisterView(request): 
    if request.method == 'POST': #POST ==POST  => True
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if  password == password2: #welcome @123==Welcome@123  True
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'error':'Username already exists'})
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
            
            
        else:
            print("password did not match")
            return redirect('register')
        
    else:
        return render(request,'Authentication/register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if User is not None:
            auth.login(request,user)
            print('Login Successfully')
            return redirect('showproducts')
        else:
            print("Invalid User")
            return render(request,'Authentication/login.html')
        
    else:
        return render(request,'Authentication/login.html')
    
    
    
    
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        print('Logout Successfully')
    return redirect('login')


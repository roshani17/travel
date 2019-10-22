from django.shortcuts import render,redirect

# Create your views here.
def Mumbai(request):

    if request.user.is_authenticated:
        return render(request,'mumbai.html')
    else:
        return redirect('/account/login')
 
 
    

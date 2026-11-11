from django.shortcuts import render,redirect
from .forms import UserForm,UserProfileForm,LoginForm,UserUpdateForm,UserProfileUpdateForm,VendorRegistrationForm,vendorRegistration
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from buses.models import ALLBuses
from .models import vendorRegistration

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
           user = form1.save()
           user.set_password(user.password)
           user.save()

           profile = form2.save(commit=False)
           profile.user = user  
           profile.save()
           registered = True
    else:
        form1 = UserForm()
        form2 = UserProfileForm()
    context = {
        'form1' : form1,
        'form2' : form2,
        'registered' : registered
    }

    return render(request,"accounts/registration.html",context)



# def user_login(request):
#     if request.method=='POST':
#         form3 = LoginForm(request.POST)
#         if form3.is_valid():
#             username = form3.cleaned_data['username']
#             password = form3.cleaned_data['password']

#             user = authenticate(username=username,password=password)

#             if user:
#                 if user.is_active:
#                     login(request,user)
#                     return redirect("home")
#                 else:
#                     return HttpResponse("User is not active")
#             else:
#                 return HttpResponse("Please check your creds..!!")
#     else:
#         form3 = LoginForm()
#         return render(request,"accounts/login.html",{'form3':form3})



def user_login(request):
    if request.method == 'POST':
        form3 = LoginForm(request.POST)
        if form3.is_valid():
            username = form3.cleaned_data['username']
            password = form3.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:                   
                    if hasattr(user, 'vendorregistration'):
                        if user.vendorregistration.is_approved:
                            login(request, user)
                            return redirect("vendor_dashboard")
                        else:
                            return HttpResponse("<h1>Your vendor account is pending admin approval. Please wait! 🕒</h1>")
                    else:
                        login(request, user)
                        return redirect("home")
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("Please check your creds..!!")
    else:
        form3 = LoginForm()
    return render(request, "accounts/login.html", {'form3': form3})



# @login_required(login_url='login')
# def vendor_dashboard(request):
#     return render(request, "accounts/vendor_dashboard.html", {})


@login_required(login_url='login')
def vendor_dashboard(request):
    try:
        vendor_profile = request.user.vendorregistration
        my_buses = ALLBuses.objects.filter(vendor=vendor_profile)
    except Exception as e:
        my_buses = []
        
    context = {
        'my_buses': my_buses
    }
    return render(request, "accounts/vendor_dashboard.html", context)



#

@login_required(login_url='login')
def home(request):
    approved_vendors = vendorRegistration.objects.filter(is_approved=True)
    
    context = {
        'approved_vendors': approved_vendors
    }
    return render(request, "accounts/home.html", context)



@login_required(login_url = 'login')
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def profile(request):
    return render(request,"accounts/profile.html",{})





@login_required(login_url="login")
def user_update(request):
    try:
        user_details_instance = request.user.userdetails
    except:
        user_details_instance = None

    if request.method == 'POST':
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UserProfileUpdateForm(request.POST, request.FILES, instance=user_details_instance)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("profile")
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = UserProfileUpdateForm(instance=user_details_instance)
        
    return render(request, "accounts/update.html", {'form1': form1, 'form2': form2})








def vendor_register(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = VendorRegistrationForm(request.POST, request.FILES)
        
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            
            profile = form2.save(commit=False)
            profile.user = user  
            profile.save()
            registered = True
    else:
        form1 = UserForm()
        form2 = VendorRegistrationForm()
        
    context = {
        'form1': form1,
        'form2': form2,
        'registered': registered
    }
    return render(request, "accounts/vendor_registration.html", context)






def travels_detail(request, vendor_id):
    agency = vendorRegistration.objects.get(id=vendor_id)
    agency_buses = ALLBuses.objects.filter(vendor=agency)
    
    context = {
        'agency': agency,
        'agency_buses': agency_buses
    }
    return render(request, "accounts/travels_detail.html", context)


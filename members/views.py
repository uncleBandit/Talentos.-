from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import  Organization, Membership
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm




# Dashboard view
@login_required
def dashboard(request):
    # Show organizations this user belongs to
    memberships = Membership.objects.filter(user=request.user)
    organizations = [m.organization for m in memberships]

    context = {
        "user": request.user,
        "organizations": organizations,
    }
    return render(request, "members/dashboard.html", context)


# User profile view
@login_required
def profile(request):
    return render(request, "members/profile.html", {"user": request.user})


# List all organizations
@login_required
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, "members/organization_list.html", {"organizations": organizations})


# Organization detail view
@login_required
def organization_detail(request, pk):
    org = get_object_or_404(Organization, pk=pk)
    members = Membership.objects.filter(organization=org)
    return render(request, "members/organization_detail.html", {"organization": org, "members": members})


# Add a membership (for demonstration)
@login_required
def add_membership(request):
    if request.method == "POST":
        org_id = request.POST.get("organization")
        role = request.POST.get("role", "employer")
        org = get_object_or_404(Organization, pk=org_id)
        Membership.objects.create(user=request.user, organization=org, role=role)
        return redirect("dashboard")
    organizations = Organization.objects.all()
    return render(request, "members/add_membership.html", {"organizations": organizations})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately
            return redirect("dashboard")  # Or wherever you want
    else:
        form = SignUpForm()
    
    return render(request, "members/signup.html", {"form": form})
# Generic test page (optional)
#def members_test(request):
    #return render(request, "members/myfirst.html")

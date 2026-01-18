from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from members.models import Organization, Membership
from django.utils import timezone

# List all jobs
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, "jobs/job_list.html", {"jobs": jobs})


# Job detail page
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    # Check if user is an employer/admin for this organization
    can_edit = False
    if request.user.is_authenticated:
        can_edit = Membership.objects.filter(
            user=request.user,
            organization=job.organization,
            role__in=["employer", "admin"]
        ).exists()

    return render(request, "jobs/job_detail.html", {"job": job, "can_edit": can_edit})

# Create a new job (only for employers/admins)
@login_required
def job_create(request):
    # Check if user is an employer in any org
    memberships = Membership.objects.filter(user=request.user, role__in=["employer", "admin"])
    if not memberships.exists():
        return redirect("job_list")  # redirect if not authorized

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        org_id = request.POST.get("organization")
        org = get_object_or_404(Organization, pk=org_id)
        Job.objects.create(
            title=title,
            description=description,
            organization=org,
            created_at=timezone.now()
        )
        return redirect("job_list")

    organizations = [m.organization for m in memberships]
    return render(request, "jobs/job_form.html", {"organizations": organizations})


# Edit job (only by employer/admin of the org)
@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    membership = Membership.objects.filter(user=request.user, organization=job.organization, role__in=["employer", "admin"])
    if not membership.exists():
        return redirect("job_detail", pk=pk)

    if request.method == "POST":
        job.title = request.POST.get("title")
        job.description = request.POST.get("description")
        job.save()
        return redirect("job_detail", pk=pk)

    return render(request, "jobs/job_form.html", {"job": job, "organizations": [job.organization]})


# Apply to a job
@login_required
def job_apply(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        cover_letter = request.POST.get("cover_letter")
        JobApplication.objects.create(
            job=job,
            applicant=request.user,
            cover_letter=cover_letter,
            applied_at=timezone.now()
        )
        return redirect("job_detail", pk=pk)
    return render(request, "jobs/job_apply.html", {"job": job})


# Optional: List applicants for a job (employer/admin only)
@login_required
def job_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)
    membership = Membership.objects.filter(user=request.user, organization=job.organization, role__in=["employer", "admin"])
    if not membership.exists():
        return redirect("job_detail", pk=pk)

    applications = JobApplication.objects.filter(job=job)
    return render(request, "jobs/job_applicants.html", {"job": job, "applications": applications})

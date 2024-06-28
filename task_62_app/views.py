from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import modelformset_factory, inlineformset_factory

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from task_62_app.models import Skill, Achievement

from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This mail id already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, 'The password doesnot match')
        return redirect('login')
    return render(request, 'register.html')


def update_user(request):
    if request.method == 'POST':
        form = update_user_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = update_user_form(instance=request.user)

    return render(request, 'update_user.html', {'form': form})


def add_basic_details(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,
                             'Basic details added successfully!' if created else 'Basic details updated successfully!')
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'add_basic_details.html', context)


def update_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'update_user_password.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials...')
            return redirect('login')
    return render(request, 'login.html')


def logOut(request):
    auth.logout(request)
    return redirect('login')


@login_required
def home_page(request):
    skills = Skill.objects.filter(user=request.user)
    achievements = Achievement.objects.filter(user=request.user)
    profile = UserProfile.objects.filter(user=request.user).first()
    contact = contact_details.objects.filter(user=request.user).first()
    context = {
        'skills': skills,
        'achievements': achievements,
        'profile': profile,
        'contact': contact
    }
    return render(request, 'home.html', context)


def add_contact_details(request):
    contact, created = contact_details.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = contact_details_form(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request,
                             'Contact details added successfully!' if created else 'Contact details updated successfully!')
            return redirect('home')
    else:
        form = contact_details_form(instance=contact)

    context = {
        'form': form,
        'contact': contact
    }
    return render(request, 'add_contact_details.html', context)


def add_skills(request):
    if request.method == 'POST':
        form = skill_form(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('home')
    else:
        form = skill_form()
    return render(request, 'add_skill.html', {'form': form})


def update_skills(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    if request.method == 'POST':
        form = skill_form(request.POST, instance=skill)
        if form.is_valid():
            skill.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('home')
    else:
        form = skill_form(instance=skill)
    return render(request, 'update_skill.html', {'form': form})


@login_required
def project_page(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    contact = contact_details.objects.filter(user=request.user).first()
    project_show = project_showcase.objects.filter(user=request.user)
    context = {
        'profile': profile,
        'contact': contact,
        "project_show": project_show,
    }
    return render(request, 'project.html', context)


@login_required
def portfolio_page(request):
    # skills = Skill.objects.filter(user=request.user)
    # achievements = Achievement.objects.filter(user=request.user)
    profile = UserProfile.objects.filter(user=request.user).first()
    contact = contact_details.objects.filter(user=request.user).first()
    projects = project_showcase.objects.filter(user=request.user)
    works = work_experience.objects.filter(user=request.user)
    educ = education.objects.filter(user=request.user)
    certificate = certifications.objects.filter(user=request.user)
    context = {
        'profile': profile,
        'contact': contact,
        'projects': projects,
        'works': works,
        'educ' : educ,
        'certificate' : certificate
    }
    return render(request, 'portfolio.html', context)


def project_showcase_create_view(request):
    if request.method == 'POST':
        form = project_showcase_form(request.POST, request.FILES)
        if form.is_valid():
            project_showcases = form.save(commit=False)
            project_showcases.user = request.user
            project_showcases.save()
            return redirect('project')
    else:
        form = project_showcase_form()
    context = {
        'form': form,
    }
    return render(request, 'add_project_showcase.html', context)


def project_showcase_update_view(request, project_id):
    project = get_object_or_404(project_showcase, id=project_id, user=request.user)
    if request.method == 'POST':
        form = project_showcase_form(request.POST, request.FILES, instance=project)

        if form.is_valid():
            project.save()
            return redirect('project')
    else:
        form = project_showcase_form(instance=project)

    context = {
        'form': form,
    }
    return render(request, 'update_project_showcase.html', context)


def project_showcase_delete_view(request, project_id):
    project = get_object_or_404(project_showcase, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context = {
        'project': project,
    }
    return render(request, 'delete_project_confirm.html', context)


def add_work_experience(request):
    if request.method == 'POST':
        form = work_experience_form(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.save()
            return redirect('portfolio')
    else:
        form = work_experience_form()
    context = {
        'form': form,
    }
    return render(request, 'add_work_experience.html', context)


def update_work_experience(request, work_id):
    work = get_object_or_404(work_experience, id=work_id, user=request.user)
    if request.method == 'POST':
        form = work_experience_form(request.POST, request.FILES, instance=work)

        if form.is_valid():
            work.save()
            return redirect('portfolio')
    else:
        form = work_experience_form(instance=work)

    context = {
        'form': form,
    }
    return render(request, 'update_work_experience.html', context)


def delete_work_experience(request, work_id):
    work = get_object_or_404(work_experience, id=work_id, user=request.user)
    if request.method == 'POST':
        work.delete()
        return redirect('portfolio')
    context = {
        'work': work,
    }
    return render(request, 'delete_work_confirm.html', context)

def add_education(request):
    if request.method == 'POST':
        form = education_form(request.POST)
        if form.is_valid():
            educ = form.save(commit=False)
            educ.user = request.user
            educ.save()
            return redirect('portfolio')
    else:
        form = education_form()
    context = {
        'form': form,
    }
    return render(request, 'add_education.html', context)


def update_education(request, ed_id):
    educ = get_object_or_404(education, id=ed_id, user=request.user)
    if request.method == 'POST':
        form = education_form(request.POST, request.FILES, instance=educ)

        if form.is_valid():
            educ.save()
            return redirect('portfolio')
    else:
        form = education_form(instance=educ)

    context = {
        'form': form,
    }
    return render(request, 'update_education.html', context)


def delete_education(request, ed_id):
    educ = get_object_or_404(education, id=ed_id, user=request.user)
    if request.method == 'POST':
        educ.delete()
        return redirect('portfolio')
    context = {
        'educ': educ,
    }
    return render(request, 'delete_education_confirm.html', context)


def add_certifications(request):
    if request.method == 'POST':
        form = certificates_form(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('portfolio')
    else:
        form = certificates_form()
    context = {
        'form': form,
    }
    return render(request, 'add_certifications.html', context)


def update_certifications(request, certificate_id):
    certificate = get_object_or_404(certifications, id=certificate_id, user=request.user)
    if request.method == 'POST':
        form = certificates_form(request.POST, request.FILES, instance=certificate)

        if form.is_valid():
            certificate.save()
            return redirect('portfolio')
    else:
        form = certificates_form(instance=certificate)

    context = {
        'form': form,
    }
    return render(request, 'update_certifications.html', context)


def delete_certifications(request, certificate_id):
    certificate = get_object_or_404(certifications, id=certificate_id, user=request.user)
    if request.method == 'POST':
        certificate.delete()
        return redirect('portfolio')
    context = {
        'certificate': certificate,
    }
    return render(request, 'delete_certifications_confirm.html', context)

User = get_user_model()

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')

    return render(request, 'delete_account.html')
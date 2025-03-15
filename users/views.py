from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from .models import CustomUser, Profile, StudentProfile, ProfessionalProfile, MentorProfile, CompanyProfile
from .forms import (
    CustomUserCreationForm, CustomUserChangeForm, ProfileForm,
    StudentProfileForm, ProfessionalProfileForm, MentorProfileForm,
    CompanyProfileForm, UserTypeForm
)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create associated profile based on user type
            Profile.objects.create(user=user)
            
            if user.user_type == 'student':
                StudentProfile.objects.create(user=user)
            elif user.user_type == 'professional':
                ProfessionalProfile.objects.create(user=user)
            elif user.user_type == 'mentor':
                MentorProfile.objects.create(user=user)
            elif user.user_type == 'company':
                CompanyProfile.objects.create(user=user)
            
            login(request, user)
            messages.success(request, 'Registration successful. Please complete your profile.')
            return redirect('users:profile_setup')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_setup(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if user.user_type == 'student':
            specific_form = StudentProfileForm(request.POST, instance=user.studentprofile)
        elif user.user_type == 'professional':
            specific_form = ProfessionalProfileForm(request.POST, instance=user.professionalprofile)
        elif user.user_type == 'mentor':
            specific_form = MentorProfileForm(request.POST, instance=user.mentorprofile)
        else:  # company
            specific_form = CompanyProfileForm(request.POST, instance=user.companyprofile)
        
        if profile_form.is_valid() and specific_form.is_valid():
            profile_form.save()
            specific_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:dashboard')
    else:
        profile_form = ProfileForm(instance=profile)
        
        if user.user_type == 'student':
            specific_form = StudentProfileForm(instance=user.studentprofile)
        elif user.user_type == 'professional':
            specific_form = ProfessionalProfileForm(instance=user.professionalprofile)
        elif user.user_type == 'mentor':
            specific_form = MentorProfileForm(instance=user.mentorprofile)
        else:  # company
            specific_form = CompanyProfileForm(instance=user.companyprofile)
    
    return render(request, 'users/profile_setup.html', {
        'profile_form': profile_form,
        'specific_form': specific_form
    })

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile')
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['profile_form'] = ProfileForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
            if self.request.user.user_type == 'student':
                context['specific_form'] = StudentProfileForm(self.request.POST, instance=self.request.user.studentprofile)
            elif self.request.user.user_type == 'professional':
                context['specific_form'] = ProfessionalProfileForm(self.request.POST, instance=self.request.user.professionalprofile)
            elif self.request.user.user_type == 'mentor':
                context['specific_form'] = MentorProfileForm(self.request.POST, instance=self.request.user.mentorprofile)
            else:  # company
                context['specific_form'] = CompanyProfileForm(self.request.POST, instance=self.request.user.companyprofile)
        else:
            context['profile_form'] = ProfileForm(instance=self.request.user.profile)
            if self.request.user.user_type == 'student':
                context['specific_form'] = StudentProfileForm(instance=self.request.user.studentprofile)
            elif self.request.user.user_type == 'professional':
                context['specific_form'] = ProfessionalProfileForm(instance=self.request.user.professionalprofile)
            elif self.request.user.user_type == 'mentor':
                context['specific_form'] = MentorProfileForm(instance=self.request.user.mentorprofile)
            else:  # company
                context['specific_form'] = CompanyProfileForm(instance=self.request.user.companyprofile)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        specific_form = context['specific_form']
        
        if profile_form.is_valid() and specific_form.is_valid():
            form.save()
            profile_form.save()
            specific_form.save()
            messages.success(self.request, 'Profile updated successfully.')
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile_user'
    
    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs.get('username'))

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
        'profile': user.profile,
    }
    
    if user.user_type == 'student':
        # Add student-specific dashboard data
        context['student_profile'] = user.studentprofile
        # Add recommended careers, courses, etc.
    elif user.user_type == 'professional':
        # Add professional-specific dashboard data
        context['professional_profile'] = user.professionalprofile
        # Add industry insights, networking suggestions, etc.
    elif user.user_type == 'mentor':
        # Add mentor-specific dashboard data
        context['mentor_profile'] = user.mentorprofile
        # Add mentee requests, scheduled sessions, etc.
    else:  # company
        # Add company-specific dashboard data
        context['company_profile'] = user.companyprofile
        # Add job postings, candidate matches, etc.
    
    return render(request, 'users/dashboard.html', context) 
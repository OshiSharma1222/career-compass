from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Profile, StudentProfile, ProfessionalProfile, MentorProfile, CompanyProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'location', 'date_of_birth', 'phone_number')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'cover_image', 'headline', 'skills', 'interests', 'education', 'experience', 'certifications', 'social_links')
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3}),
            'interests': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'certifications': forms.Textarea(attrs={'rows': 3}),
            'social_links': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_skills(self):
        skills = self.cleaned_data['skills']
        if isinstance(skills, str):
            try:
                import json
                return json.loads(skills)
            except json.JSONDecodeError:
                return skills.split(',')
        return skills

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('current_education', 'field_of_study', 'graduation_year', 'career_interests', 'academic_achievements')
        widgets = {
            'career_interests': forms.Textarea(attrs={'rows': 3}),
            'academic_achievements': forms.Textarea(attrs={'rows': 3}),
        }

class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        fields = ('current_position', 'company', 'industry', 'years_of_experience', 'expertise')
        widgets = {
            'expertise': forms.Textarea(attrs={'rows': 3}),
        }

class MentorProfileForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = ('expertise_areas', 'mentorship_focus', 'availability')
        widgets = {
            'expertise_areas': forms.Textarea(attrs={'rows': 3}),
            'mentorship_focus': forms.Textarea(attrs={'rows': 3}),
            'availability': forms.Textarea(attrs={'rows': 3}),
        }

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'industry', 'company_size', 'website', 'company_description', 'hiring_status')
        widgets = {
            'company_description': forms.Textarea(attrs={'rows': 4}),
        }

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        label=_("I am a")
    ) 
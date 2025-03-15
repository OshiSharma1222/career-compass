from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('mentor', 'Mentor'),
        ('company', 'Company'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    def get_absolute_url(self):
        return reverse('users:profile', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    skills = models.JSONField(default=list, blank=True)
    interests = models.JSONField(default=list, blank=True)
    education = models.JSONField(default=list, blank=True)
    experience = models.JSONField(default=list, blank=True)
    certifications = models.JSONField(default=list, blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    current_education = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    career_interests = models.JSONField(default=list, blank=True)
    academic_achievements = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Student Profile"

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    current_position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(default=0)
    expertise = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Professional Profile"

class MentorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    expertise_areas = models.JSONField(default=list)
    mentorship_focus = models.JSONField(default=list)
    availability = models.JSONField(default=dict)
    rating = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    total_mentees = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Mentor Profile"

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    company_size = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    company_description = models.TextField(blank=True)
    hiring_status = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.company_name}'s Profile" 
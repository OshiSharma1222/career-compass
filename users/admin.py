from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Profile, StudentProfile, ProfessionalProfile, MentorProfile, CompanyProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_type', 'bio', 'location', 'date_of_birth', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline')
    search_fields = ('user__username', 'user__email', 'headline')

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_education', 'field_of_study', 'graduation_year')
    search_fields = ('user__username', 'user__email', 'current_education', 'field_of_study')
    list_filter = ('graduation_year',)

class ProfessionalProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_position', 'company', 'industry', 'years_of_experience')
    search_fields = ('user__username', 'user__email', 'current_position', 'company', 'industry')
    list_filter = ('industry', 'years_of_experience')

class MentorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'verified', 'total_mentees')
    search_fields = ('user__username', 'user__email')
    list_filter = ('verified', 'rating')

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'industry', 'company_size', 'hiring_status', 'verified')
    search_fields = ('company_name', 'industry')
    list_filter = ('industry', 'company_size', 'hiring_status', 'verified')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)
admin.site.register(MentorProfile, MentorProfileAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin) 
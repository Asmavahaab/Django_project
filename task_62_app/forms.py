from django import forms
from django.contrib.auth.models import User

from . models import *

class skill_form(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']

class achievement_form(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = "__all__"

class update_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'dob', 'mother_tongue', 'nationality', 'blood_group']

class contact_details_form(forms.ModelForm):
    class Meta:
        model = contact_details
        fields = ['phone_number','whatsapp_number','address','linkedin_handle','insta_handle']


class project_showcase_form(forms.ModelForm):
    class Meta:
        model = project_showcase
        fields = ['project_title','technologies_used','project_description','project_link','project_images']



class work_experience_form(forms.ModelForm):
    class Meta:
        model = work_experience
        fields = ['company_name','job_title','mode','start_date','duration','responsibilities']

class education_form(forms.ModelForm):
    class Meta:
        model = education
        fields = ['course','institute','board','aggregrate_marks','year_of_passing']

class certificates_form(forms.ModelForm):
    class Meta:
        model = certifications
        fields = ['topic','issuing_organisation','date_of_issue','certificate_link']
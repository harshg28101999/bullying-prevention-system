from django import forms
from django.db import models
from datetime import datetime
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


#Add feature where email and name are not required when logged in.
class ReportForm(forms.Form):
	your_name = forms.CharField(required=True)
	your_email = forms.EmailField(required=True)
	date_time_of_incident= forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=False)    
	description = forms.CharField(required=True, widget=forms.Textarea)

class StudentRegisterForm(UserCreationForm):

	# What is this?
    class Meta(UserCreationForm.Meta):
        model = User

    #Help saves data
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()

        # Create student in models
        # A student profile crreated to add info
        student = Student.objects.create(user=user)
        return user

    #return render(request = request,
     #             template_name = "main/register.html",
      #            context={"form":form})

class TeacherRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        # What is commit?
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        # A student profile crreated to add info
        teacher = Teacher.objects.create(user=user)
        if commit:
            user.save()
        return user

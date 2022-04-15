from django import forms
from .models import post,Profile,Comment
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','body')

class PostEditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','body')

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="",widget=forms.PasswordInput)
    
class UserRegistationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(label='confirm_password',widget=forms.PasswordInput(attrs={'placeholder':' Confirm_Password'}))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )
        def clean_confrom_password(self):
            password = self.clean_confrom_password('password')
            confirm_password = self.clean_confrom_password('confirm_password')
            if password != confirm_password:
                raise  forms.ValidationError('Password Missmatch')
            else:
                return confirm_password



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            'user',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
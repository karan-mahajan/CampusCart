from django import forms
from .models import Profile, UserComment, Report, Contact, UserRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.helper import FormHelper
from PIL import Image
from django.conf import settings


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone_number", "address", "profile_image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('phone_number', css_class='form-control'),
            Field('address', css_class='form-control'),
            Field('profile_image', css_class='form-control'),
        )

    def save(self):
        super.save()

        img = Image.open(self.profile_image.path)
        if img.height > 400 and img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control'),
        )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith(settings.EMAIL_VERIFY):
            raise forms.ValidationError(f'Please enter a {settings.EMAIL_VERIFY} mail')
        elif get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists! Please try a different email.')
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
        )
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['username'].help_text = 'Cannot Change Username again'
        self.fields['email'].help_text = 'Cannot Change Email again'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "address",
            "profile_image",
            "bio",
            "user_class",
            "course",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("phone_number", css_class="form-control"),
            Field("address", css_class="form-control"),
            Field("profile_image", css_class="form-control"),
            Field("bio", css_class="form-control", placeholder="Enter your bio"),
            Field(
                "user_class", css_class="form-control", placeholder="Enter your class"
            ),
            Field("course", css_class="form-control", placeholder="Enter your course"),
        )
        self.fields['address'].help_text = 'Please enter your complete address'


class UserCommentsForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('comment', css_class='form-control'),
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "number", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name", css_class="form-control"),
            Field("email", css_class="form-control"),
            Field("number", css_class="form-control"),
            Submit("submit", "Submit", css_class="btn btn-primary"),
        )


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("report", css_class="form-control"),
            Submit("submit", "Submit", css_class="btn btn-primary"),
        )


class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['item_name', 'description', 'item_category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("item_name", css_class="form-control"),
            Field("description", css_class="form-control"),
            Field("item_category", css_class="form-control"),
        )
        self.fields['item_name'].help_text = 'Please enter the item you are looking for.'
        self.fields['item_category'].help_text = 'Please select the category you are looking for.'
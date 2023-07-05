from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or ' \
                                            'fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small">' \
                                             '<li>Your password can\'t be too similar to your other personal ' \
                                             'information.</li>' \
                                             '<li>Your password must contain at least 8 characters.</li>' \
                                             '<li>Your password can\'t be a commonly used password.</li>' \
                                             '<li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">' \
                                             '<small>Enter the same password as before notification.</small></span>'


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control", "id": "firstnameid"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control", "id": "lastnameid"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Email", "class": "form-control", "id": "emailid"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Phone", "class": "form-control", "id": "phoneid"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Address", "class": "form-control", "id": "addressid"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "City", "class": "form-control", "id": "cityid"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "State", "class": "form-control", "id": "stateid"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Zipcode", "class": "form-control", "id": "zipcodeid"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone',  'address', 'city', 'state', 'zipcode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstnameid'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastnameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phoneid'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'addressid'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'cityid'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'id': 'stateid'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'id': 'zipcodeid'})

        }

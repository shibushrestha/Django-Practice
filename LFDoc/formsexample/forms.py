from django import forms
from django.forms import ModelForm
from .models import Person
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError



# A validator to validate a username uniqueness with respect to the Person model
def unique_username(value):
    if value and Person.objects.filter(username=value).exists():
        raise ValidationError(_('Username already taken.....'), code='unique')

# Name validator that only accepts alphabets [a-zA-Z]
name_validator = RegexValidator(r'^[a-zA-Z]*$', message=_('Only alphabets are allowed.'))

# Username validator tha only accepts alphanumeric character and !#@_
username_validator = RegexValidator(r'^[a-zA-Z0-9!#@_]', 
    message=_('Only alphanumeric character and !#@_ is allowed.'), code='alphanumeric')

# A normal form
class CreatePersonForm(forms.Form):
    username = forms.CharField(max_length=100, validators=[unique_username, username_validator], 
        widget=forms.TextInput(attrs={'placeholder':"Enter a username"}))
    first_name = forms.CharField(max_length=100, validators=[name_validator] )
    last_name = forms.CharField(max_length=100, validators=[name_validator], 
        widget=forms.TextInput(attrs={'placeholder':'Your last name'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD', 'size':15}))
    email = forms.EmailField(validators=[EmailValidator],
        widget=forms.EmailInput(attrs={'placeholder':'Enter a Email address'}))
    comments = forms.CharField(max_length=1000, widget=forms.Textarea)

    # You can also add widget to field like this:
    first_name.widget.attrs.update({'placeholder':"Your first name"})

    # define a custom clean method on a specific field
    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username == 'kidbenwah':
            raise ValidationError('Username not allowed.')
        return username

    # Cleaning fields that depend upon each other.
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        if username and first_name and username==first_name:
            raise ValidationError(_("Username and first name can't be same"), code="can't be same")
        
    
    

#   MODELFORM 
class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter a username',})
        self.fields['first_name'].widget.attrs.update({'placeholder':'Your first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Your last name'})
        self.fields['date_of_birth'].widget.attrs.update({'placeholder':'YYYY-MM-DD'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter a email address'})
        self.fields['comments'].required = False
        # Override the model validation logic in forms like so:
        #self.fields['username'].validators = [unique_username]
            
    class Meta():
        model = Person
        # You can include every fields from the Model like this.
        # fields = '__all__'
        # Or specify all fields like this
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email', 'comments',)
        labels = {
            'username' : 'Username',
            'first_name' : 'First name',
            'last_name' : 'Last name',
            'date_of_birth' : 'Birth date',
            'email' : 'Email address',
            'comments' : 'Comments',
        }

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email == "shibushrestha12@gmail.com":
            raise ValidationError('This email is already taken.')
        return email
       
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        if username and first_name is not None: 
            if username == first_name:
                raise ValidationError('username and first_name cannot bet same.')
        

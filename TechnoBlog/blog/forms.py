from django.forms import ModelForm
from . models  import contactUsersTable

class contactUsers(ModelForm):
    class Meta():
        model = contactUsersTable
        fields = ['fname', 'lname', 'email', 'phone', 'comment']
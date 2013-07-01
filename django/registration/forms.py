from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import ugettext, ugettext_lazy as _

from registration.models import GameUser

class UserCreateForm(forms.ModelForm):
	"""
	A form that creates a user, with no privileges, from the given username and
	password.
	"""
	
	error_messages = {
		'duplicate_username': _("A user with that username already exists."),
		'password_mismatch': _("The two password fields didn't match."),
	}
	first_name = forms.RegexField(label=_("First Name"), max_length=100,
		regex=r'^[a-zA-Z\s\-\']+$',
		error_messages={
			'invalid': "This value may contain only letters, numbers and "
						 "@/./+/-/_ characters."},)

	last_name = forms.RegexField(label=_("Last Name"), max_length=100,
		regex=r'^[\w\s]+$',
		error_messages={
			'invalid': "This value may contain only letters, numbers and "
						 "@/./+/-/_ characters."},)

	username = forms.RegexField(label=_("Username"), max_length=30,
		regex=r'^[\w.@+-]+$',
		help_text=_("Required. 30 characters or fewer. Letters, digits and "
					  "@/./+/-/_ only."),
		error_messages={
			'invalid': _("This value may contain only letters, numbers and "
						 "@/./+/-/_ characters.")})

	email = forms.EmailField(required=True,
		error_messages={'invalid': _("This must be a valid e-mail address.")})
	
	password = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)

	class Meta:
		model = GameUser
		fields = ("first_name", "last_name", "username",)

	def clean_username(self):
		# Since User.username is unique, this check is redundant,
		# but it sets a nicer error message than the ORM. See #13147.
		username = self.cleaned_data["username"]
		try:
			GameUser._default_manager.get(username=username)
		except GameUser.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code='duplicate_username',
		)

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		user.is_staff = True;
		user.is_superuser = True;
		if commit:
			user.save()
		return user

# class UserCreateForm(UserCreationForm):


#     error_messages = {
#         'duplicate_username': _("A user with that username already exists."),
#         'password_mismatch': _("The two password fields didn't match."),
#     }

#     class Meta:
#         model = User
#         fields = ("email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user
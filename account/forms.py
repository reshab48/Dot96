from django import forms
from django.contrib.auth.models import User
from account.models import Profile, Address, FeedBack

class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(max_length=50, help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.", widget=forms.TextInput(attrs={'placeholder' : 'Eg: someone96'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'First Name'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}))
	email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'someone@example.com'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def cleaned_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			return forms.ValidationError('Your passwords didn\'t match')
		return cd['password2']

class ProfileCreateEditForm(forms.ModelForm):
	mobile_no = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder' : 'XXXXXXXXXX'}))

	class Meta:
		model = Profile
		fields = ('mobile_no',)

class UserEditForm(forms.ModelForm):
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'First Name'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}))
	email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'someone@example.com'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class AddressAddForm(forms.ModelForm):
	full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Full Name'}))
	street = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Eg: Azadhind Sarani Subashpally'}))
	pin = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder' : 'Eg: 734001'}))
	landmark = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Eg: Near Hati More'}))
	phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder' : 'XXXXXXXXXX'}))

	class Meta:
		model = Address
		fields = ('full_name', 'street', 'city', 'pin', 'landmark', 'phone')

class FeedBackAddForm(forms.ModelForm):
	subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Eg: Problem in delivery'}))

	class Meta:
		model = FeedBack
		fields = ('subject', 'description')
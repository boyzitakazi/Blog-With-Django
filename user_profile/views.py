from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .models import PostModel

# Create your views here.

# Untuku Menampilkan Portofolio
class Portofolio(TemplateView):
	template_name = 'portfolio.html'


# Untuku Menampilkan About Us
class AboutUs(TemplateView):
	template_name = 'about-us.html'


# Contoh Registrasi
def register(request):
	# template registrasi akun ada di main
	template_name = 'register.html'
	
	if request.method == 'POST':

		# inherit dari Forms
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():

			# data dibershihkan dan bisa diinput pada database
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			password = userObj['password']

			# membuat akun
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username=username, password=password)
				login(request, user) # masuk

				# tampilan setelah masuk
				return render(request,template_name,{'p':'p'})
			
			else:
				# pesan jika ada data yang sama
				raise forms.ValidationError('Looks like a username with that email or password already exists')

	else:
		# jika salah maka akan tetap di tampilan form
		form = UserRegisterForm()

	# tampilan untuk form registrasi
	return render(request, template_name,{'form':form})


# ========== Start Blog Post ============== #
# Untuku Menampilkan Semua Postingan
def blog_post(request):
	post_model = PostModel.objects.all()

	context = {
		'post_model':post_model,
	}

	return render(request,'blog.html',context)

# Untuku Menampilkan Single Post/Blog Menggunakan ID
def single_blog(request, urlid):
	post_model = PostModel.objects.filter(id=urlid)

	context = {
		'post_model':post_model,
	}

	return render(request,'single-blog.html',context)
# ========== End Blog Post ============== #


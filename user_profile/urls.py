from django.urls import path, include
from .views import blog_post, single_blog, Portofolio, AboutUs # mengambil fungction/class dari views

urlpatterns = [
	# url dari views untuk ditampilkan pada browser (tampilan untuk About)
    path('about', AboutUs.as_view(), name='about' ),

	# url dari views untuk ditampilkan pada browser (tampilan untuk Portofolio)
    path('portofolio', Portofolio.as_view(), name='portofolio' ),

	# url dari views untuk ditampilkan pada browser menggunakan parameter(tampilan untuk detail Post)
    path('blog/<urlid>', single_blog, name='single_blog' ),

    # url dari views untuk ditampilkan pada browser (tampilan untuk semua post)
    path('blog', blog_post, name='blog_post' ),
]
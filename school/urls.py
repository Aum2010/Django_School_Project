from django.urls import path , include
from .views import HomePage,AboutPage,ContactPage,ScorePage,RegisterPage
urlpatterns = [
    path('home/',HomePage,name='home-page'),
    path('about/',AboutPage,name='about-page'),
    path('contact/',ContactPage,name='contact-page'),
    path('score/',ScorePage,name='score-page'),
    path('register/',RegisterPage,name='register-page'),
]

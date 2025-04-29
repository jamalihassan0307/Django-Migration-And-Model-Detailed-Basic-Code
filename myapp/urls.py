
from django.urls import path



from . import views

urlpatterns = [

path('mysite/', views.message),
path('Hi/', views.greeting),
path('', views.home, name = 'home'),
path('about-us/', views.contact, name = 'contact'),
path('a/', views.a, name = 'a'),
path('b/', views.b, name = 'b'),
path('c/', views.c, name = 'c'),

path('response/', views.response, name = 'response'),
path('form-submit/', views.submit_form, name = 'submit_form'),
path('XYZ/<str:email>/', views.url_data, name = 'xyz'),

path('create_artist/', views.create_artist, name = 'create_artist'),
path('artists/', views.fetch_artists, name = 'artists'),
path('delete-artist/<int:pk>/', views.delete_artist, name = 'del_artist'),
path('edit-artist/<int:pk>/', views.edit_artist, name = 'edit_artist'),
]
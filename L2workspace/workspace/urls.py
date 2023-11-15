from django.urls import path
from . import views #importing the views file from this directory


urlpatterns = [
    path('', views.index, name='index'),
    path('wiki_view/', views.wiki_view, name='wiki_view'),
    #path('login_user/', views.login_user, name='login_user'),

]

# need to creat a section in the database that stores urls that way I can interate through each and check to see if the status code is 
#200 when printing cards else I still want to print a card slot for that url but instead of  a redirect the card will show error message
#say there is a error try connecting to Ricoh VPn
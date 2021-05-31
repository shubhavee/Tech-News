from django.urls import path
from story import views

#TEMPLATE TAGGING
app_name = 'story'

urlpatterns = [
    path('submit/', views.submit, name='submit'),
    path('newest/', views.newest, name='newest'),
    path('s/<int:story_id>/vote/', views.vote, name='vote'),
    path('s/<int:story_id>/', views.story, name='story'),
    path('search/', views.search, name='search'),

]

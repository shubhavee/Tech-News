from django.urls import path
from userprofile import views

#TEMPLATE TAGGING
app_name = 'userprofile'

urlpatterns = [
    # path('submit/', views.submit, name='submit'),
    # path('newest/', views.newest, name='newest'),
    # path('s/<int:story_id>/vote/', views.vote, name='vote'),
    # path('s/<int:story_id>/', views.story, name='story'),
    path('<str:username>/', views.userprofile, name='userprofile'),
    path('<str:username>/votes/', views.votes, name='votes'),
    path('<str:username>/submissions/', views.submissions, name='submissions'),

]

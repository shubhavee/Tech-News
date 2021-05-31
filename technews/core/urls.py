from django.urls import path
from core import views
# from apps.core.views import signup


#TEMPLATE TAGGING
app_name = 'core'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

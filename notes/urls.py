from django.urls import path
from .views import *

app_name = 'notes'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', NotesListView.as_view(template_name='base.html'), name='note_list'),
    path('note/<int:pk>/', NotesDetailView.as_view(), name='note_detail')
]

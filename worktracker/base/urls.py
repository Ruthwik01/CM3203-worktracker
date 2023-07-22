from django.urls import path
from .views import TaskLi, home, TaskDe, TaskAdd, TaskEdit, TaskDelete, LoginVi, assessment, dashboard, Register, show_assessments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginVi.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('todo/', TaskLi.as_view(), name='tasks'),
    path('todo/<int:pk>/', TaskDe.as_view(), name='task'),
    path('task_add/', TaskAdd.as_view(), name='task_add'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('assessment', assessment, name='assessment'),
    path('register/', Register.as_view(), name='register'),
    path('assessments/', show_assessments, name='show_assessments')
]

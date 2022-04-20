from django.urls import path

from task.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

)

urlpatterns = [
    path('', TaskListView.as_view(), name='home-page'),
    path('/create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tags/', TagsListView.as_view(), name='tags-list'),
    path('tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
app_name = 'task'

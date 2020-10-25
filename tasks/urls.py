from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.TaskListView.as_view(), name='list'),
	path('complete/<int:uid>', views.complete_task, name='complete'),
	path('delete/<int:uid>', views.delete_task, name='delete'),
	path('create/', views.TaskCreateView.as_view(), name="create"),
	path("edit/<int:pk>", views.TaskEditView.as_view(), name="edittask"),
	path("export/", views.TaskExportView.as_view(), name="export"),
]
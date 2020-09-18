from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,  name='login'),
    path('register/', views.register,  name='register'),
    path('logout_user/', views.logout_user,  name='logout_user'),
    path('',views.index, name='index'),
    path('delete/<int:item_id>/',  views.delete, name='delete'),
    path('cross_off/<int:item_id>/',  views.cross_off, name='cross_off'),
    path('uncross/<int:item_id>/',  views.uncross, name='uncross'),
    path('edit/<int:item_id>/',  views.edit, name='edit'),
    path('search/',  views.search, name='search'),
    path('completed_task/',  views.completed_task, name='completed_task'),
    path('ongoing_task/',  views.ongoing_task, name='ongoing_task'),
    path('all_completed/',  views.all_completed, name='all_completed'),
    path('all_ongoing/',  views.all_ongoing, name='all_ongoing'),
    path('del_completed/',  views.del_completed, name='del_completed'),
    path('del_all/',  views.del_all, name='del_all'),
]
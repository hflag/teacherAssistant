from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'teacher'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('coursetable/', views.CourseTableView.as_view(), name='coursetable'),
    path('classactive/', views.ClassActive.as_view(), name='active'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logou_then_login'),
    path('ask/', views.CustomerAskView.as_view(), name='ask'),
    path('summary/', views.SummaryView.as_view(), name='summary'),
    path('score/<str:banji_name>/<str:scorename>/', views.ClassStudentActScoreView.as_view(), name='score'),
    path('export2excel/<str:banji_name>/<str:scorename>/', views.export_to_excel, name='export2excel'),
]
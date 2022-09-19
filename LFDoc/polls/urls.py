from django.urls import path, re_path
from . import views
from .views import HomeView

app_name = 'polls'
urlpatterns = [
	#path('', views.index, name='index'),
	path('', HomeView.as_view(), name='home'),
	re_path(r'^question/(?P<question_id>[\d]+)/$', views.detail, name='detail'),
	re_path(r'^question/(?P<question_id>[\d]+)/vote/', views.vote, name='vote'),
	re_path(r'^question/(?P<question_id>[\d]+)/result/', views.result, name='result'),
	path('addquestion/', views.add_question, name='addquestion'),
]
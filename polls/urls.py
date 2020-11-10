from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # /polls
    path('<int:question_id>/', views.detail, name='details'), #/polls/3/
    path('<int:question_id>/results/', views.results, name='results'), #/polls/3/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/3/vote/
]

# ten napis sie wyswietla gdy jestem w moim branchu 'lukasz'
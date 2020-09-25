from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # exemple: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # exemple: /polls/specifices/5/    specifices est ajouter pour que l'url soit plus logique à comprendre mais il n'est pas nécessaire
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # exemple: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    
    # exemple: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
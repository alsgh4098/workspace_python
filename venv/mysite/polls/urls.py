# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

########################## polls url
# 목차

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_def, name='index_url'),
    path('<int:question_id>/detail/', views.detail_def, name='detail_url'),
    path('<int:question_id>/<int:choice_id>/<int:cnt>/results/', views.results_def, name='results_url'),
    path('<int:question_id>/<int:choice_id>/<int:cnt>/vote/', views.vote_def, name='vote_url')
]

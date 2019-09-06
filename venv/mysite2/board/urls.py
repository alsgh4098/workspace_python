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
    path('form/', views.board_form_def, name='form_url'),
    path('list/', views.board_list_def, name='list_url'),
    path('save/', views.board_save_def, name='save_url'),
    path('<int:id>/detail/', views.board_detail_def, name='detail_url'),
    path('<int:id>/delete/', views.board_delete_def, name='delete_url'),
    path('<int:id>/update/', views.board_update_def, name='update_url')
]



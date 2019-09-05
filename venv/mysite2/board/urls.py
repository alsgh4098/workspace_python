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
    path('form/', views.board_form_def, name='form_url'),
    path('list/', views.board_list_def, name='list_url'),
]

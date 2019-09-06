"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('board/', include('board.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# < h1
# style = "width: 100%; height: 200px; font-size: 20px; line-height: 18px; border: 1px solid #dddddd; padding: 20px;" >
# 제목: {{KEY_DETAIL
# .0
# .1}}
# < / h1 >
#
# < pre
# style = "width: 100%; height: 200px; font-size: 20px; line-height: 18px; border: 1px solid #dddddd; padding: 20px;" >
# 내용:
# < / pre >

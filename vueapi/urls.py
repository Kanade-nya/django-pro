from django.urls import path
from . import views
app_name = 'vueapi'
urlpatterns = [
    path('upload/goodsinfo',views.goodInfo,name='goodsinfo')
]
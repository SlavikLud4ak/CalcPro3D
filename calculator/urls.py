from django.contrib import admin
from django.urls import path, include
from calculator import views


urlpatterns = [
    path('', views.GenSetting, name='generalsettings'),
    path('addsetting',views.AddGenSetting, name='addsetting'),
    path('editsetting',views.EditGenSetting, name='editsetting'),
    path('updsetting/<str:id>',views.UpdGenSetting, name='updsetting'),
    path('delsetting/<str:id>',views.DelGenSetting, name='delsetting'),
]
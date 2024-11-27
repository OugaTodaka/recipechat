from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path("",views.FavoriteView.as_view(),name="favorite"),
    path("<int:chat_id>/add/",views.favorite_add,name='add'),
    path("<int:favorite_id>/delete/",views.favorite_delete,name='delete'),
]

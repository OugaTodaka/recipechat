from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Favorite
from chat.models import Chat
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class FavoriteView(LoginRequiredMixin,ListView):
    template_name = "favorite/favorite.html"
    model = Favorite
    login_url = reverse_lazy('user:signin')
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by("favo_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def favorite_add(request,chat_id):
    chat = Chat.objects.get(id=chat_id)
    Favorite.objects.create(user=request.user,
                            title=chat.detail,
                            link=chat.link,
                            img_link=chat.img_link
                            )
    return HttpResponseRedirect(reverse('chat:chat'))


def favorite_delete(request,favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.is_delete = 1
    favorite.save()
    return HttpResponseRedirect(reverse('favorite:favorite'))

from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Favorite

class FavoriteView(ListView):
    template_name = "favorite/favorite.html"
    model = Favorite
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by("favo_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

def favorite_delete(request,favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.is_delete = 1
    favorite.save()
    return HttpResponseRedirect(reverse('favorite:favorite'))

from django.views.generic import ListView
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
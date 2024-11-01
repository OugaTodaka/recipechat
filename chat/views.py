from django.views.generic import FormView
from .models import Chat
from django.urls import reverse_lazy
from .forms import ChatForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class ChatView(LoginRequiredMixin,FormView):
    template_name = "chat/chat.html"
    success_url = reverse_lazy('chat:chat')
    form_class = ChatForm

    def form_valid(self,form):
        chat = form.save(commit=False)
        chat.user = self.request.user
        chat.link = None
        chat.img_link = None
        chat.is_system = False
        chat.send_at = timezone.now()
        chat.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['chatdata'] = Chat.objects.filter(user=self.request.user).order_by("send_at")
            return context






from django.views.generic import FormView
from .models import Chat

class ChatView(FormView):
    template_name = "chat/chat.html"
    model = Chat
    def get_queryset(self):
        return Chat.objects.filter(user=self.request.user).order_by("send_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    def form_valid(self, form):


from django.views.generic import FormView
from .models import Chat
from django.urls import reverse_lazy
from .form import ChatForm

class ChatView(FormView):
    template_name = "chat/chat.html"
    success_url = reverse_lazy('')
    form_class = ChatForm
#     def get_queryset(self):
#         return Chat.objects.filter(user=self.request.user).order_by("send_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    def form_valid(self,form):
        message = form.cleaned_data['chat']
        user = self.request.user.username
        detail = message






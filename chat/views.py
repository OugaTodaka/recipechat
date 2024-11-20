from django.views.generic import FormView
from .models import Chat
from django.urls import reverse_lazy
from .forms import ChatForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import datetime
import json

from time import sleep
from googleapiclient.discovery import build

GOOGLE_API_KEY          = "AIzaSyBAg-3ihff7VmTLuwrSkUodmys144Rd8_g"
CUSTOM_SEARCH_ENGINE_ID = "a65cb3a84db0d4e35"

class ChatView(LoginRequiredMixin,FormView):
    template_name = "chat/chat.html"
    success_url = reverse_lazy('chat:chat')
    form_class = ChatForm
    login_url = reverse_lazy('user:signin')

    def form_valid(self,form):
        chat = form.save(commit=False)
        chat.user = self.request.user
        chat.link = None
        chat.img_link = None
        chat.is_system = False
        chat.send_at = timezone.now()
        chat.save()
        target_keyword = chat.detail + " レシピ"
        sys_response = getSearchResponse(target_keyword)
        result = []
        for entry in sys_response.get("items", []):
            title = entry.get("title")
            link = entry.get("link")
            og_image = None
            metatags = entry.get("pagemap", {}).get("metatags", [])
            for tag in metatags:
                if "og:image" in tag:
                    og_image = tag["og:image"]
                    break
            result.append({"title": title, "link": link, "og:image": og_image})

        # 結果を表示
        print(result)
        for i in result:   
            Chat.objects.create(user = self.request.user,
                                detail = i['title'],
                                link = i['link'],
                                img_link = i['og:image'],
                                is_system = True,
                                send_at = timezone.now()
                                )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['chatdata'] = Chat.objects.filter(user=self.request.user).order_by("send_at")
            return context

def getSearchResponse(keyword):

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 1
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            sleep(1)
            response.append(service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=6,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[0].get("startIndex")
        except Exception as e:
            print(e)
            break
    j_response = response[0]
    return j_response





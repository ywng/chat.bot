from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http.response import HttpResponse
# Create your views here.
class ChatBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '2318934571':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
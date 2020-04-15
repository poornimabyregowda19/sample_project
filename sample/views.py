from django.http import HttpResponse
from django.views import View
import os

class MyView(View):
    def get(self, request):
        # <view logic>
        data = os.getenv("SIMPLE_SETTINGS")
        return HttpResponse(data)
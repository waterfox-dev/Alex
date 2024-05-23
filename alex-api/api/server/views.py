from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

from api.settings import ALEX_URL

import qrcode


# Create your views here.
class ApiView :
    
    @staticmethod 
    def get_app_qr(request: HttpRequest, alex_link:str = ALEX_URL) -> HttpResponse:
        img = qrcode.make(alex_link) 
        response = HttpResponse(content_type="image/png", status=200)
        img.save(response, "PNG")
        return response
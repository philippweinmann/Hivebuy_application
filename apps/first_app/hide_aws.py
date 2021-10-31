from django.http import response
import requests
import boto3
from django.views.generic import View
from django.http.response import HttpResponse
import base64


class MediaDownloadView(View):

    def get(self, *args, **kwargs):
        image_url = 'https://hivebuyexercicebucket.s3.eu-central-1.amazonaws.com/bansky.jpg'
        response = requests.get(url=image_url)
        uri = ("data:" +
               response.headers['Content-Type'] + ";" +
               "base64," + str(base64.b64encode(response.content).decode("utf-8")))
        base64_image = uri
        return base64_image

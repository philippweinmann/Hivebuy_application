'''
import requests
import re
from django.http import HttpResponse


def proxy_file():
    # Set up the image URL and filename
    image_url = 'https://hivebuyexercicebucket.s3.eu-central-1.amazonaws.com/bansky.jpg'
    file_location = download_media(image_url)
    return file_location


def download_media(url):
    r = requests.get(url, allow_redirects=True)
    if url.find('/'):
        filename = url.rsplit('/', 1)[1]
        file_location = "ressources/" + filename
        open(file_location, 'wb').write(r.content)
        return file_location
    
'''

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

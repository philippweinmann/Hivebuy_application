from django.shortcuts import render
from .hide_aws import MediaDownloadView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def show_bansky(request):
    res = "Image loaded through S3: </br>"
    res += show_bansky_s3()
    res += '<br/>'
    res += "Image loaded through django backend<br/>"
    res += show_bansky_hidden()
    res += '<br/>'
    res += "Image loaded through django backend if you are authenticated: <br/>"
    if request.user.is_authenticated:
        res += show_bansky_hidden_with_user_auth(request)
    else:
        res += '<br/>'
        res += "Sorry you cannot access this element if you are not logged in"
    return HttpResponse(res)


def show_bansky_s3():
    image_url = 'https://hivebuyexercicebucket.s3.eu-central-1.amazonaws.com/bansky.jpg'
    res = '<img src=' + image_url + ' alt="bansky image" width="512">'
    return res


def show_bansky_hidden():
    mediaDownloadView = MediaDownloadView()
    base_64_image = mediaDownloadView.get()
    res = '<img src=' + base_64_image + ' alt="bansky image" width="512">'
    res += '<br/>'
    return res


@login_required
def show_bansky_hidden_with_user_auth(request):
    return show_bansky_hidden()

from django.shortcuts import render
import datetime
from .models import Dreamreal

# Create your views here.

from django.http import HttpResponse


def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name+"<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)

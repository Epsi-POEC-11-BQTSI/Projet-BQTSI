"""
Imports non utilisés et mis en commentaires pour la note pylint
from datetime import datetime
from django.http import HttpResponse
"""
from datetime import datetime
from django.shortcuts import render


def index(request):
    """ Renvoie à la page index le user et la date.???? Ce code est-il encore utile????"""
    # render (request, "templates")
    return render(request, "index.html", context={"user": "Zoely", "date": datetime.now()})

# Django placeholder file
# This ensures Django is detected in GitHub language stats.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Hostel MiniSite")

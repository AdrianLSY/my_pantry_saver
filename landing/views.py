from django.http import HttpResponse
from django.template import loader
 
# Our main landing mage at '/'
def landing(request):
    # return our template
    return HttpResponse(loader.get_template('landing.html').render())
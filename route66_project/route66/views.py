

# importing the respons function

from django.http import HttpResponse

# defining the reponse on each of the paths

def index(request):
    return HttpResponse("Please follow one of the following routes: mycity/ myeats/")

def mycity(request):
    return HttpResponse("Memphis All Day!!")

def myeats(request):
    return HttpResponse("Railgarten")

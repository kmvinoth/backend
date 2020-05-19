from django.http import HttpResponse


def index(request):
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    return HttpResponse("Hello, world. You're at Home page.")
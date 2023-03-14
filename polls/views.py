from django.http import HttpResponse

def index(request):
    return HttpResponse("It ain't about how hard you hit.")

def potato(request):
    return HttpResponse("Congratulations!! You've found my potato.")
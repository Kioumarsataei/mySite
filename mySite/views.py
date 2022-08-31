from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("<h1>Http-Test</h1>")

def json_test(request):
    return JsonResponse({"name":"Kioumars"})
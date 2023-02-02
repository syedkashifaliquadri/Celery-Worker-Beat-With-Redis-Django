from django.shortcuts import HttpResponse
from celery_with_django.tasks import test_func


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

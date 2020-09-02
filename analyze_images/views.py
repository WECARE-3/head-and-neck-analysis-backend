from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        print(images[0].read())
        print(type(images[0]))
        print(images[1].read())
        print(type(images[1]))

        return HttpResponse('Success')
    else:
        return HttpResponse(status=404)

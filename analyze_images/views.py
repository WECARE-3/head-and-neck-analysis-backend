from django.http import HttpResponse
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            return HttpResponse(request.FILES['image'])
        else:
            return HttpResponse('Form is not valid')
    else:
        return HttpResponse(status=404)

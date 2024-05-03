from django.shortcuts import render
from django.http import HttpResponse
import random

def captcha_form(request):
    if request.method == 'POST':
        captcha_input = request.POST.get('captcha_input')
        captcha_number = request.POST.get('captcha_number')
        if captcha_input == captcha_number:
            return HttpResponse("CAPTCHA введена вірно")
        else:
            error_message = "Спробуйте ще раз."
            captcha_number = random.randint(1000, 9999)
            return render(request, 'index.html', {'error_message': error_message, 'captcha_number': captcha_number})
    else:
        captcha_number = random.randint(1000, 9999)
        return render(request, 'index.html', {'captcha_number': captcha_number})

# Create your views here.

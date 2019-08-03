from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail


def hello(request):
    return HttpResponse("hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def contact(request):
    # 创建表单对象
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
        else:
            form = ContactForm(
                initial={'subject': 'I love your site!'}
            )

        return render(request, 'contact_form.html', {'form': form})


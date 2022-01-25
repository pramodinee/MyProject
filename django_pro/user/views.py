from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm


from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


##################################################################
####################index#######################################
def index(request):
    return render(request, 'user/index.html',{'title':'index'})

########################################################################
########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            #########################mail####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'hello', 'from@example.com', 'to@emaple.com'
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'reqister here'})

###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})

def forgot(request):
    if request.POST:

        # email = request.POST.get("email")
        # print (email)
        # user = authenticate(request, email=email)
        # print (user)
        # if (not user):
        #     print ("No user")
        #     return render(request, 'user/forgot.html')
        # else:
        return render(request, 'user/recovery_password.html')
    else:
        return render(request, 'user/forgot.html')





def reset (request):
    if request.POST:

        current_password = request.POST.get('current_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        user = authenticate(request, password1=current_password)
        # email = request.POST.get("email")
        # print (email)
        # user = authenticate(request, email=email)
        # print (user)
        # if (not user):
        #     print ("No user")
        #     return render(request, 'user/forgot.html')
        # else:
        return render(request, 'user/recovery1_password.html')
    else:
        return render(request, 'user/reset.html')



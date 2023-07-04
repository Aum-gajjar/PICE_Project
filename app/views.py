from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# For sending forgot password mail
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
import uuid

# For change password
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# For database amd scraping
from app.models import Product
from app.scrapy import productinfo

# Create your views here.

def index(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio.html')

def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login is successfull")
            return redirect('/')
        else:
            messages.error(request, "Invalid details! Please try again")
            return redirect('/login')


    return render(request,'login.html')

def handlesignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password != confirmpassword:
            messages.error(request, "Password is Incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.warning(request, "Username is already taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is taken")
                return redirect('/signup')
            # if User.objects.get("email"):
            #     if "@gmail.com" in 'email':
            #         pass
            #     else:
            #         messages.warning(request, "Email is invalid")
            #         return redirect('/signup')
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        # ftoken = str(uuid.uuid4())
        # profile_obj = Profile.objects.create(user=myuser)
        # profile_obj.save()

        messages.success(request, "Signup was Successfull Please login!")
        return redirect('/login')
    return render(request,'signup.html')

def handlelogout(request):
    logout(request)
    messages.info(request, "Logout was Successfull")
    return redirect('/login')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username.')
            return redirect('forgot_password')

        # Generate a random password reset token
        token = get_random_string(length=32)

        # Save the token to the user's profile
        # profile = user.profile
        # profile.forget_password_token = token
        # profile.save()

        # Send the password reset email
        subject = 'Password Reset Request'
        message = f'Hi {user.username},\n\nYou recently requested a password reset for your account.\n\nPlease click the following link to reset your password:\n\nhttp://{request.get_host()}/reset_password/uidb64={user}/token={token}\n\nIf you did not request this reset, please ignore this email and your password will remain unchanged.\n\nThanks,\nThe PICE Team'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])

        messages.success(request, 'Password reset email sent.')
        return redirect('/login')

    return render(request, 'forgot-password.html')


def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and PasswordResetTokenGenerator().check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password and confirm_password and password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, 'Your password was successfully updated. You can now log in with your new password.')
                return redirect('/login')
            else:
                messages.error(request, 'Please enter a valid password.')
        return render(request, 'reset_password.html')
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('forgot_password')


def search(request):
    if request.method == 'POST':
        channel = request.POST.get('channel', '')
        gtin_asin_str = request.POST.get('gtin_asin', '')
        gtin_asin_list = [s.strip() for s in gtin_asin_str.split(', ')]  # split by comma and strip whitespace
        valid_gtin_asin_list = []
        invalid_gtin_asin_list = []
        for gtin_asin in gtin_asin_list:
            if gtin_asin.isnumeric() and len(gtin_asin) in [8, 12, 13, 14] or (len(gtin_asin) == 10 and gtin_asin[:2] == 'B0'):
                valid_gtin_asin_list.append(gtin_asin)
            elif  gtin_asin.isnumeric() and len(gtin_asin) in [8, 12, 13, 14] or (len(gtin_asin) == 12 and gtin_asin[:3] == 'SDL'):
                valid_gtin_asin_list.append(gtin_asin)
            elif len(gtin_asin) in [5,6]:
                valid_gtin_asin_list.append(gtin_asin)
            elif len(gtin_asin) == 8 and gtin_asin[:1] == 'G' :
                valid_gtin_asin_list.append(gtin_asin)
            else:
                invalid_gtin_asin_list.append(gtin_asin)
        if valid_gtin_asin_list:
            # Redirect to the success page with valid GTIN/ASIN numbers

            productinfo(channel,valid_gtin_asin_list)

            # Retrieve products from the database based on gtin_asin and channel
            products = Product.objects.filter(asingtin__in=valid_gtin_asin_list)

            messages.success(request, "for "+gtin_asin_str+" from "+channel+".")
            return render(request, 'product-info.html', {'gtin_asin_list': valid_gtin_asin_list, 'channel': channel, 'products':products})
        else:
            # Show an error message on the same page for invalid GTIN/ASIN numbers
            messages.error(request, "Invalid GTIN/ASIN/Product numbers: {}".format(", ".join(invalid_gtin_asin_list)))
            return render(request, 'search.html', {'gtin_asin': gtin_asin_str})
    return render(request, 'search.html')

def productInfo(request):
    # Retrieve products from the database based on gtin_asin and channel

    return render(request, 'product-info.html')

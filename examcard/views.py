from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import qrcode
import json
from qr_code.qrcode.utils import QRCodeOptions
from examcard.models import StudentProfile, Fee, Log,Report, Unit, StudentUnit
from examcard.forms import UserLoginForm, StudentProfileForm, UserRegisterForm, ReportForm, StudentUnitForm
# Create your views here.
import random
from examcard.decorators import anonymous_required, superuser_only

@login_required(login_url='login')
def add_unit(request):
    context = {}
    units = Unit.objects.all()
    context['units'] = units
    if request.method == "POST":
        form = StudentUnitForm(request.POST)
        if form.is_valid():
            unit_name = request.POST['student_unit']
            obj = form.save(commit=False)
            obj.profile_id = request.user.studentprofile.id
            obj.save()

            messages.success(request, f'The Unit {unit_name} was added succefully')
            return redirect('/profile/unit/')
        else:
            return redirect('/profile/unit/')
    else:
        form = StudentUnitForm()
        context['form'] = form
    return render(request, 'pages/unit.html', context)

@login_required(login_url='login')
def home_dashboard(request):
    try:
        fee_qs = Fee.objects.filter(profile_id = request.user.studentprofile.id)
        return render(request, 'pages/home.html', {'fee_qs':fee_qs})
    except ObjectDoesNotExist:
        return redirect('/profile/create/')
        
    


@login_required(login_url='login')
def exam_card(request):
    try:
        exam_card_number = random.randint(245,400000)
        stude_unit = StudentUnit.objects.filter(profile_id = request.user.studentprofile.id)
        fullname = f'{request.user.studentprofile.first_name} {request.user.studentprofile.sirname} {request.user.studentprofile.last_name}'
        qr_metadata = f'{exam_card_number} {fullname} {request.user.studentprofile.adm_number}'
        context = dict(
            my_options=qr_metadata,
            exam_card_number = exam_card_number,
            stude_unit = stude_unit,
        )
    except ObjectDoesNotExist:
        messages.success(request, f'Create Your Profile {request.user.username} !!!')
        return redirect('/profile/create/')

    return render(request, 'pages/examcard.html', context=context)

@staff_member_required(login_url='admin:login')
@login_required(login_url='login')
def log_list(request):
    log_qs = Log.objects.all()
    context = {}
    context['log_qs'] = log_qs
    if request.method == "POST":
        form = Report.objects.create(
            user = request.user,
            student = request.POST['student'],
            message = request.POST['message'],
        )
        
        form.save()
        
        # obj.save()
        return redirect('/profile/scan/')
    else:
        form = ReportForm()
        context['form'] = form
    return render(request, 'pages/loglist.html', context)
@staff_member_required(login_url='admin:login')
@login_required(login_url='login')
def report_list(request):
    report_list_qs = Report.objects.filter(user_id = request.user.id).order_by('-id')
    return render(request, 'pages/report_list.html', {'report_list_qs':report_list_qs})
    
@staff_member_required(login_url='admin:login')
@login_required(login_url='login')
def make_report(request, id):
    context = {}
    if request.method == "POST":
        form = Report.objects.create(
            user = request.user,
            student = request.POST['student'],
            message = request.POST['message'],
        )
        
        form.save()
        
        # obj.save()
        return redirect('/profile/scan/')
    else:
        log_qs = Log.objects.get(pk = id)
        form = ReportForm()
        context['form'] = form
        context['log_qs'] = log_qs
    return render(request, 'pages/report.html', context)

@staff_member_required(login_url='admin:login')
@login_required(login_url='login')
def exam_card_scanner(request):
    context = {}
    if request.method == "POST":
        qs = request.POST['q'].split()[4:][0]
        # print(qs)
        profile_qs = StudentProfile.objects.get(adm_number = qs)
        fee_qs = Fee.objects.get(profile_id = profile_qs.id)
        log_save = Log.objects.create(
            user_id = request.user.id,
            profile_id = profile_qs.id,
            fee_id = fee_qs.profile_id,

        )
        log_save.save()
        # print(profile_qs.id)
        context['profile_qs'] = profile_qs
        context['fee_qs'] = fee_qs
        # create logs

        return render(request, 'pages/scan.html', context)
    else:
        return render(request, 'pages/scan.html', context)

def student_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)

            messages.success(request, f'login was Success {username} !!!')
            return redirect('/profile/')
        else:
            messages.success(
                request, f'login Error !!!! Provide Correct Username And Password')
    else:
        form = UserLoginForm()
    return render(request, 'pages/login.html', {'form': form})


def student_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/profile/')  # will change to dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form})


@login_required(login_url='login')
def student_create_profile(request):
    context = {}
    if request.method == 'POST':
        profileform = StudentProfileForm(request.POST, request.FILES)
        if profileform.is_valid():

            profile_qs = StudentProfile.objects.filter(user_id=request.user.id)
            if profile_qs.count() == 1:
                user = profile_qs.first()
                messages.success(
                    request, f'{request.user.studentprofile.first_name} Had Created Profile Successfully !')
                return redirect('/profile/create/')
            else:
                obj = profileform.save(commit=False)
                obj.user_id = request.user.id
                obj.save()
                messages.success(
                    request, f'{request.user.studentprofile.first_name} Created Successfully !')
                return redirect('/profile/')
        else:
            profileform = StudentProfileForm()
            context['profileform'] = profileform
            messages.success(
                request, f'{request.user.username} fill all the fields correctly!')
            return redirect('/profile/create/')
    else:
        profileform = StudentProfileForm()
        context['profileform'] = profileform
    return render(request, 'pages/create_profile.html', context)

def user_log_out(request):
    logout(request)
    return redirect('/profile/')
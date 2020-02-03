from django.shortcuts import render, redirect
from .forms import AutogenForm
import qrcode
from qr_code.qrcode.utils import QRCodeOptions
from . models import Autogen
# Create your views here.
def hacker_view(request):
    hacker_context = {}
    # {% qr_from_text my_options size="m" image_format="png" error_correction="L"  %}
    
    if request.method == 'POST':
        hacker_form = AutogenForm(request.POST, request.FILES)
         
        if hacker_form.is_valid():
            studentname = hacker_form.cleaned_data.get('student_full_name')
            examcardno = hacker_form.cleaned_data.get('exam_card_number')
            admno = hacker_form.cleaned_data.get('adm_number')
            
            hacker_obj = hacker_form.save(commit = False)
            hacker_form.save()
            qr_metadata = f'{examcardno}-{studentname}-{admno}'
            context = dict(
                my_options = qr_metadata,
                studentname = studentname,
                examcardno = examcardno,
                admno = admno,
            )
            return render(request, 'myview.html', context=context)
        else:
            return redirect('/')
    else:
        hacker_form = AutogenForm()
        hacker_context['hacker_form'] = hacker_form
    return render(request, 'hack.html', hacker_context)

def myview(request):
    # Build context for rendering QR codes.
    hack_qs = Autogen.objects.get(exam_card_number = 124124)

    qr_metadata = f'{hack_qs.exam_card_number}-{hack_qs.student_full_name}-{hack_qs.adm_number}'

    context = dict(
        my_options = qr_metadata,
    )

    # Render the view.
    return render(request, 'myview.html', context=context)
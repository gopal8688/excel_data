from django.shortcuts import render, redirect
from .models import File_input, Save_data
from django.contrib import messages
from django.http import HttpResponse
import os
import pandas as pd


def upload_file(request):
    if request.method == "POST":
        file = request.FILES['files']
        File_input(file=file).save()
        messages.success(request, 'file is saved')
        return redirect('save')
    else:
        return render(request, 'file.html')


def show_data(request):
    b = File_input.objects.all()
    qs = Save_data.objects.all()
    if qs:
        return render(request, 'show_data.html', {'qs': qs})
    for x in b:
        df = pd.read_excel(x.file)
        for x in df.values:
            q, w, e, r, t, y, u = x
            Save_data(no=q, product=w, proposal_no=e, inwardnumber=r, currentworkstep=t, names=y,
                      customer_names=u).save()

    return render(request, 'show_data.html', {'qs': Save_data.objects.all()})


def update(request):
    id = request.GET.get('id')
    qs = Save_data.objects.get(id=id)
    return render(request, 'update.html', {'qs': qs})


def delete(request):
    id = request.GET.get('id')
    print(id)
    Save_data.objects.filter(id=id).delete()
    return redirect('show_data')


def updated(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = request.POST.get('c')
    d = request.POST.get('d')
    e = request.POST.get('e')
    f = request.POST.get('f')
    g = request.POST.get('g')
    Save_data.objects.filter(id=request.POST.get('id')).update(no=a, product=b, proposal_no=c, inwardnumber=d,
                                                               currentworkstep=e, names=f, customer_names=g)
    return redirect('show_data')

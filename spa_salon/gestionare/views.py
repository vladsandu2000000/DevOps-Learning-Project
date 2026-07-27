from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Pacient, Tratament
from .forms import PacientForm, TratamentForm

def home(request):
    return render(request, 'gestionare/home.html')

def lista_pacienti(request):
    pacienti = Pacient.objects.all()
    return render(request, 'gestionare/lista_pacienti.html', {'pacienti': pacienti})

def adauga_pacient(request):
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm()
    return render(request, 'gestionare/adauga_pacient.html', {'form': form})

def editeaza_pacient(request, id):
    pacient = get_object_or_404(Pacient, CodPacient=id)
    if request.method == 'POST':
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm(instance=pacient)
    return render(request, 'gestionare/adauga_pacient.html', {'form': form})

def sterge_pacient(request, id):
    pacient = get_object_or_404(Pacient, CodPacient=id)
    if request.method == 'POST':
        pacient.delete()
        return redirect('lista_pacienti')
    return render(request, 'gestionare/confirmare_stergere_pacient.html', {'pacient': pacient})

def lista_tratamente(request):
    tratamente = Tratament.objects.all()
    return render(request, 'gestionare/lista_tratamente.html', {'tratamente': tratamente})

def adauga_tratament(request):
    if request.method == 'POST':
        form = TratamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamente')
    else:
        form = TratamentForm()
    return render(request, 'gestionare/adauga_tratament.html', {'form': form})

def editeaza_tratament(request, id):
    tratament = get_object_or_404(Tratament, CodTratament=id)
    if request.method == 'POST':
        form = TratamentForm(request.POST, instance=tratament)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamente')
    else:
        form = TratamentForm(instance=tratament)
    return render(request, 'gestionare/adauga_tratament.html', {'form': form})

def sterge_tratament(request, id):
    tratament = get_object_or_404(Tratament, CodTratament=id)
    if request.method == 'POST':
        tratament.delete()
        return redirect('lista_tratamente')
    return render(request, 'gestionare/confirmare_stergere_tratament.html', {'tratament': tratament})

def lista_diagnoze(request):
    diagrame = Tratament.objects.values('Diagnoza').annotate(numar_pacienti=Count('Diagnoza'))
    return render(request, 'gestionare/lista_diagnoze.html', {'diagrame': diagrame})

from django.shortcuts import render, redirect
from .models import Carro

# Create your views here.

def home(request):
    carros = Carro.objects.all()
    return render(request, "index.html", {"carros": carros})

def salvar(request):
    vplaca = request.POST.get("placa")
    vmodelo = request.POST.get("modelo")
    vmarca = request.POST.get("marca")
    vcor = request.POST.get("cor")

    Carro.objects.create(placa=vplaca, modelo=vmodelo, marca=vmarca, cor=vcor)
    carros = Carro.objects.all()

    return render(request, "index.html", {"carros": carros})

def alterar(request, id):
    carro = Carro.objects.get(id=id)
    return render(request, "atualizar.html", {"carro":carro})

def atualizar(request, id):
    #pego os novos campos
    vplaca = request.POST.get("placa")
    vmodelo = request.POST.get("modelo")
    vmarca = request.POST.get("marca")
    vcor = request.POST.get("cor")

    #pego a pessoa do banco
    carro = Carro.objects.get(id=id)

    carro.placa = vplaca
    carro.modelo = vmodelo
    carro.marca = vmarca
    carro.cor = vcor

    carro.save()
    return redirect(home)

def deletar(request, id):
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect(home)

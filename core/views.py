from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from .models import *


# Create your views here.

def root(request):
    return redirect(crud_view)
    #if not request.user.is_authenticated:
    #    return redirect(login_view)
    #return redirect(painel)

def crud_view(request):
    avisos = Aviso.objects.all()
    return render(request, "crud.html", {"avisos" : avisos})

def crud_create(request):
    if request.method == 'POST':
        Aviso.objects.create(
            titulo_aviso=request.POST['titulo_aviso'],
            descricao=request.POST['descricao'],
            tipo_destinatario=request.POST['tipo_destinatario']
        )
    return redirect(crud_view)

@require_POST
def crud_delete(request, id_aviso):
    try:
        aviso = Aviso.objects.get(id_aviso=id_aviso)
        aviso.delete()

        return JsonResponse({'success': True})

    except Aviso.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Aviso não encontrado.'}, status=404)

@require_POST
def crud_update(request, id_aviso):
    try:
        aviso = Aviso.objects.get(id_aviso=id_aviso)

        titulo = request.POST.get("titulo_aviso_upd")
        descricao = request.POST.get("descricao_upd")
        tipo_destinatario = request.POST.get("tipo_destinatario_upd")

        if not titulo or not descricao or not tipo_destinatario:
            return JsonResponse({
                'success': False,
                'error': 'Preencha todos os campos.'
            }, status=400)

        aviso.titulo_aviso = titulo
        aviso.descricao = descricao
        aviso.tipo_destinatario = tipo_destinatario
        aviso.save()

        return JsonResponse({
            'success': True
        })

    except Aviso.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Aviso não encontrado.'
        }, status=404)


def register_view(request):
    #User = get_user_model()

    #name = request.POST.get("name")
    #email = request.POST.get("email")
    #cpf = request.POST.get("cpf")
    #curso = request.POST.get("curso")
    #turma = request.POST.get("turma")


    #user = User.objects.create(
    #    name=name,
    #    email=email,
    #    first_name=name.split(' ')[0],
    #   password=make_password(),
    #)

    return render(request, 'user/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(painel)

    return render(request, "user/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect(root)

@login_required
def painel(request):
    return render(request, "panels/base.html")

from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela para banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #exibir todos os usuarios ja cadastradosem uma página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a págna lstagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)
   


from django.shortcuts import render,redirect


# Create your views here.
def index(request):
        return render(request,'escola/index.html')


def cadastrar(request):
   return render(request,'escola/cadastro_aluno.html')


def teste(request):
      return render(request, "escola/home.html")
 

def teste_copy(request):
      return render(request, "escola/fomu.html")

def andament(request):
      return render(request, "escola/andamento.html")

def pedidos(request):
      return render(request, 'escola/pedidosadmin.html')

def menu(request):
      return render(request, 'escola/menuadmin.html')

def formuadmin(request): 
      return render(request, 'escola/formularioadmin.html')

def calendario(request):
      return render(request, 'escola/calendario.html')

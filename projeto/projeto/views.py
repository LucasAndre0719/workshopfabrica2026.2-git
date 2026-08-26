from django.http import HttpResponse

def teste_veiw(resquest):
    return HttpResponse ("ABA DE TESTES!")

def home (resquest):
    return HttpResponse ("<h1> BEM VINDO!! </h1>")
# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from random import randint

# NOTE: Ejemplo de hello world con método GET
@api_view(['GET'])
def hello_world(request):
    template = '<h1>Hello world Django APIs!</h1>' 
    return HttpResponse(template)

# NOTE: Ejemplo de hello world con método POST
@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_data(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "mi_parametro" enviada en la petición.
    '''
    template = f'<h1>{request.GET.get("mi_parametro")} - Otro param: {request.GET.get("otro_param")}</h1>'
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)



@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def welcome(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "nombre" enviada en la petición.
    '''
    nombre = request.GET.get("nombre") or ""
    apellido = request.GET.get("apellido") or ""
    text = f"{nombre} {apellido}" if nombre or apellido else "desconocido! La próxima probá pasando los parámetros en la URL así te saludamos"
    template = f'<h1>Bienvenido al e-Commerce de comics de Marvel, {text}!</h1>'
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)


@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def grade_homework(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "grade" enviada en la petición.
    '''
    calificacion = request.GET.get("grade") or 0
    
    template = f'<h1>Has calificado mi tarea con un {float(calificacion)}! Muchas gracias!</h1>' if float(calificacion) > 8.9 else "<h1>Parámetro no reconocido, inténtelo nuevamente, quizás probando con otro número.</h1>"
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)


@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def guess_number(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "guess" enviada en la petición.
    '''
    number = randint(0,100)
    guess = request.GET.get("guess")
    
    template = f'<h1>Has adivinado! El número correcto era: {number}!</h1>' if guess.isdigit() and int(guess) == number else f"<h1>Número incorrecto, no has adivinado. El número era {number}.</h1>"
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)







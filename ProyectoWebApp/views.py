from django.shortcuts import render, HttpResponse
from datetime import date
from ProyectoWebApp.models import Resultados



def resultados(request):
    misanimalitos={"0":"Delfin","00":"Ballena","1":"Carnero","01":"Carnero","2":"Toro","02":"Toro",
                   "3":"Ciempies","03":"Ciempies","4":"Alacran","04":"Alacran","5":"Leon","05":"Leon",
                   "6":"Rana","06":"Rana","7":"Perico","07":"Perico","8":"Raton","08":"Raton","9":"Aguila","09":"Aguila",
                   "10":"Tigre","11":"Gato","12":"Caballo","13":"Mono","14":"Paloma","15":"Zorro","16":"Oso",
                   "17":"Pavo","18":"Burro","19":"Chivo","20":"Cerdo","21":"Gallo","22":"Camello","23":"Cebra",
                   "24":"Iguana","25":"Gallina","26":"Vaca","27":"Perro","28":"Zamuro","29":"Elefante","30":"Caiman",
                   "31":"Lapa","32":"Ardilla","33":"Pescado","34":"Venado","35":"Jirafa","36":"Culebra"
                   }
    hoy1=date.today()
    resultados=Resultados.objects.filter(fecha_lot=hoy1)
    #return render(request, "Inicio.html", {"nombre_usuario": p1.nombre,"nombre_apellido": p1.apellido, "la_lista": lista})
    return render(request, "ProyectoWebApp/resultados.html", {'resultados':resultados, 'diccionario':misanimalitos})

def home(request):
    
    return render(request, "ProyectoWebApp/home.html")

def descarga(request):
    
    return render(request, "ProyectoWebApp/descarga.html")

def quienes(request):
    
    return render(request, "ProyectoWebApp/quienes.html")


#Programa para acceder a la API rest de pokemon online
import requests #importamos librerias
import matplotlib.pyplot as plt
import matplotlib.image as img
pokemon=input("Ingrese el nombre de un pokemon: ") #Pedimos al usuario ingrese el nombre de un pokemon
url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"#API con el JSON de los poquemones
respuesta=requests.get(url) #Guardamos el resultado de nuestra solicitud en respuesta
if respuesta.status_code != 200: #Cuando un status__code de una petición es 200 quiere decir que todo ok
    print("No se encontro el pokemon")
    exit()
imagennormal=img.imread(respuesta.json()['sprites']['front_default'])#Leemos la imagen que se encuentra dentro del JSON en sprites, front_default
imagenback=img.imread(respuesta.json()['sprites']['back_default'])#Lo mismo que la instruccion de arriba, solo que ahora el back
imagenfrontgold=img.imread(respuesta.json()['sprites']['versions']['generation-ii']['gold']['front_default'])#Lo mismo, solo que ahora version gold
imagenbackgold=img.imread(respuesta.json()['sprites']['versions']['generation-ii']['gold']['back_default'])#Ahora version gold la vista back
imagearray=[imagennormal,imagenback,imagenfrontgold,imagenbackgold]#Array donde colocamos todas nuestras imagenes leidas
titlearray=['Vista frontal','Vista posterior','Frontal versión gold','Posterior versión gold']#Array titulos de imagenes leidas
for i in range(0,len(imagearray)):#Creamos nuestro subplot para colocar nuestras imagenes
    plt.subplot(2,2,i+1)
    plt.xticks([]),plt.yticks([])
    plt.xlabel(titlearray[i])
    plt.imshow(imagearray[i])
plt.suptitle(respuesta.json()['name'])#Ponemos de nombre a nuestro suptitle el nombre del pokemon
plt.show()#Mostamos nuesto plot

"""
En este ejercicio se esta consumiendo un repositorio de la pagina web omdb para la consulta de titulos 
de peliculas 
"""
from llaves import llaves
import requests
import json

if __name__=='__main__':
  llaves = llaves()
  #creamos un diccionarios con los parametro necesarios para hacer la consulta
  argum = {'t':'Mamamia','plot':'full'}
  url ='http://www.omdbapi.com'
  print(llaves)
  args = llaves.update(argum)

  respuesta = requests.get(url,params=args) # respuesta del servidor 
  # print(respuesta) imprime el estatus dependiendo del numero se sabes is el servidor esta activo o no 
  # 
  print(respuesta.url)
  if respuesta.status_code == 200:
    
    # de esta forma puedo obtener la informacion contenida en el json y buscarlo directamente por su clave 
    json_conenido = json.loads(respuesta.text)
    img_web = json_conenido['Poster']
    print(img_web)

    contenido = respuesta.content  # se guarda todoe el contenido de la pagina o en este caso la respuesta a la pecition
    file = open('pagina5.html','wb')
    file.write(contenido)
    file.close()
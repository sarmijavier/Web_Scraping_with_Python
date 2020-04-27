import requests
from bs4 import BeautifulSoup
import urllib.request # guardar de manera sencilla las imagenes que utilizaremos


def run():

    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i)) #obtener informacion de los servidores
        # la url de la imagen
        soup = BeautifulSoup(response.content, 'html.parser')# parsiar el documento, el contenido que resive es html
        image_container = soup.find(id='comic')# encuentreo el nodo con la etiqueta de comic, referencia en el html de la pagina
        #contenedor de la etiqueta
        image_url = image_container.find('img')['src']# encontrar la etiqueta y acceder a la etiqueta src, que es donde esta la imagen

        image_name = image_url.split('/')[-1]# dividir la diagonales y acceder a la ultima posición
        print('DESCARGANDO...')
        urllib.request.urlretrieve('https:{}'.format(image_url),image_name)#guardar la imagen, necesita la url el tipo de transporte como https


if __name__ == '__main__':
    run()


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


class GraficaClase:
    pass




def getTopTen():


    listaDeGraficas = []


    URL = 'https://www.amazon.es/s?k=tarjeta+gr%C3%A1fica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&ds=v1%3A6yf73u5VHmCJmGOXrszSxvvw%2BtYGhzbr2Y%2FODunP5k4&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3QFPAFHSKURKU&qid=1663328816&rnid=1323854031&sprefix=tarjeta+gr%C3%A1fica%2Caps%2C85&ref=sr_st_review-rank'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    results = soup2.find_all("div",{"class":"s-result-item","data-component-type": "s-search-result"})
    for i in range(0,10):

        listaDeGraficas.append(GraficaClase())

        #NOMBRE
        name=results[i].h2.text
        #print(name)
        listaDeGraficas[i].nombre = name.replace('\n','')

        #VALORACION
        try:
            rating = results[i].find('i', {'class': 'a-icon'}).text
            #print(rating)
            listaDeGraficas[i].valoracion = rating.replace('\n','')
        except AttributeError:
            #print("Not rated")
            listaDeGraficas[i].valoracion = "-"
        #PRECIO
        try:
            price1 = results[i].find('span', {'class': 'a-price-whole'}).text
            listaDeGraficas[i].precio = price1.replace('\n','')
        except AttributeError:
            listaDeGraficas[i].precio = "-"



        try:
            auxSgColinerTipoRam = results[i].find_all('div', {'class': 'sg-col-inner'})
            for coliner in auxSgColinerTipoRam:

                #print(coliner)
                #print("FINCOLINER-------------------------------------------------------------")

                try:
                    tipoDeColiner = coliner.find('span', {"class":"a-color-secondary"}).text

                except:
                    tipoDeColiner = "No hay tipo coliner coorecto"
                    continue


                if("Tipo de RAM" in tipoDeColiner):#TIPO DE RAM
                    RAM = coliner.find('span', {"class":"a-text-bold"})
                    listaDeGraficas[i].ram = RAM.text.replace('\n','')
                elif("Tamaño de RAM" in tipoDeColiner):#Tamaño de RAM
                    tmnRAM = coliner.find('span', {"class":"a-text-bold"})
                    listaDeGraficas[i].tmnRam = tmnRAM.text.replace('\n','')

                elif ("Tarjeta gráfica" in tipoDeColiner):#Tarjeta gráfica
                    tarjeta = coliner.find('span', {"class": "a-text-bold"})
                    listaDeGraficas[i].tarjeta = tarjeta.text.replace('\n','')
                elif ("Velocidad Memoria" in tipoDeColiner):#Velocidad Memoria
                    velMem = coliner.find('span', {"class": "a-text-bold"})
                    listaDeGraficas[i].velMem = velMem.text.replace('\n','')




        except AttributeError:
            continue


    #price = soup2.find(id='priceblock_ourprice').get_text()

    #print(title)
    #print(price)
    return listaDeGraficas

# Press the green button in the gutter to run the script.


def generateTxt(list):

    textoImpreso = ""
    for i in list:
        textoImpreso+= str(list.index(i)+1) + ". " + i.nombre + "\n"
        textoImpreso += "*PRECIO " + i.precio + "\n"
        textoImpreso += "*VALORACION " + i.valoracion + "\n"
        textoImpreso += "*RAM " + i.ram + "\n"
        textoImpreso += "*TAMAÑO DE RAM " + i.tmnRam + "\n"
        textoImpreso += "*TARJETA " + i.tarjeta + "\n"
        textoImpreso += "*VELOCIDAD DE MEMORIA " + i.velMem + "\n"
        textoImpreso += "\n"
        textoImpreso += "\n"


    with open('mejoresGraficas.txt', 'x') as f:
        f.write(textoImpreso)

if __name__ == '__main__':
    print("main")
    topTen = getTopTen()
    generateTxt(topTen)





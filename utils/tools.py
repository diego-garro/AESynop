#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: tools.py
versión: 0.0.1

Este es un módulo para las herramientas que se necesitarán en el programa principal.
"""

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

def fecha_para_registro():
    """
    Esta función retorna la fecha a la cual es ejecutada.
    ---------------------------------
    No recibe ningún parámetro.
    ---------------------------------
    Retorna una fecha con formato %Y/%m/%d %H:%M:%S.
    Ejemplo: 2019/09/17 13:33:52
    """
    hoy = datetime.utcnow()
    return(datetime.strftime(hoy, '%Y/%m/%d %H:%M:%S'))

def registro_de_actividad(mensaje):
    """
    Esta función registra la actividad realizada justo antes de ser ejecutada y
    la almacena en el archivo log.txt
    ---------------------------------
    Recibe un parámetro:
    * mensaje: un objeto de tipo string, el mensaje que se escribirá en log.txt
    ---------------------------------
    No retorna ningún valor.
    """
    log = open("log.txt", "a")
    fecha = fecha_para_registro()
    print(mensaje.format(fecha))
    log.write(mensaje.format(fecha) + '\n')
    log.close()

def fecha_para_synops():
    """
    Esta función retorna la fecha en una tupla para la extracción de los sinópticos
    más recientes desde la web.
    -----------------------
    No recibe parámetros
    -----------------------
    Retorna una lista con año, mes, dia, hora y minuto actuales
    """
    hoy = datetime.utcnow()
    hoy_6h = hoy - timedelta(hours=6)
    tupla_hoy = (hoy.year, hoy.month, hoy.day, hoy.hour, hoy.minute)
    tupla_hoy_6h = (hoy_6h.year, hoy_6h.month, hoy_6h.day, hoy_6h.hour, hoy_6h.minute)
    return(tupla_hoy, tupla_hoy_6h)

def scraping_synops(url):
    """
    Esta función scrapea la página de Ogimet.com para obtener los últimos sinópticos
    emitidos por las estaciones terrestres.
    -----------------------
    Recibe un paŕametro:
    * url: un objeto de tipo string, la url de la página para extraer los sinópticos.
    -----------------------
    Retorna el METAR más actual como una cadena de texto si logra conectar a la url,
    si no, retorna una cadena vacía
    """
    f = open("texto_web.txt", 'w')
    req = requests.get(url)
    statusCode = req.status_code
    fecha = fecha_para_registro()
    if statusCode == 200:
        mensaje = "{}... Se accede correctamente a la página de Ogimet.com."
        registro_de_actividad(mensaje)
        html = BeautifulSoup(req.text, "html.parser")
        entrada = html.find('pre')
        f.write(str(entrada))
    else:
        mensaje = "{}... No se pudo acceder a la pádina de Ogimet.com."
        registro_de_actividad(mensaje)
        #return ''
    f.close()
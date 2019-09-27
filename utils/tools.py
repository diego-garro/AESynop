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
import re

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

def registro_de_actividad(mensaje, log):
    """
    Esta función registra la actividad realizada justo antes de ser ejecutada y
    la almacena en el archivo log.txt
    ---------------------------------
    Recibe dos parámetros:
    * mensaje: un objeto de tipo string, el mensaje que se escribirá en log.txt.
    * log: file, archivo log donde se escribirán todos los registros de acividad.
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

def scraping_synops(url, log):
    """
    Esta función scrapea la página de Ogimet.com para obtener los últimos sinópticos
    emitidos por las estaciones terrestres.
    -----------------------
    Recibe dos paŕametros:
    * url: un objeto de tipo string, la url de la página para extraer los sinópticos.
    * log: file, archivo log donde se escribirán todos los registros de acividad.
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
        registro_de_actividad(mensaje, log)
        html = BeautifulSoup(req.text, "html.parser")
        entrada = html.find('pre')
        f.write(str(entrada))
    else:
        mensaje = "{}... No se pudo acceder a la pádina de Ogimet.com."
        registro_de_actividad(mensaje, log)
        #return ''
    f.close()

def almacenar_synops(fichero):
    """
    Esta función toma los reportes sinópticos almacenados en un fichero de texto
    y los acomoda en un string de una sola linea, luego los guarda en una lista.
    ---------------------------
    Recibe un parámetro:
    * fichero: file, el archivo de texto que contiene los reportes sinópticos.
    ---------------------------
    Retorna la lista con los sinópticos colectados.
    """
    lista = []
    synop = ''
    for linea in fichero:
        if linea == '\n' or re.search(r'#+', linea):
            break
        if re.search(r'\d{12}', linea):
            synop = ''
            synop = linea.replace('\n', '')
        elif re.search(r'=\n', linea):
            synop += re.sub(r'\s+', ' ', linea)
            lista.append(re.sub(r'\s{2,}', ' ', synop))
        else:
            synop += re.sub(r'\s+', ' ', linea)
    return lista

def extraer_synops(file_name, oaci_code):
    """
    Esta función encuentra la estación deseada para sacar los sinópticos dentro de un
    archivo de texto plano. Ejecuta la función almacenar_synops() para extraer los
    reportes.
    ----------------------------
    Recibe dos parámetros:
    * file_name: string, el nombre del archivo donde se encuentran los reportes sinópticos.
    * oaci_code: int, el código OACI de la estación a escanear.
    ----------------------------
    Retorna la lista de los reportes sinópticos como una lista, tal como lo retorna la
    función almacenar_synops().
    """
    formato = r'SYNOPS\sde\s{}'.format(oaci_code)
    f = open(file_name, 'r')
    for linea in f:
        #acierto = re.search(formato, linea)
        if re.search(formato, linea):
            f.readline()
            break
    return almacenar_synops(f)
    
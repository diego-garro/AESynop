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

def registro_de_actividad(log_file, mensaje):
    """
    Esta función registra la actividad realizada justo antes de ser ejecutada y
    la almacena en el archivo log.txt
    ---------------------------------
    Recibe dos parámetros:
    * log_file: un objeto de tipo file, es el archivo log para escribir la actividad.
    * mensaje: un objeto de tipo string, el mensaje que se escribirá en log.txt
    ---------------------------------
    No retorna ningún valor.
    """
    fecha = fecha_para_registro()
    print(mensaje.format(fecha))
    log_file.write(mensaje)

def fecha_para_synops():
    """
    Esta función retorna la fecha en una lista para la extracción de los sinópticos
    más recientes desde la web.
    -----------------------
    No recibe parámetros
    -----------------------
    Retorna una lista con año, mes, dia, hora y minuto actuales
    """
    lista = []
    hoy = datetime.utcnow()
    lista.append(hoy.year)
    lista.append(hoy.month)
    lista.append(hoy.day)
    lista.append(hoy.hour)
    lista.append(hoy.minute)
    return lista
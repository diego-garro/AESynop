#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Package: AESynop
Versión: 0.0.1

Developer: Diego Garro Molina
e-mail: diego.garromolina@ucr.ac.cr

AESynop en su versión 0.0.1 es un proyecto para la evaluación de los reportes sinópticos
emitidos por las estaciones meteorológicas terrestres.

Este programa evalúa los reportes grupo por grupo, de modo que extraiga todos los errores
cometidos por el personal de cada estación y que se aprenda de ellos.
"""

from datetime import datetime, timedelta
from utils import tools as tl

log = open("log.txt", "w")
log.write("")
log.close()

hoy, hoy_6h = tl.fecha_para_synops()

URL_ES = 'http://ogimet.com/display_synops2.php?lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano={}&mes={}&day={}&hora={}&anof={}&mesf={}&dayf={}&horaf={}&enviar=Ver'
URL_EN = 'https://www.ogimet.com/display_synops2.php?lang=en&lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano={}&mes={}&day={}&hora={}&anof={}&mesf={}&dayf={}s&horaf={}&send=send'

url = URL_ES.format(hoy_6h[0], str(hoy_6h[1]).zfill(2), str(hoy_6h[2]).zfill(2), str(hoy_6h[3]).zfill(2), hoy[0], str(hoy[1]).zfill(2), str(hoy[2]).zfill(2), str(hoy[3]).zfill(2))
print(url)

tl.scraping_synops(url)
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

log = open("log.txt", "w")

hoy = datetime.utcnow()


url_es = 'http://ogimet.com/display_synops2.php?lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&enviar=Ver'
url_en = 'https://www.ogimet.com/display_synops2.php?lang=en&lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&send=send'


log.close()
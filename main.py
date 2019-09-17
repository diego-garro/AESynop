#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
AESynop en su versión 0.0.1 es un proyecto para la evaluación de los reportes sinópticos
emitidos por las estaciones meteorológicas terrestres.

Este programa evalúa los reportes grupo por grupo, de modo que extraiga todos los errores
cometidos por el personal de cada estación y que se aprenda de ellos.
"""

from datetime import datetime, timedelta

hoy = datetime.utcnow()


url_es = 'http://ogimet.com/display_synops2.php?lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&enviar=Ver'%(annio_6h, mes_6h, dia_6h, hora_6h, annio, mes, dia, hora)
url_en = 'https://www.ogimet.com/display_synops2.php?lang=en&lugar=78764+78762+78774+78767&tipo=ALL&ord=DIR&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&send=send'%(annio_6h, mes_6h, dia_6h, hora_6h, annio, mes, dia, hora)

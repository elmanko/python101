#!/usr/bin/env python3.6

DIGIT_MAP = {
    'zero' : '0',
    'one'  : '1',
    'two'  : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9',
}
import sys
def convert(s):
    """woot"""
    #if not isinstance(s, list):
    #    raise TypeError(
    #       "pasale una lista" )
    #x = -1 #Lo movi de los except por que no afecta lo demas, y se comento por el retur del except
    try: #para manejar exceptions 
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        #x = int(number)
        #print(f'Conversion successful x= {x}')
        return int(number)
    except (KeyError,TypeError) as e:
        print(f'Conversion error: {e!r}',# !r forza la representacion en fstring de reps o el error
             file=sys.stderr) #jala de sys el codigo de error pal exception
        #pass #no-op para bloques de codigo vacios que py no quiere
        #return -1 #voy a usar  raise para cualquier except de key o type
        raise
    #return x

from math import log

#obvio los import no se hacen por todos lados con las patas
#este codigo es de pura prueba, no me juzgues, prro

def string_log(s):
    v = convert(s)
    return log(v)
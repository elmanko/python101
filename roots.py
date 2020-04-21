#!/usr/bin/env python3.6
import sys
def sqrt(x):
    """
    saca raices cuadradas

    Args:
        x: el numero del que quieres la raiz
    
    Regresa:
        la raiz cuadrada de x
    
    Levanta:
        valueError: si x es negativo
    """
    if x < 0:
        raise ValueError(
                "lol no pudo sacar la raiz "
                f"cuadrada de un numero negativo= {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess ) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print('no deberia ser impreso jamas')
    except ValueError as e:
        print(e, file=sys.stderr)
    
    print('todo normal')
if __name__ == "__main__":
    main()
from src.cuadrado import Cuadrado
from src.rectangulo import Rectangulo


def calcular_areas(lista_figuras):
    for figura in lista_figuras:
        print(figura)
        print(f'Area: {figura.area()}')
        print(f'Perimetro: {figura.perimetro()}')
        print('*'.center(50, '*'))


c1 = Cuadrado(lado=3)
c2 = Cuadrado(lado=4)
c3 = Cuadrado(lado=9)
c4 = Cuadrado(lado=7)
c5 = Cuadrado(lado=8)
r1 = Rectangulo(altura=7, base=3)
r2 = Rectangulo(altura=5, base=8)
r3 = Rectangulo(altura=3, base=10)
r4 = Rectangulo(altura=2, base=1)
r5 = Rectangulo(altura=9, base=5)

lista_figuras = [c1, r1, c2, r2, c3, r3, c4, r4, c5, r5]
calcular_areas(lista_figuras)

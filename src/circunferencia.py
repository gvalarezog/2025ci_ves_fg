import math

from src.figura_geometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica):
    def __init__(self, radio=0):
        FiguraGeometrica.__init__(self, alto=radio)

    def __str__(self):
        return f'Circunferencia -> [radio= {self.alto}]'

    def area(self):
        return math.pi * self.alto ** 2

    def perimetro(self):
        return 2 * self.alto + math.pi

if __name__ == '__main__':
    circunferencia = Circunferencia(radio=5)
    print(circunferencia)
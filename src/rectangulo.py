#integrates
#

from src.figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, base=0, altura=0):
        FiguraGeometrica.__init__(self, ancho=base, alto=altura)

    def __str__(self):
        return f'Rectangulo -> [base= {self.ancho}, altura= {self.alto}]'

if __name__ == '__main__':
    rectangulo = Rectangulo(altura=7, base=3)
    print(rectangulo)
    print(f'Area: {rectangulo.area()}')
    print(f'Perimetro: {rectangulo.perimetro()}')
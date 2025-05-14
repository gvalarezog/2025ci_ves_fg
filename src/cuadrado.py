from src.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado=0):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)

    def __str__(self):
        return f'Cuadrado->[lado = {self.alto}]'

if __name__ == '__main__':
    c1 = Cuadrado(lado=6)
    print(c1)
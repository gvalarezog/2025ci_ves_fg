#integrante:
#1
class FiguraGeometrica:
    '''
    Classe que representa una figura geometrica
    '''
    def __init__(self, alto=0, ancho=0):
        '''

        :param alto:
        :param ancho:
        '''
        self._alto = alto
        self._ancho = ancho

    def __str__(self):
        return f'Figura Geometrica {self.__dict__.__str__()}'

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        self._alto = nuevo_alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        self._ancho = nuevo_ancho

    def area(self):
        return self.alto * self.ancho

    def perimetro(self):
        return 2*(self.alto + self.ancho)

if __name__ == '__main__':
    figura = FiguraGeometrica(alto=5, ancho=10)
    print(figura)

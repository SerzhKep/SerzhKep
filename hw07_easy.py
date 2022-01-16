# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, a, b, c):

        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        self.a = a
        self.b = b
        self.c = c
        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.ca = sideLen(self.c, self.a)

    def areaTriangle(self):

        semi_perimeter = self.perimeterTriangle() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ca))

    def perimeterTriangle(self):
        return self.ab + self.bc + self.ca

    def heightTriangle(self):
        return self.areaTriangle() / (self.ab / 2)

treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))

print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):

        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.cd = sideLen(self.c, self.d)
        self.da = sideLen(self.d, self.a)
        self.diagonal_ac = sideLen(self.c, self.a)
        self.diagonal_bd = sideLen(self.b, self.d)
        self.perimeter = self.ab + self.bc + self.cd + self.da
        self.area = areaTriangle(self.ab, self.diagonal_bd, self.da) \
                    + areaTriangle(self.diagonal_bd, self.bc, self.cd)

        def isTrapezeEqu(self):
            if self.diagonal_AC == self.diagonal_BD:
                return True
            return False



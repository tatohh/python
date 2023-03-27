"""
7. Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador)
de forma que podamos hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador.
La fracción se construye simplificada, no se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
"""
import math

class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    def __float__(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other):
        if isinstance(other, int):
            numerator = self.__numerator * other
            denominator = self.__denominator
            gcd = math.gcd(numerator, denominator)
            return Fraction(numerator // gcd, denominator // gcd)
        else:
            raise TypeError("Tipos de operandos no permitidos para *: 'Fraction' and '{}'".format(type(other).__name__))

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.denominator() + self.__denominator * other.numerator()
            denominator = self.__denominator * other.denominator()
            gcd = math.gcd(numerator, denominator)
            return Fraction(numerator // gcd, denominator // gcd)
        else:
            raise TypeError("Tipos de operandos no permitidos para +: 'Fraction' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.denominator() - self.__denominator * other.numerator()
            denominator = self.__denominator * other.denominator()
            gcd = math.gcd(numerator, denominator)
            return Fraction(numerator // gcd, denominator // gcd)
        else:
            raise TypeError("Tipos de operandos no permitidos para -: 'Fraction' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.denominator()
            denominator = self.__denominator * other.numerator()
            g


    def __repr__(self):
        return f"Fraction({self.__numerator}, {self.__denominator})"

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
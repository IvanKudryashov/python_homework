'''
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра.
/
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
'''


class Sum:

    def __init__(self, drob1, drob2):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_sum(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        ch = a_ch * b_zn + b_ch * a_zn
        zn = b_zn * a_zn
        res = (ch, zn)
        return res

    def __str__(self):
        return f'{self.drob1} + {self.drob2} =  {self.data_sum(self.drob1, self.drob2)[0]}/{self.data_sum(self.drob1, self.drob2)[1]}'


class Multy:

    def __init__(self, drob1, drob2):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_mult(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        res = (a_ch * b_ch, a_zn * b_zn)
        return res

    def __str__(self):
        return f'{self.drob1} * {self.drob2} =  {self.data_mult(self.drob1, self.drob2)[0]}/{self.data_mult(self.drob1, self.drob2)[1]}'


a = '3/5'
b = '4/5'

sum1 = Sum(a, b)
mult1 = Multy(a, b)
print(sum1)
print(mult1)

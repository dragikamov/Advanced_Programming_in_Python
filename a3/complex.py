# 350112
# a3 5.py
# Dragi Kamov
# d.kamov@jacobs-university.de

class Complex(object):

    def __init__(self,real,imag):
        self._real=real
        self._imag=imag

    def __str__(self):
        if(self._imag==1):
            return str(self._real)+"+"+"i"
        else:
            return str(self._real)+"+"+str(self._imag)+"i"

    def __ne__(self,other):
        return self._real!=other._real or self._imag!=other._imag

    def __eq__(self,other):
        return self._real==other._real and self._imag==other._imag

    def __add__(self,other):
        ex=Complex(self._real+other._real,self._imag+other._imag)
        return ex

    def __sub__(self,other):
        ex=Complex(self._real-other._real,self._imag-other._imag)
        return ex

    def __mul__(self,other):
        ex=Complex((self._real*other._real)-(self._imag*other._imag),
                   (self._real*other._imag)+(self._imag*other._real))
        return ex

    def __truediv__(self,other):
        Real=((self._real*other._real)+(self._imag*other._imag))/((other._real**2)+(other._imag**2))
        Imag=((self._imag*other._real)-(self._real*other._imag))/((other._real**2)+(other._imag**2))
        ex=Complex(Real,Imag)
        return ex
    

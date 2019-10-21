import math

class Q(object):
    def __init__(self, a, b=1):
        k = math.gcd(a,b)
        self.a = a // k
        self.b = b // k

    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        return f'{self.a}/{self.b}'   # type(str)

    def add(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c, b*d)

    def __add__(self, q):
        a = self.a
        b = self.b
        if isinstance(q, int):
            c = q
            d = 1
        else:
            c = q.a
            d = q.b
        return Q(a*d+b*c, b*d)

    def __sub__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c, b*d)

    def __mul__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*c, b*d)

    def __truediv__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d, b*c)

q=Q(1,2)
q1=Q(2,4)

print(q.add(q1))

print(q+q1)
print(q-q1)
print(q*q1)
print(q/q1)

print(q+3)


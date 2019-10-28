class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
    def __repr__(self):
        return f'{self.value}'
    def eval(self):
        return self.value

class Binary(Expr):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left}, {self.right})'
    def eval(self):
        return toExpr(self.left).eval() + toExpr(self.right).eval()

def toExpr(x):
    if not isinstance(x, Expr):
        x = Val(x)
    return x

class Add(Binary):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(Binary):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(Binary):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Binary):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() // self.right.eval()



x = Val(3)
print(x)
assert x.eval() == 3

assert isinstance(x, Expr)
assert isinstance(x, Val)
assert not isinstance(x, int)

# e = Add(1,3)   #evalを使って値にするので、そもそもintを入れるとNG
e = Add(Val(1), Val(3))
print(e.eval())
assert e.eval() == 4

e = Add(Val(1), Add(Val(3), Val(4)))
print(e.eval())
assert e.eval() == 8

e = Add(1,2)    # Add(1,2,3)はNG
print(e.eval())

e = Add(Add(1,2),5)
print(e.eval())

b=Binary(Add(1,5),Val(3))
print(b)
print(b.eval())

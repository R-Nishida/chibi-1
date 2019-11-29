import pegpy.tpeg as pegpy
grammar = pegpy.grammar('chibi.tpeg')
parser = pegpy.generate(grammar)

class Expr(object):
    @classmethod
    def new(cls, v):
        if isinstance(v, Expr):
            return v
        return Val(v)

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
        self.left = Expr.new(left)  #self.left = left でも動いた
        self.right = Expr.new(right)
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left}, {self.right})'

class Add(Binary):
    __slots__ = ['left', 'right']
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(Binary):
    __slots__ = ['left', 'right']
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(Binary):
    __slots__ = ['left', 'right']
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Binary):
    def eval(self):
        return self.left.eval() // self.right.eval()

def conv(t):
    if t == 'Block':
        return conv(t[0])
    if t == 'Int':
        return Val(int(str(t)))
    if t == 'Add':
        return Add(conv(t[0]), conv(t[1]))
    if t == 'Sub':
        return Sub(conv(t[0]), conv(t[1]))
    if t == 'Mul':
        return Mul(conv(t[0]), conv(t[1]))
    if t == 'Div':
        return Div(conv(t[0]), conv(t[1]))
    print('TODO', t.tag)
    return Val(0)

def run(s : str):
    t = parser(s)
    if t.isError():
        print('tree error')
    else:
        e = conv(t)
        print(repr(e))
        print(e.eval())

def main():
    try:
        while True:
            s = input("$$>")
            if s == '':
                break
            run(s)
    except EOFError:
        return

if __name__ == '__main__':
    main()
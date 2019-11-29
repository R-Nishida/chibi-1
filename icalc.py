import pegpy.tpeg as pegpy
grammar = pegpy.grammar('math.tpeg')
parser = pegpy.generate(grammar)

t=parser('1+2*3')
print(repr(t))

t=parser('(1+2)*3')
print(repr(t))

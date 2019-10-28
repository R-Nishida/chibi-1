from exp import Val, Add, Mul, Sub, Div

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1 = s[:pos]
        s2 = s[pos+1:]
        return Add(parse(s1), parse(s2))
    if s.find('-') > 0:
        pos = s.rfind('-')
        s1 = s[:pos]
        s2 = s[pos+1:]
        return Sub(parse(s1), parse(s2))
    if s.find('*') > 0:
        pos = s.find('*')
        s1 = s[:pos]
        s2 = s[pos+1:]
        return Mul(parse(s1), parse(s2))
    if s.find('/') > 0:
        pos = s.find('/')
        s1 = s[:pos]
        s2 = s[pos+1:]
        return Div(parse(s1), parse(s2))

    return Val(int(s))

e = parse("5+2-4*3")
print(e)
print(e.eval())
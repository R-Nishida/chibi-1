def calc(s):
    return int(s)

def ope_plus(ss):
    k = ss.find('+')
    if (k == -1):
        return calc(ss)
    return ope_plus(ss[:k]) + ope_plus(ss[k+1:])
    
ss = input("please input :")
print('-->', str(ope_plus(ss)))

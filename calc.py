def calc(s):
    return int(s)

def ope_plus(ss):
    k = ss.find('+')
    return calc(ss[:k]) + calc(ss[k+1:])
    
ss = input("please input :")
print('-->', str(ope_plus(ss)))

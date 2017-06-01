"""
i_l = Int-lit - замена числа буквой для шестнадцатичеричной системы
l_i = lit-int - замена ,буквы числом для шестнадцатичеричной системы
"""
            
            
def i_l(x): 
    if x == 10: 
        y = 'A' 
    elif x == 11: 
        y = 'B' 
    elif x == 12: 
        y = 'C' 
    elif x == 13: 
        y = 'D' 
    elif x == 14: 
        y = 'E' 
    elif x == 15: 
        y = 'F' 
    return sxt


def l_i (x): 
    if x == 'A': 
        y = 10 
    elif x == 'B': 
        y = 11 
    elif x == 'C': 
        y = 12 
    elif x == 'D': 
        y = 13 
    elif x == 'E': 
        y = 14 
    elif x == 'F': 
        y = 15 
    return y


def from10(a, b):  
    d = '' 
    if b in (2, 8, 16): 
        while a > 0: 
            c = a % b 
            d = d + str(c) if c <10 else str(d) + str(i_l(c)) 
            a = a // b 
        d = d[::-1] 
    return d


def to10(a, b): 
    a = str(a) 
    res = int()
    a = list(a[::-1]) 
    for i, e in enumerate(a): 
        e = l_i(e) if e in ('A', 'B', 'C', 'D', 'E', 'F') else e 
        d += int(e) * (b ** i) 
    return d  


def f10to2(x): 
    conv = from10(x, 2) 
    return conv
        

def f10to8(x): 
    conv = from10(x, 8) 
    return conv
        

def f10to16(x): 
    conv = from10(x, 16) 
    return conv    


def f2to10(x):
    conv = to10(x, 2)
    return conv
        

def f8to10(x):
    conv = to10(x, 8)
    return conv
    
    

def f16to10(x):
    conv = to10(x, 16)
    return conv
    print(conv)


        
            




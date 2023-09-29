import math
import numpy as np
from scipy.misc import derivative 

def f(x): 
   return 3*pow(x, 4) - 4*pow(x,3) + 2*pow(x, 2)  - 4*x - 1
 
eps=0.0001 
segments = [[-1, 0],[1, 2]] 

for a, b in segments: 
    print(f'Відрізки, які знайшли у попередній практичній:  [{a}, {b}]') 

def nuton(a,b,eps): 
    df2 = derivative(f, b, n = 2) 
    if (f(b)*df2>0): 
        xi = b 
    else: 
        xi = a 
    df = derivative(f,xi, n= 1) 
    xi_1 = xi - f(xi)/df 
    while (abs(xi_1 - xi)>eps):  
        xi = xi_1 
        xi_1 = xi - f(xi)/df 
    return print ("Розв'язок рівняння методом Ньютона x = ", xi_1) 
    
def komb(a,b,eps): 
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0): 
        a0 = a 
        b0 = b 
    else: 
        a0 = b 
        b0 = a 
    ai = a0 
    bi = b0 
    while abs(ai-bi)>eps:    
        ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai)) 
        bi_1 = bi - f(bi)/derivative(f,bi, n= 1)  
        ai = ai_1 
        bi = bi_1 
    x = (ai_1+bi_1)/2 
    return print("Розв'язок рівняння комбінованим методом x = ", x) 

for i in segments:
    a = i[0]
    b = i[1]
    print (f'Розв’язок нелінійного рівняння на відрізку [{a}, {b}]')
    nuton(a,b,eps)
    komb(a,b,eps)
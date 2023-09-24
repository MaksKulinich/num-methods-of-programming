import math
import numpy as np
from scipy.misc import derivative 

def f(x): 
   return 3*pow(x, 4) - 4*pow(x,3) + 2*pow(x, 2)  - 4*x - 1 
eps=0.0001 

def find_segments(): # функція для відокремлення коренів 
    search_range = np.arange(-10, 10, 1)
    a = None 
    previous_x = None 
    current_x  = None 
    segments = [] 
    for x in search_range: 
        x = round(x, 4) 
        current_x = f(x) 
        if previous_x != None and previous_x * current_x < 0: 
            segments.append((a, x)) 
        a = x 
        previous_x = current_x 
    return segments 

segments = find_segments() 

for a, b in segments: 
    print(f'Знайдені відрізки:  [{a}, {b}]') 
    
def halving(a, b, eps): #метод половинного ділення 
    while (abs(a-b) > eps): 
        if f(a)*f((a+b)/2)<0:  
            b = (a+b)/2  
        else:  
            a = (a+b)/2 
        x = (a+b)/2 
    print ('x= ', round(x,5), '  -   Метод половинного ділення') 

def hord (a,b,eps): #метод хорд 
    if (f(a)*derivative(f,a,n=2)>0): 
        x0=a 
        xi=b 
    else: 
        x0=b 
        xi=a 
    xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0)) 
    while (abs(xi_1-xi)>eps): 
        xi=xi_1 
        xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0)) 
    print('x= ', round (xi_1,5) , '  -   Метод хорд') 

for i in segments:
    a = i[0]
    b = i[1]
    print (f'Розв’язок нелінійного рівняння на відрізку [{a}, {b}]')
    halving (a,b,eps)
    hord (a,b,eps)
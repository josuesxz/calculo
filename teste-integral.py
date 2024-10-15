# meu_calculo\Scripts\activate

import sympy as calc

x = calc.symbols('x') #defina o diferencial
f=x**2 #defina a função 
print(calc.integrate(f,x))

print(" RELAÇÕES ENTRE OS COEFICIENTES E AS RAÍZES - Eq. do 2º grau")
x1 = float(input("x' = "))
x2 = float(input("x'' = "))
b = (-1)*(x1+x2)
c = x1*x2
print("f(x) = x2 + (", b ,")x + (", c,")")
print("    ou")
b = (-1)*b
c = (-1)*c
print("f(x) = -x2 + (", b ,")x + (", c,")")

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

resultado = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
##(((x2-x1)**2)+((y2-y1)**2))**1/2
#√((x2 – x1)² + (y2 – y1)²).


print(f"A distãncia é igual a: {resultado:.3f}")
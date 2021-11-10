pesos = input("cuantos pesos colombianos tienes?: ")
pesos = float(pesos)           #es igual a int y transforma un valor o una variable a un decimal 
valor_dolar = 3750
dolares = pesos / valor_dolar
dolares = round(dolares, 2)    #los reducimos a dos decimales y la guardamos en la variable dolares 
dolares = str(dolares)
print("tienes $" + dolares + " dolares")
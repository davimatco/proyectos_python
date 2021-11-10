menu = """       
bienvenido al conversor de monedas 😁

1 - pesos colombianos
2 - pesos argentinos 
3 - pesos mexicanos 

elige una opcion """   

opcion = int(input(menu))

if opcion == 1:
    pesos = input("cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)           #es igual a int y transforma un valor o una variable a un decimal 
    valor_dolar = 3750
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)    #los reducimos a dos decimales y la guardamos en la variable dolares 
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)           #es igual a int y transforma un valor o una variable a un decimal 
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)    #los reducimos a dos decimales y la guardamos en la variable dolares 
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion ==  3:
    pesos = input("cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)           #es igual a int y transforma un valor o una variable a un decimal 
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)    #los reducimos a dos decimales y la guardamos en la variable dolares 
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
else: 
    input("elige una opcion correcta")

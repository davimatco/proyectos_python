def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)           #es igual a int y transforma un valor o una variable a un decimal 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)    #los reducimos a dos decimales y la guardamos en la variable dolares 
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
menu = """       
bienvenido al conversor de monedas 😁

1 - pesos colombianos
2 - pesos argentinos 
3 - pesos mexicanos 

elige una opcion """   

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion ==  3:
    conversor("mexicanos", 24)
else: 
    input("elige una opcion correcta")


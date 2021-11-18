import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("elije un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("elije un numero mayor")
        else:
            print("elije un numero menor")
        numero_elegido = int(input("elije otro numero"))
    print("ganaste")

    

if __name__ == "__main__":
    run()

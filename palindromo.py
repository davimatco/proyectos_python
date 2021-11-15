def palindromo(palabra):
    palabra = palabra.replace(" ", "")       #eliminar los espacios
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
def run():
    palabra = input("escribe una palabra ")
    es_palindromo = palindromo(palabra)
    if  es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")

if __name__ == "__main__":        #punto de entrada de un programa de python
   run()
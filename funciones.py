#  def imprimir_mensaje():        #las funciones tambien tienen nombres y se aplican las mismas reglas 
#      print("mensaje especial: ")
#  print("estoy aprendiendo a usar funciones  ")

#    imprimir_mensaje()                  #invocar: voy a la definicion de la funcion 
#    imprimir_mensaje() 
#    imprimir_mensaje() 


# def conversacion(mensaje):                            #los parametros son variables que tenemos para usar dentro de la funcion
#     print("hola")
#     print("como estas")
#     print(mensaje)
  

# opcion = int(input("elije una opcion (1, 2, 3): "))
# if opcion == 1:
#     conversacion("elejiste la opcion 1")

# elif opcion == 2: 
#     conversacion("elejiste la opcion 2")

# elif opcion == 3: 
#     conversacion("elejiste la opcion 3")

# else: 
#     print("escribe la opcion correcta")


def suma(a, b): 
    print("se suman dos numeros")
    resultado = a + b
    return resultado         #se deevuelve el resultado 

sumatoria = suma(1, 4)
print(sumatoria)


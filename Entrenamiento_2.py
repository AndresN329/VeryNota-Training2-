#Peticion de datos 
print("-" * 40)
print("             VeryNota :0")
print("-" * 40)

#Verificacion de aprovacion

while True:

    try:
        Calificacion = float(input("\nPor favor ingresar una calificación numérica de 0 a 100: "))

        if 0 <= Calificacion <=100:

            if Calificacion >= 60:
                print("\nHas aprobado, felicitaciones :)")
                break
            else:
                print("\nHas reprobado, continua esforzandote :(")
                break
        else: 
            print("\nSolo se permiten numeros de 0 a 100")
    except ValueError:
        print("\nPor favor, ingresa un valor numerico entre 0 y 100 >:(")


# Promedio

print("-" * 50)
print("       Sacar promedio de notas")
print("-" * 50)


Notas_no_comas = [] #En caso de que diga que no quiere promedio

while True:
    Prome = input("\n¿Quieres sacar el promedio de tus notas?(SI/NO): ").lower().strip()
    if Prome == "si":
        while True:
            try:
                Ing_Notas = input("\nPor favor ingresa tus notas separadas por comas: ").strip()

                if "," not in Ing_Notas:
                    print("\nLos números deben estar separados por comas")
                    continue

                Notas_comas = Ing_Notas.split(",")
                Notas_no_comas = []

                for nota in Notas_comas:
                    numero = float(nota.strip())
                    if 0 <= numero <= 100:
                        Notas_no_comas.append(numero)
                    else:
                        print("\nLa nota", numero, "está fuera de rango de 0-100")
                        break  # sale del for y pide notas again
                else:
                    promedio = sum(Notas_no_comas) / len(Notas_no_comas)
                    print("\nEl promedio es:", promedio)
                    break 
            except ValueError:
                print("\nPor favor ingresa solo números separados por comas")
        break  

    elif Prome == "no": 
        print("\nA bueno.")
        
        Confirmacion = input("\n¿Quieres ingresar una lista de notas para compararlas? (SI/NO): ").lower().strip()
        if Confirmacion == "si":
            while True:
                try:
                    Ing_Notas = input("\nPor favor ingresa tus notas separadas por comas: ").strip()

                    if "," not in Ing_Notas:
                        print("\nLos números deben estar separados por comas")
                        continue

                    Notas_comas = Ing_Notas.split(",")
                    for nota in Notas_comas:
                        numero = float(nota.strip())
                        if 0 <= numero <= 100:
                            Notas_no_comas.append(numero)
                        else:
                            print("\nLa nota",numero,"está fuera del rango de 0-100")
                            break
                    else:
                        break
                except ValueError:
                    print("\nPor favor ingresa solo números separados por comas")
        break
    else:
        print("\nPor favor escribe solo 'Si' o 'No'")

#Calificaciones mayores a un valor especifico

if Notas_no_comas:  #continuar si hay notas
    print("-" * 50)
    print("    Notas mayores a valor especifico")
    print("-" * 50)
    while True:
        try:
            Nota_comparar = float(input("\nIngresa la nota que quieres usar para comparar (Cuantas mayores hay): "))
            if 0 <= Nota_comparar <= 100:
                mayores = [nota for nota in Notas_no_comas if nota > Nota_comparar]
                print("\nHay",len(mayores),"calificaciones mayores a",Nota_comparar)
                if mayores:
                    print("\nLas notas son:", mayores)
                break
            else:
                print("\nLa nota de comparacion debe estar entre 0 y 100")
        except ValueError:
            print("\nPor favor solo ingresa un número")

#Verificar y contar calificaciones específicas

print("-" * 50)
print("    Verificar y contar calificaciones específicas")
print("-" * 50)

while True:
    try:
        Entrada = input("\nIngresa las calificaciones separadas por comas: ").strip()

        if "," not in Entrada:
            print("\nDebes separar las calificaciones con comas.")
            continue

        Calificaciones = [float(nota.strip()) for nota in Entrada.split(",")]
        Buscar = float(input("\nIngresa la calificación específica que deseas buscar: "))
        Cantidad = Calificaciones.count(Buscar)  #Contar cuantas veces aparece

        print("\nLa calificación",Buscar,"aparece",Cantidad,"veces en la lista")
        break

    except ValueError:
        print("\npor favor ingresar ingresar solo números.")

print("-" * 50)
print("Gracias por usar el programa :)")
print("-" * 50)
print("Buenos días\nPara salir, escriba 'salir'\nLas operaciones son:")
print("+ - * /")

# Bucle principal
while True:
    try:
        # Solicitar el primer número
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = float(resultado)

        while True:  # Bucle para operaciones continuas
            # Solicitar la operación
            op = input("Ingrese operación suma(+), resta(-), multiplicación(*), división(/)\n >>> ")
            if op.lower() == "salir":
                break

            # Solicitar el segundo número
            n2 = input("Ingrese segundo número: ")
            if n2.lower() == "salir":
                break
            n2 = float(n2)

            # Realizar la operación
            if op == "+":
                resultado += n2
            elif op == "-":
                resultado -= n2
            elif op == "*":
                resultado *= n2
            elif op == "/":
                # Prevenir división por cero
                if n2 == 0:
                    print("Error: División por 0 no es permitida.")
                    continue
                resultado /= n2
            else:
                print("Operación no encontrada. Intente de nuevo.")
                continue  # Continuar con el bucle si la operación no es válida

            # Mostrar el resultado
            print(f"El resultado es: {resultado}")

    except ValueError:
        print("Por favor, ingrese un número válido.")

    if op.lower() == "salir" or n2.lower() == "salir":
        break  # Salir del bucle principal si se ingresó 'salir' durante las operaciones

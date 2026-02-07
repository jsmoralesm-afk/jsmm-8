print("=== CALCULADORA BÁSICA ===")

while True:
    print("\nOpciones:")
    print("1. potencia")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Gracias por usar la calculadora 👋")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcion == "4":
            if num2 == 0:
                print("Error: no se puede dividir entre 0")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)
    else:
        print("Opción inválida, intenta de nuevo.")
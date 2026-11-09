def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def leer_numero(mensaje):
    """Pide un número y repite hasta que sea válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingresa un número válido.")


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


OPERACIONES = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    "4": dividir,
}


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Hasta luego.")
            break

        if opcion not in OPERACIONES:
            print("Opción inválida. Intenta de nuevo.")
            continue

        a = leer_numero("Primer número: ")
        b = leer_numero("Segundo número: ")

        try:
            print("Resultado:", OPERACIONES[opcion](a, b))
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
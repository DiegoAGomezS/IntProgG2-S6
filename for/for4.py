#tablas de multiplicar de un número ingresado.

def tablaNumero(nume):
    for i in range(1, 13):
        mult = nume * i
        print(f"{nume} * {i} = {mult}")  

def main():
    numero = int(input("Ingrese un número natural: "))
    tablaNumero(numero)

main()
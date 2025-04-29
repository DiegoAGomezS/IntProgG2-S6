def numerosPares (nume):
    for i in range(1, nume + 1):
        if i % 2 == 0:
            print(i, end = " ")
    
def main():
    nume = int(input("Ingrese el numero: "))
    if nume <= 0:
        print("Ingrese un número natural: ")
    else: numerosPares(nume)

main()
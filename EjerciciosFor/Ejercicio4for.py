def contadorRegresivo(inicio, resta):
    if resta == 0:
        for i in range(inicio, resta):
           print(i, end = " ")
    else:
        for i in range(inicio - 1):
            print(i, end = " ")
        
def main():
    inicio = int(input("Ingrese el numero: "))
    resta = inicio - 1
    contadorRegresivo(inicio, resta)
    
main()
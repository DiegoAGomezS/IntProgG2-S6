def sumaNumeros(num1,num2):
    if (num1 + num2) > 100:
        for i in range(num1, num2):
            print(i, end = " ")
    else:
        for i in range((num1, num2 < 100)):
            print(i, end = " ")

def main():
    num1 = int(input("Ingrese su primer valor: "))
    num2 = int(input("Ingrese su primer valor: "))
    sumaNumeros(num1, num2)
    
main()
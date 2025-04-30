
def serieFibonacci(n):
    num1 = 0
    num2 = 1
    for i in range(n):
        print(num1, end = " ")
        siguiente = num1 + num2
        num1 = num2
        num2 = siguiente

def main():
    n = int(input("Seleccione el número de caracteres: "))
    serieFibonacci(n)
    
main ()
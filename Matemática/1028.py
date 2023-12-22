n = int(input())

def euclides_mdc(dividendo, divisor): #maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp    
    return dividendo

for i in range(n):
    F1, F2 = [int(x) for x in input().split()]
    res = euclides_mdc(F1, F2)
    
    print(res)

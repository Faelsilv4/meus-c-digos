

num = int(input("Fatorial do numero: "))

def fatorial(n):
    return 1 if  n == 1 or n == 0 else n * fatorial(n-1)

print(fatorial(num))

def delta (a,b,c):
    return b**2-4*a*c

def delta_p (a,b,c):
    return (-b+(delta(a,b,c)**(1/2)))/(2*a)

def delta_n (a,b,c):
    return (-b-(delta(a,b,c)**(1/2)))/(2*a)

def main():
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))
    c = int(input("Valor de c: "))
    
    if a==0 or delta(a,b,c)<0:
        print("Impossivel calcular")
    else:
        print(f"R1 = {delta_p(a,b,c):.1f}")
        print(f"R2 = {delta_n(a,b,c):.1f}")
if __name__ =="__main__":
    main()
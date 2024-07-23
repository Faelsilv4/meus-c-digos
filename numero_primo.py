def primo(n):
    x = 0
    if n % 2 == 1 or n ==2:
        for y in range(1,n+1):
            primo = n % y
            if primo == 0:
                x+=1
                if x>2:
                    x=n
    if x==2:
        return f"O número {n} é primo"
    else:
        return f"O número {n} nao é primo"
def main():
    num=int(input("Digite o número: "))
    print(primo(num))
if __name__=="__main__":
    main()
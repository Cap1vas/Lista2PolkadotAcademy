def encontrar_primos(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if num > 1:  # 1 não é primo
            eh_primo = True
            for div in range(2, int(num ** 0.5) + 1):
                if num % div == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(num)
    return primos

inicio = int(input("Insira o início do intervalo: "))
fim = int(input("Insira o fim do intervalo: "))

primos = encontrar_primos(inicio, fim)

if len(primos) == 0:
    print("Não há números primos nesse intervalo.")
else:
    print("Números primos no intervalo:")
    for primo in primos:
        print(primo)
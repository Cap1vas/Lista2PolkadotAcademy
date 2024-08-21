def parImpar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"

num = int(input("Entra com um valor aia"))
print(parImpar(num))

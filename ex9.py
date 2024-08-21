frase = input("Insira uma frase: ")
letra = input("Insira a letra que deseja contar: ")

contador = 0
for char in frase.lower():
    if char == letra.lower():
        contador += 1

print(f"A letra '{letra}' aparece {contador} vezes na frase.")
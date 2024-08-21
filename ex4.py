tempAtual = float(input("Qual a temp atual?"))
if(tempAtual>30):
    print("Está muito quente")
elif(tempAtual<15):
    print("Está muito frio")
elif(tempAtual>=15 and tempAtual<=30):
    print("Está agradável")
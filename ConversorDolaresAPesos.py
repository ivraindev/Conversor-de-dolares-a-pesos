dolares = input ("escribre aqui la cantidad en Dolares: ")
dolares = float (dolares)
valor_pesoMexicano = 0.049
pesos = dolares / valor_pesoMexicano
pesos = round(pesos, 2)
pesos = str (pesos)
print ("Tienes $" + pesos + " pesos Méxicanos")
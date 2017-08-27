print("Informações de viagem")
distancia = float(input("Distância percorrida (km): "))
tempo = float(input("Duração da viagem (h): "))
vm = distancia/tempo
combustivel = distancia/12
print("Velocidade média: %.1f m/s" %vm)
print("Distância percorrida: %.1f km" %distancia)
print("Combustível consumido: %.1f l" %combustivel)

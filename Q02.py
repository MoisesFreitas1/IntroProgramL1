print("Salário líquido do professor")
horas = float(input("Horas trabalhadas: "))
horaAula = float(input("Valor da hora-aula: R$ "))
salario = horas*horaAula*0.92
print("Salário Líquido: R$ %.2f"%salario)
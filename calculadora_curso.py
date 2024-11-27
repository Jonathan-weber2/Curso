# Entrada dos dados
nome = input("Nome do usuário: ")
idade = int(input("Idade do usuário: "))  # Convertendo para int
renda = float(input("Ganho anual: "))  # Convertendo para float
meses = int(input("Meses de trabalho: "))  # Convertendo para int
dias = int(input("Dias trabalhados no mês: "))  # Convertendo para int
horas = int(input("Horas de trabalho: "))  # Convertendo para int

# Exibindo os dados fornecidos
print(f"Seu nome é {nome}, sua idade é {idade}, sua renda anual é R${renda}, meses trabalhados: {meses}, dias trabalhados: {dias}, horas trabalhadas: {horas}")

# Cálculos
renda_mensal = renda / meses  # Renda mensal
dias_trabalhados = meses * dias  # Total de dias trabalhados no ano
horas_trabalhadas = dias_trabalhados * horas  # Total de horas trabalhadas no ano

# Exibindo os resultados dos cálculos
print(f"Sua renda mensal é R${renda_mensal:.2f}")
print(f"Você trabalhou um total de {dias_trabalhados} dias.")
print(f"Você trabalhou um total de {horas_trabalhadas} horas.")

# Calculando o valor médio ganho por hora
ganhos_por_hora = renda / horas_trabalhadas  # Ganho por hora de trabalho
print(f"O valor médio ganho por hora é R${ganhos_por_hora:.2f}")

# Criando uma lista com os resultados
dados = [renda_mensal, dias_trabalhados, horas_trabalhadas, ganhos_por_hora]

# Exibindo os dados da lista
print(dados)

# Exibindo cada item individualmente
print(f"Renda mensal: {dados[0]:.2f}")
print(f"Dias trabalhados no ano: {dados[1]}")
print(f"Horas trabalhadas no ano: {dados[2]}")
print(f"Ganho médio por hora: {dados[3]:.2f}")

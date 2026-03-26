from datetime import datetime, timedelta

# função do montante
def calcular_montante(c, i, n):
    return c * (1 + i/100) ** n

try:
    tipo = input("Tipo de investimento é  cdb ou lci:  ")
    capital = float(input("Capital inicial: "))
    taxa = float(input("Taxa (% ao mês): "))
    meses = int(input("Meses: "))

    # datas
    data_aplicacao = datetime.now()
    data_vencimento = data_aplicacao + timedelta(days=meses*30)

    # cálculo
    montante = calcular_montante(capital, taxa, meses)

    # saída
    print("\n--- Resultado ---")
    print(f"Tipo: {tipo}")
    print(f"Capital: R$ {capital:.2f}")
    print(f"Taxa: {taxa:.2f}%")
    print(f"Prazo: {meses} meses")
    print(f"Montante: R$ {montante:.2f}")
    print("Data aplicação:", data_aplicacao.strftime("%d/%m/%Y"))
    print("Vencimento:", data_vencimento.strftime("%d/%m/%Y"))

except:
    print("Erro: entrada inválida.")
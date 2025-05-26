import math

# Função para calcular o montante com juros compostos
def calcular_juros_compostos(principal, taxa_juros, tempo_meses):
    taxa_decimal = taxa_juros / 100
    montante = principal * (1 + taxa_decimal) ** tempo_meses
    return round(montante, 2)

# Função para calcular média ponderada de gastos mensais
def calcular_media_ponderada(despesas):
    total_peso = sum(peso for _, peso in despesas)
    if total_peso == 0:
        return 0
    soma_ponderada = sum(valor * peso for valor, peso in despesas)
    return round(soma_ponderada / total_peso, 2)

# Coleta de dados do usuário
def coletar_despesas():
    despesas = []
    print("Digite suas despesas fixas e variáveis. (Digite 0 para encerrar)")
    while True:
        try:
            valor = float(input("Valor da despesa: R$ "))
            if valor == 0:
                break
            peso = int(input("Peso da despesa (1 a 5): "))
            despesas.append((valor, peso))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    return despesas

def coletar_investimentos():
    investimentos = []
    print("\nDigite seus investimentos. (Digite 0 para encerrar)")
    while True:
        try:
            valor = float(input("Valor investido: R$ "))
            if valor == 0:
                break
            taxa = float(input("Taxa de rendimento (% ao mês): "))
            tempo = int(input("Tempo de aplicação (em meses): "))
            montante = calcular_juros_compostos(valor, taxa, tempo)
            investimentos.append(montante)
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    return investimentos

# Cálculo de salário ideal
def calcular_salario_ideal(total_despesas, total_lucros):
    margem_segura = 0.10  # margem extra de segurança de 10%
    salario = (total_despesas - total_lucros) * (1 + margem_segura)
    return round(salario, 2)

# Projeções de lucro
def gerar_projecoes(salario):
    return {
        "Diário": round(salario / 30, 2),
        "Semanal": round(salario / 4, 2),
        "Mensal": salario,
        "Anual": round(salario * 12, 2)
    }

# Função principal
def main():
    print("==== CONTROLE FINANCEIRO DIDÁTICO ====")
    
    despesas = coletar_despesas()
    investimentos = coletar_investimentos()

    total_despesas = calcular_media_ponderada(despesas)
    total_lucros = sum(investimentos)

    salario_ideal = calcular_salario_ideal(total_despesas, total_lucros)
    projecoes = gerar_projecoes(salario_ideal)

    print("\n==== RESULTADOS ====")
    print(f"Despesas médias ponderadas: R$ {total_despesas}")
    print(f"Rendimento estimado dos investimentos: R$ {total_lucros}")
    print(f"Salário ideal estimado: R$ {salario_ideal}")

    print("\nProjeções:")
    for periodo, valor in projecoes.items():
        print(f"{periodo}: R$ {valor}")

if __name__ == "__main__":
    main()

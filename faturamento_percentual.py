import json

# Dados de faturamento embutidos (em reais)
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Função para carregar dados de um arquivo JSON (opcional)
def carregar_json(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Usando dados embutidos.")
        return faturamento_estados
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON. Usando dados embutidos.")
        return faturamento_estados

# Função para calcular percentuais
def calcular_percentuais(dados):
    # Calcular faturamento total manualmente
    total = 0.0
    for valor in dados.values():
        total += valor
    
    # Verificar se o total é zero para evitar divisão por zero
    if total == 0:
        return {estado: 0.0 for estado in dados}
    
    # Calcular percentual para cada estado
    percentuais = {}
    for estado, valor in dados.items():
        percentual = (valor / total) * 100
        percentuais[estado] = percentual
    
    return percentuais, total

# Carregar dados (descomente para usar arquivo externo)
# dados = carregar_json("faturamento_estados.json")
dados = faturamento_estados  # Usar dados embutidos

# Calcular percentuais e total
percentuais, faturamento_total = calcular_percentuais(dados)

# Exibir resultados
print("Percentual de representação por estado no faturamento mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
print(f"\nFaturamento total: R${faturamento_total:.2f}")

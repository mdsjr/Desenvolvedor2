import json

# Dados de faturamento embutidos (para teste)
dados_json = [
    {"dia": 1, "faturamento": 1000.0},
    {"dia": 2, "faturamento": 1500.0},
    {"dia": 3, "faturamento": 0.0},  # Sem faturamento
    {"dia": 4, "faturamento": 2000.0},
    {"dia": 5, "faturamento": 1800.0},
    {"dia": 6, "faturamento": 0.0},  # Sem faturamento
    {"dia": 7, "faturamento": 2200.0},
    {"dia": 8, "faturamento": 1700.0},
    {"dia": 9, "faturamento": 0.0},  # Sem faturamento
    {"dia": 10, "faturamento": 1900.0}
]

# Função para carregar dados de um arquivo JSON (opcional)
def carregar_json(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Usando dados embutidos.")
        return dados_json
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON. Usando dados embutidos.")
        return dados_json

# Função para analisar faturamento
def analisar_faturamento(dados):
    # Inicializar variáveis
    menor_faturamento = None
    maior_faturamento = None
    soma_faturamento = 0.0
    dias_com_faturamento = 0
    faturamentos = []

    # Filtrar dias com faturamento e calcular soma
    for entrada in dados:
        faturamento = entrada.get("faturamento", 0.0)
        if faturamento > 0:  # Ignorar dias sem faturamento
            faturamentos.append(faturamento)
            soma_faturamento += faturamento
            dias_com_faturamento += 1
            # Atualizar menor e maior faturamento
            if menor_faturamento is None or faturamento < menor_faturamento:
                menor_faturamento = faturamento
            if maior_faturamento is None or faturamento > maior_faturamento:
                maior_faturamento = faturamento

    # Verificar se há dias com faturamento
    if dias_com_faturamento == 0:
        return {
            "menor_faturamento": 0.0,
            "maior_faturamento": 0.0,
            "dias_acima_media": 0
        }

    # Calcular média mensal
    media_mensal = soma_faturamento / dias_com_faturamento

    # Contar dias com faturamento acima da média
    dias_acima_media = 0
    for faturamento in faturamentos:
        if faturamento > media_mensal:
            dias_acima_media += 1

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media,
        "media_mensal": media_mensal  # Para referência
    }

# Carregar dados (descomente para usar arquivo externo)
# dados = carregar_json("faturamento.json")
dados = dados_json  # Usar dados embutidos

# Analisar faturamento
resultado = analisar_faturamento(dados)

# Exibir resultados
print(f"Menor faturamento diário: R${resultado['menor_faturamento']:.2f}")
print(f"Maior faturamento diário: R${resultado['maior_faturamento']:.2f}")
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")
print(f"(Média mensal: R${resultado['media_mensal']:.2f})")  # Para referência

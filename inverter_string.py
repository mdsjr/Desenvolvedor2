def inverter_string(s):
    # Converter a string em uma lista de caracteres (ou iterar diretamente)
    tamanho = 0
    for _ in s:  # Contar o tamanho manualmente
        tamanho += 1
    
    # Criar uma nova string invertida
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        # Acessar o caractere na posição i manualmente
        contador = 0
        for char in s:
            if contador == i:
                string_invertida += char
                break
            contador += 1
    
    return string_invertida

# Entrada da string
try:
    entrada = input("Digite uma string para inverter (ou pressione Enter para usar 'exemplo'): ")
    if entrada == "":
        entrada = "exemplo"  # String padrão se nenhuma entrada for fornecida
except EOFError:
    entrada = "exemplo"  # Fallback para string padrão em caso de erro

# Inverter a string
resultado = inverter_string(entrada)

# Exibir resultado
print(f"String original: {entrada}")
print(f"String invertida: {resultado}")

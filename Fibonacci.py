def verifica_fibonacci(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    # A sequência de Fibonacci é definida como:
    if n < 0:
        return False  # Números negativos não pertencem à sequência
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    if n == 0 or n == 1:
        return True  # 0 e 1 pertencem à sequência

    # Inicializa os dois primeiros números da sequência
    
    a = 0  # Primeiro número
    b = 1  # Segundo número
    proximo = a + b  # Próximo número

    # Gerar a sequência até que o próximo número seja >= n
    while proximo <= n:
        if proximo == n:
            return True  # O número foi encontrado
        # Atualizar os valores
        a = b
        b = proximo
        proximo = a + b
    
    return False  # O número não foi encontrado

# Entrada do número
try:
    numero = int(input("Digite um numero para verificar se pertence a sequencia de Fibonacci: "))
    # Verificar se o número pertence à sequência
    if verifica_fibonacci(numero):
        print(f"O numero {numero} pertence a sequencia de Fibonacci.")
    else:
        print(f"O numero {numero} NAO pertence a sequencia de Fibonacci.")
except ValueError:
    print("Erro: Entrada invalida. Por favor, digite um numero inteiro.")

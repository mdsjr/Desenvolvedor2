# Soluções para Exercícios de Programação - Processo Seletivo Desenvolvedor 2

Este repositório contém as soluções para os cinco exercícios propostos no processo seletivo para a posição de Desenvolvedor 2. Todos os programas foram implementados em Python 3, seguindo as restrições de evitar funções prontas (ex.: `reverse`, `min`, `max`, `sum`) e permitindo entrada flexível (definida no código ou via entrada do usuário).

## Estrutura do Repositório

O repositório contém os seguintes arquivos:

- `soma_indice.py`: Solução para a Pergunta 1 (Cálculo da variável SOMA).
- `fibonacci_checker.py`: Solução para a Pergunta 2 (Verificação de número na sequência de Fibonacci).
- `faturamento_diario.py`: Solução para a Pergunta 3 (Análise de faturamento diário).
- `faturamento_percentual.py`: Solução para a Pergunta 4 (Percentual de faturamento por estado).
- `inverter_string.py`: Solução para a Pergunta 5 (Inversão de uma string).
- `README.md`: Este arquivo, com instruções e informações sobre o projeto.

## Descrição dos Exercícios

### Pergunta 1: Cálculo da Variável SOMA

- **Descrição:** Calcula o valor final da variável `SOMA` após executar um trecho de código que soma números de 1 a 13.
- **Arquivo:** `soma_indice.py`
- **Saída Esperada:** `SOMA = 91`
- **Detalhes:** Implementado com um loop `while` para simular o trecho fornecido.

### Pergunta 2: Verificação na Sequência de Fibonacci

- **Descrição:** Verifica se um número informado pertence à sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, ...).
- **Arquivo:** `fibonacci_checker.py`
- **Entrada:** Número inteiro via `input()` ou valor fixo (padrão: 21).
- **Saída Esperada:** Mensagem indicando se o número pertence à sequência (ex.: `"O numero 21 pertence a sequencia de Fibonacci."`).
- **Detalhes:** Usa iteração para gerar a sequência e evita funções prontas.

### Pergunta 3: Análise de Faturamento Diário

- **Descrição:** Analisa um vetor de faturamento diário (em JSON) e retorna:
    - Menor faturamento diário.
    - Maior faturamento diário.
    - Número de dias com faturamento acima da média mensal.
- **Arquivo:** `faturamento_diario.py`
- **Entrada:** Dados em JSON embutidos ou arquivo externo (`faturamento.json`).
- **Saída Esperada (para dados embutidos):**
```
Menor faturamento diário: R$1000.00
Maior faturamento diário: R$2200.00
Número de dias com faturamento acima da média: 4
(Média mensal: R$1728.57)
```
- **Detalhes:** Ignora dias sem faturamento (valor 0) e calcula manualmente mínimo, máximo e média.

### Pergunta 4: Percentual de Faturamento por Estado

- **Descrição:** Calcula o percentual de representação de cada estado no faturamento mensal total.
- **Arquivo:** `faturamento_percentual.py`
- **Entrada:** Dados embutidos (`SP: R$67.836,43`, `RJ: R$36.678,66`, etc.) ou arquivo JSON (`faturamento_estados.json`).
- **Saída Esperada:**
````
Percentual de representação por estado no faturamento mensal:
SP: 37.52%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 10.98%

Faturamento total: R$180759.98
````
- **Detalhes:** Soma manual do faturamento total e cálculo de percentuais sem funções prontas.

### Pergunta 5: Inversão de String

- **Descrição:** Inverte os caracteres de uma string sem usar funções prontas (ex.: `reverse`).
- **Arquivo:** `inverter_string.py`
- **Entrada:** String via `input()` ou valor fixo (padrão: `"exemplo"`).
- **Saída Esperada (exemplo):**
````
String original: exemplo
String invertida: olpmexe
````
- **Detalhes:** Inversão manual com iteração sobre caracteres.

## Pré-requisitos

- **Python 3:** Versão 3.6 ou superior (testado com Python 3.12).
- **Dependências:** Apenas a biblioteca padrão do Python é usada, exceto para os exercícios 3 e 4, que requerem o módulo `json` (incluso no Python).
- **Sistema Operacional:** Testado no Windows (PowerShell e CMD), mas compatível com Linux/Mac.

## Como Executar

1.  **Clonar o Repositório:**
  ```bash
  git clone <URL_DO_REPOSITORIO>
  cd <NOME_DO_REPOSITORIO>
  ```

2.  **Navegar até o Diretório:**
  Os arquivos estão na raiz do repositório.
  Exemplo no Windows: `cd "C:\caminho\para\repositório"`

3.  **Executar Cada Programa:**
  Use o comando `python` ou `python3`, dependendo da configuração do seu sistema.
  Exemplos:
  ```bash
  python soma_indice.py
  python fibonacci_checker.py
  python faturamento_diario.py
  python faturamento_percentual.py
  python inverter_string.py
  ```

4.  **Entradas Interativas:**
  - Para `fibonacci_checker.py`: Digite um número inteiro ou pressione Enter para usar o valor padrão (21).
  - Para `inverter_string.py`: Digite uma string ou pressione Enter para usar o valor padrão ("exemplo").

5.  **Dados Externos (Opcional):**
  - Para `faturamento_diario.py` e `faturamento_percentual.py`, você pode criar arquivos JSON (`faturamento.json` e `faturamento_estados.json`) e descomentar as linhas correspondentes no código.
  - **Estrutura esperada para `faturamento.json`:**
    ```json
    [
        {"dia": 1, "faturamento": 1000.0},
        {"dia": 2, "faturamento": 1500.0},
        ...
    ]
    ```
  - **Estrutura esperada para `faturamento_estados.json`:**
    ```json
    {
        "SP": 67836.43,
        "RJ": 36678.66,
        ...
    }
    ```

## Notas de Execução

- **Ambiente Windows:** Os programas foram testados no PowerShell e CMD. Recomenda-se usar o CMD como terminal integrado no VS Code para evitar problemas com entrada interativa.
- **Problemas com Entrada Interativa:** Se o `input()` não funcionar no VS Code, execute no PowerShell/CMD externo ou use valores fixos (editando o código).
Exemplo para `fibonacci_checker.py`:
```python
numero = 21  # Substituir a linha do input()
````
## Codificação:

- **Todos os arquivos estão em UTF-8. Evite acentos em mensagens para compatibilidade com terminais Windows.**
## Estrutura do Código

- Cada programa é independente e segue as restrições do enunciado.
- Comentários no código explicam a lógica principal.
- Funções prontas foram evitadas (ex.: min, max, sum, reverse, fatiamento [::-1]).
- Tratamento de erros foi implementado para entradas inválidas e arquivos JSON ausentes.

## Contato
Para dúvidas ou esclarecimentos, entre em contato via [(https://www.linkedin.com/in/moacirdsjr/)].

Nota: Este repositório foi criado como parte do processo seletivo para Desenvolvedor 2. O código reflete as melhores práticas e atende rigorosamente aos requisitos fornecidos.

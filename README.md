# Calculadora de Números Complexos

## Descrição

Calculadora científica para números complexos desenvolvida em Python. O projeto implementa um parser de expressões matemáticas, árvore sintática e avaliador para operações com números complexos.

## Funcionalidades

### Operações Suportadas

- **Aritméticas básicas**: `+`, `-`, `*`, `/`, `**`
- **Funções especiais**: `conj()` (conjugado), `raiz()` (raiz quadrada)
- **Números complexos**: Formato `a+bj` (ex: `3+4j`, `2-5j`, `7j`)
- **Variáveis**: Suporte a variáveis alfanuméricas
- **Parênteses**: Controle de precedência

### Recursos

- **Parser de expressões**: Converte notação infixa para pós-fixa
- **Árvore sintática**: Representação hierárquica das expressões
- **Notação LISP**: Exibe expressões em formato LISP
- **Comparação de expressões**: Verifica equivalência estrutural
- **Tratamento de erros**: Validação e mensagens de erro

## Como Usar

### Execução

```bash
python main.py
```

### Menu Principal

1. **Calcular expressão** - Avalia uma expressão matemática
2. **Sumário** - Exibe ajuda sobre operações disponíveis
3. **Sair** - Encerra o programa

### Exemplos de Uso

#### Números Complexos

```
3+4j
2-5j
7j
-3+2j
```

#### Operações Básicas

```
(3+4j) + (1+2j)
(2+3j) * (4-j)
(5+2j) / (1+j)
(3+4j) ** 2
```

#### Funções Especiais

```
conj(3+4j)          # Conjugado: (3-4j)
raiz(9)             # Raiz quadrada: (3+0j)
raiz(-4)            # Raiz de negativo: (0+2j)
```

#### Expressões Complexas

```
2 * conj(3+4j) + raiz(9)
(a + b) * conj(c)
raiz(conj(3+4j)) + 2
```

#### Variáveis

```
a + b * 2
conj(x) + raiz(y)
```

_O programa solicitará valores para as variáveis durante a execução_

## Estrutura do Projeto

```
A3_calculadora/
├── main.py          # Ponto de entrada
├── operacoes.py     # Interface e menu principal
├── tokenizer.py     # Análise léxica (tokenização)
├── parser.py        # Análise sintática (infixa → pós-fixa)
├── arvore.py        # Árvore de expressão
├── evaluator.py     # Avaliador de expressões
├── complexo.py      # Classe para números complexos
├── lisp.py          # Conversor para notação LISP
├── compare.py       # Comparador de árvores
└── README.md        # Este arquivo
```

## Arquitetura

### Fluxo de Processamento

1. **Tokenização**: Quebra a expressão em tokens
2. **Parsing**: Converte para notação pós-fixa (Algoritmo Shunting Yard)
3. **Árvore**: Constrói árvore sintática a partir da pós-fixa
4. **Avaliação**: Percorre a árvore e calcula o resultado
5. **LISP**: Gera representação em notação LISP

### Componentes Principais

#### Analisador (tokenizer.py)

- Reconhece números complexos, operadores, funções e variáveis
- Trata números negativos e sinais unários

#### AnalisadorSintatico (parser.py)

- Implementa algoritmo Shunting Yard
- Respeita precedência de operadores
- Trata funções unárias com parênteses

#### ArvoreExpressao (arvore.py)

- Constrói árvore binária a partir da notação pós-fixa
- Nós contêm operadores/funções, folhas contêm operandos

#### Avaliador (evaluator.py)

- Percorre árvore recursivamente
- Executa operações com números complexos
- Gerencia variáveis e suas atribuições

#### NumeroComplexo (complexo.py)

- Implementação própria de aritmética complexa
- Métodos: somar, subtrair, multiplicar, dividir, potencia
- Funções especiais: conjugado, raiz_quadrada

## Requisitos Técnicos

- **Python 3.7+**
- **Bibliotecas**: `math` (padrão do Python)
- **Sistema**: Windows/Linux/macOS

## Exemplos de Saída

```
Digite a expressão: (3+4j) * conj(3+4j)

--- EXPRESSÃO ---
(3+4j) * conj(3+4j)
Tokens: ['(', '3', '+', '4j', ')', '*', 'conj', '(', '3', '+', '4j', ')']
Pós-fixa: ['3', '4j', '+', '3', '4j', '+', 'conj', '*']
LISP: (* (+ 3 4j) (conj (+ 3 4j)))
Resultado: (25.0+0.0j)
```

## Tratamento de Erros

- **Divisão por zero**: Detecta e reporta
- **Parênteses desbalanceados**: Validação sintática
- **Tokens inválidos**: Caracteres não reconhecidos
- **Variáveis indefinidas**: Solicita valores automaticamente
- **Formato inválido**: Números complexos malformados

## Limitações

- Potenciação aceita apenas expoentes reais
- Funções limitadas a `conj()` e `raiz()`
- Comparação de expressões é estrutural, não matemática
- Interface apenas em linha de comando

## Desenvolvimento

Este projeto foi desenvolvido como trabalho acadêmico, implementando conceitos de:

- Análise léxica e sintática
- Estruturas de dados (árvores)
- Algoritmos de parsing
- Programação orientada a objetos
- Aritmética de números complexos

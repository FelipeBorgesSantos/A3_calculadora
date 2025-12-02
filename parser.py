class AnalisadorSintatico:
    """Converte os tokens para notação pós-fixa usando algoritmo Shunting Yard"""
    
    # Define a ordem de prioridade dos operadores (maior número = maior prioridade)
    PRECEDENCIA = {
        "+": 1, "-": 1,    # Soma e subtração têm menor prioridade
        "*": 2, "/": 2,    # Multiplicação e divisão têm prioridade média
        "**": 3             # Potência tem maior prioridade
    }

    def __init__(self, tokens):
        self.tokens = tokens

    def is_numero(self, token):
        """Verifica se um token é um número (real ou complexo)"""
        if not isinstance(token, str):
            return False
        
        # Só aceita caracteres válidos para números
        chars_validos = set('0123456789.+-j')
        if not all(c in chars_validos for c in token):
            return False
        
        # Tenta converter pra ver se é um número válido
        try:
            from complexo import NumeroComplexo
            NumeroComplexo.de_string(token)
            return True
        except ValueError:
            return False

    def is_funcao(self, token):
        """Verifica se é uma das funções que conhecemos"""
        return token in ["conj", "raiz"]

    def is_variavel(self, t):
        """Verifica se é uma variável (letra que não é função)"""
        if not isinstance(t, str) or not t:
            return False
        if not t[0].isalpha():  # Tem que começar com letra
            return False
        if not t.replace('_', '').isalnum():  # Pode ter letras, números e _
            return False
        return not self.is_funcao(t)  # Não pode ser função

    def para_posfixa(self):
        """Converte expressão infixa para pós-fixa (algoritmo Shunting Yard)"""
        saida = []   # Lista final com a expressão em pós-fixa
        pilha = []   # Pilha temporária para operadores

        for t in self.tokens:
            # Números e variáveis vão direto pra saída
            if self.is_numero(t) or self.is_variavel(t):
                saida.append(t)

            # Operadores: respeitam a precedência
            elif t in self.PRECEDENCIA:
                # Remove operadores de maior precedência da pilha
                while (pilha and pilha[-1] in self.PRECEDENCIA and
                       self.PRECEDENCIA[pilha[-1]] > self.PRECEDENCIA[t]):
                    saida.append(pilha.pop())
                pilha.append(t)

            # Parêntese que abre: vai pra pilha
            elif t == "(":
                pilha.append(t)

            # Parêntese que fecha: processa tudo até o que abre
            elif t == ")":
                while pilha and pilha[-1] != "(":
                    saida.append(pilha.pop())
                if not pilha:
                    raise ValueError("Parênteses desbalanceados")
                pilha.pop()  # Remove o "("
                
                # Se tem função esperando, processa ela agora
                if pilha and self.is_funcao(pilha[-1]):
                    saida.append(pilha.pop())

            # Funções: vão pra pilha e esperam seus argumentos
            elif self.is_funcao(t):
                pilha.append(t)

            # Se chegou aqui, é algo que não conhecemos
            else:
                raise ValueError(f"Símbolo inesperado: {t}")

        # Esvazia a pilha no final
        while pilha:
            if pilha[-1] == "(":
                raise ValueError("Parênteses desbalanceados")
            saida.append(pilha.pop())

        return saida

class AnalisadorSintatico:
    PRECEDENCIA = {
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "**": 3
    }

    def __init__(self, tokens):
        self.tokens = tokens

    def is_number(self, token):
        # Validação básica para formatos de número esperados
        if not isinstance(token, str):
            return False
        # Permite dígitos, ponto decimal, sinais +/- e 'j' para números complexos
        chars_validos = set('0123456789.+-j')
        if not all(c in chars_validos for c in token):
            return False
        try:
            complex(token)
            return True
        except ValueError:
            return False

    def is_funcao(self, token):
        return token in ["conj", "raiz"]

    def is_variavel(self, t):
        # Permite variáveis alfanuméricas começando com letra
        if not isinstance(t, str) or not t:
            return False
        if not t[0].isalpha():  # Deve começar com letra
            return False
        if not t.replace('_', '').isalnum():  # Permite letras, números e underscores
            return False
        return not self.is_funcao(t)

    def para_posfixa(self):
        saida = []
        pilha = []

        for t in self.tokens:
            if self.is_number(t) or self.is_variavel(t):
                saida.append(t)

            elif t in self.PRECEDENCIA:
                while (pilha and pilha[-1] in self.PRECEDENCIA and
                       self.PRECEDENCIA[pilha[-1]] > self.PRECEDENCIA[t]):
                    saida.append(pilha.pop())
                pilha.append(t)

            elif t == "(":
                pilha.append(t)

            elif t == ")":
                while pilha and pilha[-1] != "(":
                    saida.append(pilha.pop())
                if not pilha:
                    raise ValueError("Parênteses desbalanceados")
                pilha.pop()

            elif self.is_funcao(t):
                pilha.append(t)

            else:
                raise ValueError(f"Símbolo inesperado: {t}")

        while pilha:
            if pilha[-1] == "(":
                raise ValueError("Parênteses desbalanceados")
            saida.append(pilha.pop())

        return saida

class Analisador:
    def __init__(self, expressao):
        self.expressao = expressao

    def _processar_numero(self, pos_inicial, char_inicial=""):
        """Processa um número a partir da posição dada"""
        numero = char_inicial
        i = pos_inicial
        tem_ponto = char_inicial == "."
        tem_j = False
        
        while i < len(self.expressao) and (self.expressao[i].isdigit() or 
              (self.expressao[i] == "." and not tem_ponto) or 
              (self.expressao[i] == "j" and not tem_j)):
            if self.expressao[i] == ".":
                tem_ponto = True
            elif self.expressao[i] == "j":
                tem_j = True
            numero += self.expressao[i]
            i += 1
        
        return numero, i

    def tokenizar(self):
        tokens = []
        i = 0
        while i < len(self.expressao):

            if self.expressao[i].isspace():
                i += 1
                continue

            # operador de potência **
            if self.expressao[i:i+2] == "**":
                tokens.append("**")
                i += 2
                continue

            # sinal unário (+ ou - no início ou após operador/parêntese)
            if self.expressao[i] in "+-" and (not tokens or tokens[-1] in "(+-*/)" or tokens[-1] == "**") and \
               i + 1 < len(self.expressao) and (self.expressao[i+1].isdigit() or self.expressao[i+1] == "."):
                num, i = self._processar_numero(i + 1, self.expressao[i])
                tokens.append(num)
                continue

            # operadores simples
            if self.expressao[i] in "+-*/()":
                tokens.append(self.expressao[i])
                i += 1
                continue

            # número complexo ou real
            if self.expressao[i].isdigit() or self.expressao[i] == ".":
                num, i = self._processar_numero(i + 1, self.expressao[i])
                tokens.append(num)
                continue

            # variáveis e funções (conj, raiz)
            if self.expressao[i].isalpha():
                nome = self.expressao[i]
                i += 1
                while i < len(self.expressao) and self.expressao[i].isalnum():
                    nome += self.expressao[i]
                    i += 1
                tokens.append(nome)
                continue

            raise ValueError(f"Token inválido na posição {i}: {self.expressao[i]}")

        return tokens

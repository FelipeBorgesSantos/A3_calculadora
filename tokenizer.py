class Analisador:
    """Classe que quebra uma expressão em pedaços (tokens)"""
    
    def __init__(self, expressao):
        self.expressao = expressao

    def _processar_numero(self, pos_inicial, char_inicial=""):
        """Lê um número completo (pode ser complexo como 3.5j)"""
        numero = char_inicial
        i = pos_inicial
        tem_ponto = char_inicial == "."
        tem_j = False
        
        # Continua lendo enquanto for dígito, ponto ou 'j'
        while i < len(self.expressao) and (self.expressao[i].isdigit() or 
              (self.expressao[i] == "." and not tem_ponto) or 
              (self.expressao[i] == "j" and not tem_j)):
            if self.expressao[i] == ".":
                tem_ponto = True  # Só permite um ponto
            elif self.expressao[i] == "j":
                tem_j = True      # Só permite um 'j'
            numero += self.expressao[i]
            i += 1
        
        return numero, i

    def tokenizar(self):
        """Método principal que quebra a expressão em tokens"""
        tokens = []
        i = 0
        
        # Percorre a expressão caractere por caractere
        while i < len(self.expressao):

            # Pula espaços em branco
            if self.expressao[i].isspace():
                i += 1
                continue

            # Operador de potência ** (tem que vir antes do * simples)
            if self.expressao[i:i+2] == "**":
                tokens.append("**")
                i += 2
                continue

            # Números negativos (como -5 ou -3.2j)
            if self.expressao[i] in "+-" and (not tokens or tokens[-1] in "(+-*/)" or tokens[-1] == "**") and \
               i + 1 < len(self.expressao) and (self.expressao[i+1].isdigit() or self.expressao[i+1] == "."):
                num, i = self._processar_numero(i + 1, self.expressao[i])
                tokens.append(num)
                continue

            # Operadores e parênteses
            if self.expressao[i] in "+-*/()":
                tokens.append(self.expressao[i])
                i += 1
                continue

            # Números (reais ou complexos)
            if self.expressao[i].isdigit() or self.expressao[i] == ".":
                num, i = self._processar_numero(i + 1, self.expressao[i])
                tokens.append(num)
                continue

            # Variáveis e funções (a, b, conj, raiz, etc)
            if self.expressao[i].isalpha():
                nome = self.expressao[i]
                i += 1
                # Continua lendo o nome completo
                while i < len(self.expressao) and self.expressao[i].isalnum():
                    nome += self.expressao[i]
                    i += 1
                tokens.append(nome)
                continue

            # Se chegou aqui, é um caractere que não reconhecemos
            raise ValueError(f"Token inválido na posição {i}: {self.expressao[i]}")

        return tokens

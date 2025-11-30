class Tokenizer:
    def __init__(self, expr):
        self.expr = expr

    def _parse_number(self, start_pos, initial_char=""):
        """Parse a number starting at the given position"""
        num = initial_char
        i = start_pos
        has_dot = initial_char == "."
        has_j = False
        
        while i < len(self.expr) and (self.expr[i].isdigit() or 
              (self.expr[i] == "." and not has_dot) or 
              (self.expr[i] == "j" and not has_j)):
            if self.expr[i] == ".":
                has_dot = True
            elif self.expr[i] == "j":
                has_j = True
            num += self.expr[i]
            i += 1
        
        return num, i

    def tokenize(self):
        tokens = []
        i = 0
        while i < len(self.expr):

            if self.expr[i].isspace():
                i += 1
                continue

            # operador de potência **
            if self.expr[i:i+2] == "**":
                tokens.append("**")
                i += 2
                continue

            # sinal unário (+ ou - no início ou após operador/parêntese)
            if self.expr[i] in "+-" and (not tokens or tokens[-1] in "(+-*/)" or tokens[-1] == "**") and \
               i + 1 < len(self.expr) and (self.expr[i+1].isdigit() or self.expr[i+1] == "."):
                num, i = self._parse_number(i + 1, self.expr[i])
                tokens.append(num)
                continue

            # operadores simples
            if self.expr[i] in "+-*/()":
                tokens.append(self.expr[i])
                i += 1
                continue

            # número complexo ou real
            if self.expr[i].isdigit() or self.expr[i] == ".":
                num, i = self._parse_number(i + 1, self.expr[i])
                tokens.append(num)
                continue

            # variáveis e funções (conj, raiz)
            if self.expr[i].isalpha():
                name = self.expr[i]
                i += 1
                while i < len(self.expr) and self.expr[i].isalnum():
                    name += self.expr[i]
                    i += 1
                tokens.append(name)
                continue

            raise ValueError(f"Token inválido na posição {i}: {self.expr[i]}")

        return tokens

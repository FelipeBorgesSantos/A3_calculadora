
# tokenizer.py

class Tokenizer:
    def __init__(self, expr):
        self.expr = expr

    def tokenize(self):
        tokens = []
        i = 0
        e = self.expr

        while i < len(e):

            if e[i].isspace():
                i += 1
                continue

            # operadores simples
            if e[i] in "+-*/()":
                tokens.append(e[i])
                i += 1
                continue

            # operador de potência **
            if e[i:i+2] == "**":
                tokens.append("**")
                i += 2
                continue

            # número complexo ou real
            if e[i].isdigit() or e[i] in "+-.":
                num = e[i]
                i += 1
                while i < len(e) and (e[i].isdigit() or e[i] in ".+-j"):
                    num += e[i]
                    i += 1
                tokens.append(num)
                continue

            # variáveis e funções (conj, raiz)
            if e[i].isalpha():
                name = e[i]
                i += 1
                while i < len(e) and e[i].isalnum():
                    name += e[i]
                    i += 1
                tokens.append(name)
                continue

            raise Exception(f"Token inválido: {e[i]}")

        return tokens

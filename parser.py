# parser.py

class Parser:
    PRECEDENCIA = {
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "**": 3
    }

    def __init__(self, tokens):
        self.tokens = tokens

    def is_number(self, token):
        try:
            complex(token)
            return True
        except:
            return False

    def is_function(self, token):
        return token in ["conj", "raiz"]

    def is_variable(self, t):
        return t.isalpha() and not self.is_function(t)

    def to_postfix(self):
        output = []
        stack = []

        for t in self.tokens:
            if self.is_number(t) or self.is_variable(t):
                output.append(t)

            elif t in self.PRECEDENCIA:
                while (stack and stack[-1] in self.PRECEDENCIA and
                       self.PRECEDENCIA[stack[-1]] >= self.PRECEDENCIA[t]):
                    output.append(stack.pop())
                stack.append(t)

            elif t == "(":
                stack.append(t)

            elif t == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()

            elif self.is_function(t):
                stack.append(t)

            else:
                raise Exception(f"Símbolo inesperado: {t}")

        while stack:
            output.append(stack.pop())

        return output

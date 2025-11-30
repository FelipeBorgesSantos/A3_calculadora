class Parser:
    PRECEDENCE = {
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "**": 3
    }

    def __init__(self, tokens):
        self.tokens = tokens

    def is_number(self, token):
        # Basic validation for expected number formats
        if not isinstance(token, str):
            return False
        # Allow digits, decimal point, minus/plus signs, and 'j' for complex numbers
        valid_chars = set('0123456789.+-j')
        if not all(c in valid_chars for c in token):
            return False
        try:
            complex(token)
            return True
        except ValueError:
            return False

    def is_function(self, token):
        return token in ["conj", "raiz"]

    def is_variable(self, t):
        # Allow alphanumeric variables starting with a letter
        if not isinstance(t, str) or not t:
            return False
        if not t[0].isalpha():  # Must start with a letter
            return False
        if not t.replace('_', '').isalnum():  # Allow letters, numbers, and underscores
            return False
        return not self.is_function(t)

    def to_postfix(self):
        output = []
        stack = []

        for t in self.tokens:
            if self.is_number(t) or self.is_variable(t):
                output.append(t)

            elif t in self.PRECEDENCE:
                while (stack and stack[-1] in self.PRECEDENCE and
                       self.PRECEDENCE[stack[-1]] > self.PRECEDENCE[t]):
                    output.append(stack.pop())
                stack.append(t)

            elif t == "(":
                stack.append(t)

            elif t == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                if not stack:
                    raise ValueError("Parênteses desbalanceados")
                stack.pop()

            elif self.is_function(t):
                stack.append(t)

            else:
                raise ValueError(f"Símbolo inesperado: {t}")

        while stack:
            if stack[-1] == "(":
                raise ValueError("Parênteses desbalanceados")
            output.append(stack.pop())

        return output

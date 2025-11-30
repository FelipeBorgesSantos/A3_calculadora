class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class ExpressionTree:
    FUNCTIONS = ["conj", "raiz"]
    OPERATORS = ["+", "-", "*", "/", "**"]

    @staticmethod
    def is_function(token):
        return token in ExpressionTree.FUNCTIONS

    @staticmethod
    def from_postfix(postfix):
        stack = []

        for token in postfix:

            # função unária
            if ExpressionTree.is_function(token):
                if not stack:
                    raise ValueError("Expressão malformada: funç��o sem operando")
                child = stack.pop()
                stack.append(Node(token, left=child))

            # número ou variável
            elif ExpressionTree.is_number(token) or token.isalpha():
                stack.append(Node(token))

            elif token in ExpressionTree.OPERATORS:
                # operador binário
                if len(stack) < 2:
                    raise ValueError("Expressão malformada: operador sem operandos suficientes")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
            else:
                raise ValueError(f"Token desconhecido: {token}")

        if len(stack) != 1:
            raise ValueError("Expressão malformada: resultado inválido")
        return stack[0]

    @staticmethod
    def is_number(t):
        try:
            complex(t)
            return True
        except (ValueError, TypeError):
            return False

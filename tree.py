# tree.py

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class ExpressionTree:
    FUNCTIONS = ["conj", "raiz"]

    @staticmethod
    def is_function(token):
        return token in ExpressionTree.FUNCTIONS

    @staticmethod
    def from_postfix(postfix):
        stack = []

        for token in postfix:

            # número ou variável
            if ExpressionTree.is_number(token):
                stack.append(Node(token))

            # função unária
            elif ExpressionTree.is_function(token):
                child = stack.pop()
                stack.append(Node(token, left=child))

            else:  
                # operador binário
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))

        return stack[-1]

    @staticmethod
    def is_number(t):
        try:
            complex(t)
            return True
        except:
            return False

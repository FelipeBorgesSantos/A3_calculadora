# evaluator.py

import cmath

class Evaluator:

    @staticmethod
    def evaluate(node, variables):

        # número
        try:
            return complex(node.value)
        except:
            pass

        # variável
        if node.value.isalpha() and node.value not in ("conj", "raiz"):
            return variables[node.value]

        # recursão
        a = Evaluator.evaluate(node.left, variables) if node.left else None
        b = Evaluator.evaluate(node.right, variables) if node.right else None

        op = node.value

        match op:
            case "+":  return a + b
            case "-":  return a - b
            case "*":  return a * b
            case "/":
                if b == 0:
                    raise Exception("Divisão por zero!")
                return a / b
            case "**": return a ** b
            case "conj": return a.conjugate()
            case "raiz": return cmath.sqrt(a)

        raise Exception(f"Operador desconhecido: {op}")

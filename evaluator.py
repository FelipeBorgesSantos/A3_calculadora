import cmath

class Evaluator:
    FUNCTIONS = {"conj", "raiz"}

    @staticmethod
    def _validate_operands(op, a, b=None):
        if op in ["+", "-", "*", "/", "**"] and (a is None or b is None):
            raise ValueError("Operandos inválidos")
        if op in ["conj", "raiz"] and a is None:
            raise ValueError("Operando inválido")

    @staticmethod
    def evaluate(node, variables):
        if node is None or not hasattr(node, 'value'):
            raise ValueError("Nó inválido")

        # número
        try:
            return complex(node.value)
        except (ValueError, TypeError):
            pass

        # variável
        if node.value.isalpha() and node.value not in Evaluator.FUNCTIONS:
            if node.value not in variables:
                raise ValueError(f"Variável '{node.value}' não definida")
            return variables[node.value]

        # recursão
        a = Evaluator.evaluate(node.left, variables) if node.left else None
        b = Evaluator.evaluate(node.right, variables) if node.right else None

        op = node.value
        Evaluator._validate_operands(op, a, b)
            
        match op:
            case "+":  return a + b
            case "-":  return a - b
            case "*":  return a * b
            case "/":
                if b == 0:
                    raise ZeroDivisionError("Divisão por zero!")
                return a / b
            case "**": return a ** b
            case "conj": return a.conjugate()
            case "raiz": return cmath.sqrt(a)

        raise ValueError(f"Operador desconhecido: {op}")

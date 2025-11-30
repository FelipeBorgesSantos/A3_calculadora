import cmath

class Avaliador:
    FUNCOES = {"conj", "raiz"}

    @staticmethod
    def _validar_operandos(op, a, b=None):
        if op in ["+", "-", "*", "/", "**"] and (a is None or b is None):
            raise ValueError("Operandos inválidos")
        if op in ["conj", "raiz"] and a is None:
            raise ValueError("Operando inválido")

    @staticmethod
    def avaliar(no, variaveis):
        if no is None or not hasattr(no, 'valor'):
            raise ValueError("Nó inválido")

        # número
        try:
            return complex(no.valor)
        except (ValueError, TypeError):
            pass

        # variável
        if no.valor.isalpha() and no.valor not in Avaliador.FUNCOES:
            if no.valor not in variaveis:
                raise ValueError(f"Variável '{no.valor}' não definida")
            return variaveis[no.valor]

        # recursão
        a = Avaliador.avaliar(no.esquerda, variaveis) if no.esquerda else None
        b = Avaliador.avaliar(no.direita, variaveis) if no.direita else None

        op = no.valor
        Avaliador._validar_operandos(op, a, b)
            
        match op:
            case "+":  return a + b
            case "-":  return a - b
            case "*":  return a * b
            case "/":
                if abs(b) < 1e-10:
                    raise ZeroDivisionError("Divisão por zero!")
                return a / b
            case "**": return a ** b
            case "conj": return a.conjugate()
            case "raiz": return cmath.sqrt(a)

        raise ValueError(f"Operador desconhecido: {op}")

from complexo import NumeroComplexo

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
            return NumeroComplexo.de_string(str(no.valor))
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
            case "+":  return a.somar(b)
            case "-":  return a.subtrair(b)
            case "*":  return a.multiplicar(b)
            case "/":  return a.dividir(b)
            case "**": return a.potencia(b.real if hasattr(b, 'real') else b)
            case "conj": return a.conjugado()
            case "raiz": return a.raiz_quadrada()

        raise ValueError(f"Operador desconhecido: {op}")

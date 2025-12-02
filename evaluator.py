from complexo import NumeroComplexo

class Avaliador:
    """Classe que percorre a árvore e calcula o resultado final"""
    
    FUNCOES = {"conj", "raiz"}

    @staticmethod
    def _validar_operandos(op, a, b=None):
        """Verifica se os operandos estão corretos para cada operação"""
        # Operações binárias precisam de dois operandos
        if op in ["+", "-", "*", "/", "**"] and (a is None or b is None):
            raise ValueError("Operandos inválidos")
        # Funções unárias precisam de um operando
        if op in ["conj", "raiz"] and a is None:
            raise ValueError("Operando inválido")

    @staticmethod
    def avaliar(no, variaveis):
        """Método principal que percorre a árvore e calcula tudo"""
        if no is None or not hasattr(no, 'valor'):
            raise ValueError("Nó inválido")

        # Caso 1: é um número (folha da árvore)
        try:
            return NumeroComplexo.de_string(str(no.valor))
        except (ValueError, TypeError):
            pass

        # Caso 2: é uma variável (folha da árvore)
        if no.valor.isalpha() and no.valor not in Avaliador.FUNCOES:
            if no.valor not in variaveis:
                raise ValueError(f"Variável '{no.valor}' não definida")
            return variaveis[no.valor]

        # Caso 3: é um operador ou função (nó interno)
        # Primeiro calcula os filhos recursivamente
        a = Avaliador.avaliar(no.esquerda, variaveis) if no.esquerda else None
        b = Avaliador.avaliar(no.direita, variaveis) if no.direita else None

        op = no.valor
        Avaliador._validar_operandos(op, a, b)
        
        # Agora executa a operação
        if op == "+":
            return a.somar(b)
        elif op == "-":
            return a.subtrair(b)
        elif op == "*":
            return a.multiplicar(b)
        elif op == "/":
            return a.dividir(b)
        elif op == "**":
            # Potência só aceita expoente real
            return a.potencia(b.real if hasattr(b, 'real') else b)
        elif op == "conj":
            return a.conjugado()
        elif op == "raiz":
            return a.raiz_quadrada()

        # Se chegou aqui, é um operador que não conhecemos
        raise ValueError(f"Operador desconhecido: {op}")

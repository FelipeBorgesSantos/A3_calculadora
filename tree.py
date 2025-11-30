class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


class ArvoreExpressao:
    FUNCOES = ["conj", "raiz"]
    OPERADORES = ["+", "-", "*", "/", "**"]

    @staticmethod
    def eh_funcao(token):
        return token in ArvoreExpressao.FUNCOES

    @staticmethod
    def criar_de_posfixa(posfixa):
        pilha = []

        for token in posfixa:

            # função unária
            if ArvoreExpressao.eh_funcao(token):
                if not pilha:
                    raise ValueError("Expressão malformada: função sem operando")
                filho = pilha.pop()
                pilha.append(No(token, esquerda=filho))

            # número ou variável  
            elif not ArvoreExpressao.eh_funcao(token) and not token in ArvoreExpressao.OPERADORES:
                pilha.append(No(token))

            elif token in ArvoreExpressao.OPERADORES:
                # operador binário
                if len(pilha) < 2:
                    raise ValueError("Expressão malformada: operador sem operandos suficientes")
                direita = pilha.pop()
                esquerda = pilha.pop()
                pilha.append(No(token, esquerda, direita))
            else:
                raise ValueError(f"Token desconhecido: {token}")

        if len(pilha) != 1:
            raise ValueError("Expressão malformada: resultado inválido")
        return pilha[0]
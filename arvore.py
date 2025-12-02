class No:
    """Representa um nó da árvore (pode ser número, variável, operador ou função)"""
    
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor        # O que está neste nó (número, +, -, conj, etc)
        self.esquerda = esquerda  # Filho da esquerda
        self.direita = direita    # Filho da direita


class ArvoreExpressao:
    """Classe que monta a árvore da expressão a partir da notação pós-fixa"""
    
    FUNCOES = ["conj", "raiz"]
    OPERADORES = ["+", "-", "*", "/", "**"]

    @staticmethod
    def eh_funcao(token):
        """Verifica se o token é uma função"""
        return token in ArvoreExpressao.FUNCOES

    @staticmethod
    def criar_de_posfixa(posfixa):
        """Monta a árvore a partir da expressão em notação pós-fixa"""
        pilha = []  # Pilha de nós da árvore

        for token in posfixa:

            # Funções (conj, raiz) - pegam um operando
            if ArvoreExpressao.eh_funcao(token):
                if not pilha:
                    raise ValueError("Expressão malformada: função sem operando")
                filho = pilha.pop()  # Pega o operando
                # Função fica na raiz, operando à esquerda
                pilha.append(No(token, esquerda=filho))

            # Números e variáveis - viram folhas da árvore
            elif not ArvoreExpressao.eh_funcao(token) and not token in ArvoreExpressao.OPERADORES:
                pilha.append(No(token))  # Nó sem filhos

            # Operadores (+, -, *, /, **) - pegam dois operandos
            elif token in ArvoreExpressao.OPERADORES:
                if len(pilha) < 2:
                    raise ValueError("Expressão malformada: operador sem operandos suficientes")
                # Em pós-fixa, o último é o da direita
                direita = pilha.pop()
                esquerda = pilha.pop()
                # Operador fica na raiz, operandos nos filhos
                pilha.append(No(token, esquerda, direita))
            
            # Token que não conhecemos
            else:
                raise ValueError(f"Token desconhecido: {token}")

        # No final deve sobrar exatamente um nó (a raiz da árvore)
        if len(pilha) != 1:
            raise ValueError("Expressão malformada: resultado inválido")
        return pilha[0]
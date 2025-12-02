class ConversorLisp:
    """Converte a árvore de expressão para notação LISP"""
    
    @staticmethod
    def to_lisp(no):
        """Percorre a árvore e gera a representação em LISP"""
        # Nó vazio
        if no is None:
            return ""
        
        # Verifica se o nó é válido
        if getattr(no, 'valor', None) is None:
            raise ValueError("Nó deve ter atributo 'valor'")
        
        # Folha da árvore (número ou variável)
        if getattr(no, 'esquerda', None) is None and getattr(no, 'direita', None) is None:
            return str(no.valor)

        # Função unária (só tem filho à esquerda)
        if getattr(no, 'direita', None) is None:
            return f"({no.valor} {ConversorLisp.to_lisp(no.esquerda)})"

        # Operador binário (tem dois filhos)
        return f"({no.valor} {ConversorLisp.to_lisp(no.esquerda)} {ConversorLisp.to_lisp(no.direita)})"

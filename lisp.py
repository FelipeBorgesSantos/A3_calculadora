class ConversorLisp:
    @staticmethod
    def to_lisp(no):
        if no is None:
            return ""
        if getattr(no, 'valor', None) is None:
            raise ValueError("Nó deve ter atributo 'valor'")
            
        if getattr(no, 'esquerda', None) is None and getattr(no, 'direita', None) is None:
            return str(no.valor)

        if getattr(no, 'direita', None) is None:
            return f"({no.valor} {ConversorLisp.to_lisp(no.esquerda)})"

        return f"({no.valor} {ConversorLisp.to_lisp(no.esquerda)} {ConversorLisp.to_lisp(no.direita)})"

class Comparador:
    @staticmethod
    def equal(a, b, profundidade=0):
        if profundidade > 1000:
            return False
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if type(a) != type(b):
            return False
        if not (hasattr(a, 'valor') and hasattr(b, 'valor')):
            return False
        if a.valor != b.valor:
            return False
        a_esq = a.esquerda if hasattr(a, 'esquerda') else None
        b_esq = b.esquerda if hasattr(b, 'esquerda') else None
        a_dir = a.direita if hasattr(a, 'direita') else None
        b_dir = b.direita if hasattr(b, 'direita') else None
        
        return (Comparador.equal(a_esq, b_esq, profundidade + 1) and 
                Comparador.equal(a_dir, b_dir, profundidade + 1))

class Comparador:
    """Compara duas árvores de expressão para ver se são estruturalmente iguais"""
    
    @staticmethod
    def equal(a, b, profundidade=0):
        """Compara dois nós recursivamente (comparação estrutural, não matemática)"""
        
        # Evita recursão infinita
        if profundidade > 1000:
            return False
        
        # Ambos são None - são iguais
        if a is None and b is None:
            return True
        
        # Um é None e outro não - são diferentes
        if a is None or b is None:
            return False
        
        # Tipos diferentes - são diferentes
        if type(a) != type(b):
            return False
        
        # Verifica se ambos têm o atributo 'valor'
        if not (hasattr(a, 'valor') and hasattr(b, 'valor')):
            return False
        
        # Valores diferentes - são diferentes
        if a.valor != b.valor:
            return False
        
        # Pega os filhos (pode ser None)
        a_esq = a.esquerda if hasattr(a, 'esquerda') else None
        b_esq = b.esquerda if hasattr(b, 'esquerda') else None
        a_dir = a.direita if hasattr(a, 'direita') else None
        b_dir = b.direita if hasattr(b, 'direita') else None
        
        # Compara recursivamente os filhos
        return (Comparador.equal(a_esq, b_esq, profundidade + 1) and 
                Comparador.equal(a_dir, b_dir, profundidade + 1))

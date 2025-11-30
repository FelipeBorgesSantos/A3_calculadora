class Compare:
    @staticmethod
    def equal(a, b, depth=0):
        if depth > 1000:
            return False
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if type(a) != type(b):
            return False
        if not (hasattr(a, 'value') and hasattr(b, 'value')):
            return False
        if a.value != b.value:
            return False
        a_left = a.left if hasattr(a, 'left') else None
        b_left = b.left if hasattr(b, 'left') else None
        a_right = a.right if hasattr(a, 'right') else None
        b_right = b.right if hasattr(b, 'right') else None
        
        return (Compare.equal(a_left, b_left, depth + 1) and 
                Compare.equal(a_right, b_right, depth + 1))

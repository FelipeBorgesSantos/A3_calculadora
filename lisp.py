class Lisp:
    @staticmethod
    def to_lisp(node):
        if node is None:
            return ""
        if getattr(node, 'value', None) is None:
            raise ValueError("Node must have a 'value' attribute")
            
        if getattr(node, 'left', None) is None and getattr(node, 'right', None) is None:
            return str(node.value)

        if getattr(node, 'right', None) is None:
            return f"({node.value} {Lisp.to_lisp(node.left)})"

        return f"({node.value} {Lisp.to_lisp(node.left)} {Lisp.to_lisp(node.right)})"

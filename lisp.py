# lisp.py

class Lisp:
    @staticmethod
    def to_lisp(node):
        if node.left is None and node.right is None:
            return str(node.value)

        if node.right is None:
            return f"({node.value} {Lisp.to_lisp(node.left)})"

        return f"({node.value} {Lisp.to_lisp(node.left)} {Lisp.to_lisp(node.right)})"

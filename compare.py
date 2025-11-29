# compare.py

class Compare:
    @staticmethod
    def equal(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.value != b.value:
            return False
        return Compare.equal(a.left, b.left) and Compare.equal(a.right, b.right)

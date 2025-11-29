# main.py

from tokenizer import Tokenizer
from parser import Parser
from tree import ExpressionTree
from evaluator import Evaluator
from lisp import Lisp
from compare import Compare


def process_expression(expr):
    print("\n--- EXPRESSÃO ---")
    print(expr)

    tokens = Tokenizer(expr).tokenize()
    print("Tokens:", tokens)

    postfix = Parser(tokens).to_postfix()
    print("Postfix:", postfix)

    tree = ExpressionTree.from_postfix(postfix)

    print("LISP:", Lisp.to_lisp(tree))

    # variáveis
    vars = {}
    for t in tokens:
        if t.isalpha() and t not in ("conj", "raiz"):
            if t not in vars:
                vars[t] = complex(input(f"Valor para variável {t}: "))

    result = Evaluator.evaluate(tree, vars)
    print("Resultado:", result)

    return tree


if __name__ == "__main__":
    print("=== CALCULADORA COMPLEXA ===")

    e1 = input("\nDigite a primeira expressão: ")
    t1 = process_expression(e1)

    e2 = input("\nDigite a segunda expressão: ")
    t2 = process_expression(e2)

    print("\nAs expressões são equivalentes?")
    print(Compare.equal(t1, t2))
3
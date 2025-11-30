from tokenizer import Tokenizer
from parser import Parser
from tree import ExpressionTree
from evaluator import Evaluator
from lisp import Lisp
from compare import Compare

FUNCTIONS = {"conj", "raiz"}


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
        if t.isalpha() and t not in FUNCTIONS:
            if t not in vars:
                while True:
                    try:
                        user_input = input(f"Valor para variável {t} (ou 'skip' para pular): ")
                        if user_input.lower() == 'skip':
                            print(f"Aviso: Variável '{t}' será definida como 0")
                            vars[t] = 0
                            break
                        vars[t] = complex(user_input)
                        break
                    except ValueError:
                        print("Formato inválido. Use: 3+4j ou 5 ou 2j, ou 'skip' para pular")

    result = Evaluator.evaluate(tree, vars)
    print("Resultado:", result)

    return tree


if __name__ == "__main__":
    print("=== CALCULADORA COMPLEXA ===")

    try:
        e1 = input("\nDigite a primeira expressão: ")
        try:
            t1 = process_expression(e1)
        except Exception as e:
            print(f"Erro ao processar primeira expressão: {e}")

        e2 = input("\nDigite a segunda expressão: ")
        try:
            t2 = process_expression(e2)
        except Exception as e:
            print(f"Erro ao processar segunda expressão: {e}")

        print("\nAs expressões são equivalentes?")
        print(Compare.equal(t1, t2))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Erro: {e}")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
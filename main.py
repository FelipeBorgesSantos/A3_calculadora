from tokenizer import Analisador
from parser import AnalisadorSintatico
from tree import ArvoreExpressao
from evaluator import Avaliador
from lisp import ConversorLisp
from compare import Comparador

FUNCOES = {"conj", "raiz"}


def processar_expressao(expr):
    print("\n--- EXPRESSÃO ---")
    print(expr)

    tokens = Analisador(expr).tokenizar()
    print("Tokens:", tokens)

    posfixa = AnalisadorSintatico(tokens).para_posfixa()
    print("Pós-fixa:", posfixa)

    arvore = ArvoreExpressao.criar_de_posfixa(posfixa)

    print("LISP:", ConversorLisp.to_lisp(arvore))

    # variáveis
    variaveis = {}
    for t in tokens:
        if t.isalpha() and t not in FUNCOES:
            if t not in variaveis:
                while True:
                    try:
                        entrada = input(f"Valor para variável {t} (ou 'pular' para definir como 0): ")
                        if entrada.lower() == 'pular':
                            print(f"Aviso: Variável '{t}' será definida como 0")
                            variaveis[t] = 0
                            break
                        variaveis[t] = complex(entrada)
                        break
                    except ValueError:
                        print("Formato inválido. Use: 3+4j ou 5 ou 2j, ou 'pular'")

    resultado = Avaliador.avaliar(arvore, variaveis)
    print("Resultado:", resultado)

    return arvore


if __name__ == "__main__":
    print("=== CALCULADORA DE NÚMEROS COMPLEXOS ===")

    try:
        expr1 = input("\nDigite a primeira expressão: ")
        try:
            arvore1 = processar_expressao(expr1)
        except Exception as e:
            print(f"Erro na primeira expressão: {e}")
            exit()

        expr2 = input("\nDigite a segunda expressão: ")
        try:
            arvore2 = processar_expressao(expr2)
        except Exception as e:
            print(f"Erro na segunda expressão: {e}")
            exit()

        print("\nAs expressões são equivalentes?")
        print("Sim" if Comparador.equal(arvore1, arvore2) else "Não")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Erro: {e}")
    except KeyboardInterrupt:
        print("\nPrograma interrompido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
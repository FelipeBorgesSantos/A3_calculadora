from tokenizer import Analisador
from parser import AnalisadorSintatico
from arvore import ArvoreExpressao
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
    from complexo import NumeroComplexo
    variaveis = {}
    for t in tokens:
        if t.isalpha() and t not in FUNCOES:
            if t not in variaveis:
                while True:
                    try:
                        entrada = input(f"Valor para variável {t} (ou 'pular' para definir como 0): ")
                        if entrada.lower() == 'pular':
                            print(f"Aviso: Variável '{t}' será definida como 0")
                            variaveis[t] = NumeroComplexo(0, 0)
                            break
                        variaveis[t] = NumeroComplexo.de_string(entrada)
                        break
                    except ValueError:
                        print("Formato inválido. Use: 3+4j ou 5 ou 2j, ou 'pular'")

    resultado = Avaliador.avaliar(arvore, variaveis)
    print("Resultado:", resultado)

    return arvore


def iniciar_menu():
    cmd = ''
   
    print("---> CALCULADORA DE NÚMEROS COMPLEXOS <---")

    while cmd != 0:
        print("\nOpções:\n1 - Calcular expressão\n2 - Sumário \n0 - Sair")
        cmd = int(input("Digite a opção: "))

        if cmd == 1:
            try:
                expr = input("\nDigite a expressão: ")
                arvore = processar_expressao(expr)
            except (ValueError, ZeroDivisionError) as e:
                print(f"Erro: {e}")
            except KeyboardInterrupt:
                print("\nPrograma interrompido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            cmd_comparar = input("\nDeseja comparar com outra expressão? (s/n): ")

            if cmd_comparar.lower() == 's':
                expr2 = input("\nDigite a segunda expressão: ")
                try:
                    arvore2 = processar_expressao(expr2)
                except Exception as e:
                    print(f"Erro na segunda expressão: {e}")
                    exit()

                print("\nAs expressões são equivalentes?")
                print("Sim" if Comparador.equal(arvore, arvore2) else "Não")
            elif cmd_comparar.lower() == 'n':
                print("Retornando para o menu inicial...")
                continue
            else:
                print("Opção inválida. Retornando para o menu inicial.")
        elif cmd == 0:
            print("Programa Encerrado!")
        elif cmd == 2:
            print("\n--> Sumário <--")
            print("\n1 - Cálculos possíveis:\nsoma (+)\nsubtração (-)\nMultiplicação (*)\nDivisão (/)\nPotenciação (**) ")
            print("2 - Utilize espaços entre números e operadores")
            print("3 - Para calcular conjugado utilize: conj(valor)")
            print("4 - Para calcular raiz quadrada utilize: raiz(valor)")
            
        else:
            print("Opção inválida. Tente novamente.")
            

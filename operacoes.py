# Importa todas as classes que vamos usar
from tokenizer import Analisador
from parser import AnalisadorSintatico
from arvore import ArvoreExpressao
from evaluator import Avaliador
from lisp import ConversorLisp
from compare import Comparador

# Lista das funções que o programa reconhece
FUNCOES = {"conj", "raiz"}


def processar_expressao(expr):
    """Processa uma expressão matemática do início ao fim"""
    print("\n--- EXPRESSÃO ---")
    print(expr)

    # Primeiro passo: quebra a expressão em pedaços (tokens)
    tokens = Analisador(expr).tokenizar()
    print("Tokens:", tokens)

    # Segundo passo: converte para notação pós-fixa (mais fácil de calcular)
    posfixa = AnalisadorSintatico(tokens).para_posfixa()
    print("Pós-fixa:", posfixa)

    # Terceiro passo: monta a árvore da expressão
    arvore = ArvoreExpressao.criar_de_posfixa(posfixa)

    # Mostra como fica em notação LISP (requisito do trabalho)
    print("LISP:", ConversorLisp.to_lisp(arvore))

    # Procura por variáveis na expressão e pede valores pro usuário
    from complexo import NumeroComplexo
    variaveis = {}
    for t in tokens:
        # Se é uma letra e não é função (conj/raiz), então é variável
        if t.isalpha() and t not in FUNCOES:
            if t not in variaveis:
                # Fica perguntando até o usuário digitar algo válido
                while True:
                    try:
                        entrada = input(f"Valor para variável {t} (ou 'pular' para definir como 0): ")
                        if entrada.lower() == 'pular':
                            print(f"Aviso: Variável '{t}' será definida como 0")
                            variaveis[t] = NumeroComplexo(0, 0)
                            break
                        # Tenta converter o que o usuário digitou
                        variaveis[t] = NumeroComplexo.de_string(entrada)
                        break
                    except ValueError:
                        print("Formato inválido. Use: 3+4j ou 5 ou 2j, ou 'pular'")

    # Finalmente calcula o resultado
    resultado = Avaliador.avaliar(arvore, variaveis)
    print("Resultado:", resultado)

    return arvore


def iniciar_menu():
    """Função principal que roda o menu da calculadora"""
    cmd = None
   
    print("---> CALCULADORA DE NÚMEROS COMPLEXOS <---")

    # Loop principal do programa
    while cmd != 0:
        print("\nOpções:\n1 - Calcular expressão\n2 - Sumário \n0 - Sair")
        try:
            cmd = int(input("Digite a opção: "))
        except ValueError:
            print("Opção inválida. Digite apenas números.")
            continue

        # Opção 1: Calcular expressão
        if cmd == 1:
            arvore = None  # Inicializa como None pra evitar erro
            try:
                expr = input("\nDigite a expressão: ")
                arvore = processar_expressao(expr)
            except (ValueError, ZeroDivisionError) as e:
                print(f"Erro: {e}")
            except KeyboardInterrupt:
                print("\nPrograma interrompido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            
            # Só oferece comparação se a primeira expressão deu certo
            if arvore is not None:
                cmd_comparar = input("\nDeseja comparar com outra expressão? (s/n): ")

                if cmd_comparar.lower() == 's':
                    expr2 = input("\nDigite a segunda expressão: ")
                    try:
                        arvore2 = processar_expressao(expr2)
                        # Compara as duas árvores pra ver se são iguais
                        print("\nAs expressões são equivalentes?")
                        print("Sim" if Comparador.equal(arvore, arvore2) else "Não")
                    except Exception as e:
                        print(f"Erro na segunda expressão: {e}")
                elif cmd_comparar.lower() == 'n':
                    print("Retornando para o menu inicial...")
                else:
                    print("Opção inválida. Retornando para o menu inicial.")

        # Opção 0: Sair
        elif cmd == 0:
            print("Programa Encerrado!")
        
        # Opção 2: Mostrar ajuda
        elif cmd == 2:
            print("\n--> Sumário <--")
            print("\n1 - Cálculos possíveis:\nsoma (+)\nsubtração (-)\nMultiplicação (*)\nDivisão (/)\nPotenciação (**) ")
            print("2 - Utilize espaços entre números e operadores")
            print("3 - Para calcular conjugado utilize: conj(valor)")
            print("4 - Para calcular raiz quadrada utilize: raiz(valor)")
            
        # Qualquer outra opção
        else:
            print("Opção inválida. Selecione uma das opções acima.")
            

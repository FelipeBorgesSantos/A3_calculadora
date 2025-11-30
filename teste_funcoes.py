from tokenizer import Analisador
from parser import AnalisadorSintatico
from tree import ArvoreExpressao
from evaluator import Avaliador

# Teste conj e raiz
print("=== TESTE CONJ ===")
expr = "conj(3+4j)"
tokens = Analisador(expr).tokenizar()
print("Tokens:", tokens)
posfixa = AnalisadorSintatico(tokens).para_posfixa()
print("Pós-fixa:", posfixa)
arvore = ArvoreExpressao.criar_de_posfixa(posfixa)
resultado = Avaliador.avaliar(arvore, {})
print("Resultado:", resultado)

print("\n=== TESTE RAIZ ===")
expr = "raiz(4)"
tokens = Analisador(expr).tokenizar()
print("Tokens:", tokens)
posfixa = AnalisadorSintatico(tokens).para_posfixa()
print("Pós-fixa:", posfixa)
arvore = ArvoreExpressao.criar_de_posfixa(posfixa)
resultado = Avaliador.avaliar(arvore, {})
print("Resultado:", resultado)
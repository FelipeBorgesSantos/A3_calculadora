import math

class NumeroComplexo:
    """Classe que implementa números complexos e suas operações"""
    
    def __init__(self, real, imag):
        """Cria um número complexo com parte real e imaginária"""
        self.real = real  # Parte real (a em a+bi)
        self.imag = imag  # Parte imaginária (b em a+bi)
    
    def somar(self, outro):
        """Soma dois números complexos: (a+bi) + (c+di) = (a+c) + (b+d)i"""
        return NumeroComplexo(self.real + outro.real, self.imag + outro.imag)
    
    def subtrair(self, outro):
        """Subtrai dois números complexos: (a+bi) - (c+di) = (a-c) + (b-d)i"""
        return NumeroComplexo(self.real - outro.real, self.imag - outro.imag)
    
    def multiplicar(self, outro):
        """Multiplica dois números complexos usando a fórmula distributiva"""
        # (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        real_resultado = self.real * outro.real - self.imag * outro.imag
        imag_resultado = self.real * outro.imag + self.imag * outro.real
        return NumeroComplexo(real_resultado, imag_resultado)
    
    def dividir(self, outro):
        """Divide dois números complexos usando o conjugado do denominador"""
        if outro.real == 0 and outro.imag == 0:
            raise ValueError("Não pode dividir por zero")
        
        # Truque: multiplica numerador e denominador pelo conjugado
        conjugado_outro = NumeroComplexo(outro.real, -outro.imag)
        numerador = self.multiplicar(conjugado_outro)
        denominador = outro.real * outro.real + outro.imag * outro.imag
        
        return NumeroComplexo(numerador.real / denominador, numerador.imag / denominador)
    
    def potencia(self, exp):
        if exp == 0:
            return NumeroComplexo(1, 0)
        elif exp == 1:
            return NumeroComplexo(self.real, self.imag)
        elif exp == 2:
            return self.multiplicar(self)
        elif exp == int(exp):  # Expoente inteiro
            exp = int(exp)
            resultado = NumeroComplexo(1, 0)
            for i in range(abs(exp)):
                resultado = resultado.multiplicar(self)
            
            if exp < 0:
                if self.real == 0 and self.imag == 0:
                    raise ValueError("Não pode elevar zero a potência negativa")
                um = NumeroComplexo(1, 0)
                resultado = um.dividir(resultado)
            
            return resultado
        else:
            # Expoente real - usa forma polar (necessário para funcionalidade completa)
            r = math.sqrt(self.real * self.real + self.imag * self.imag)
            theta = math.atan2(self.imag, self.real)
            
            novo_r = r ** exp
            novo_theta = theta * exp
            
            return NumeroComplexo(novo_r * math.cos(novo_theta), novo_r * math.sin(novo_theta))
    
    def conjugado(self):
        """Retorna o conjugado: (a+bi) -> (a-bi)"""
        return NumeroComplexo(self.real, -self.imag)
    
    def raiz_quadrada(self):
        """Calcula a raiz quadrada de um número complexo"""
        # Usa a fórmula da raiz quadrada complexa
        r = math.sqrt(self.real * self.real + self.imag * self.imag)
        
        if self.imag >= 0:
            real_resultado = math.sqrt((r + self.real) / 2)
            imag_resultado = math.sqrt((r - self.real) / 2)
        else:
            real_resultado = math.sqrt((r + self.real) / 2)
            imag_resultado = -math.sqrt((r - self.real) / 2)
        
        return NumeroComplexo(real_resultado, imag_resultado)
    
    def __str__(self):
        """Converte o número complexo para string no formato (a+bj)"""
        if self.imag >= 0:
            return f"({self.real}+{self.imag}j)"
        else:
            return f"({self.real}{self.imag}j)"  # O sinal já é negativo
    
    @staticmethod
    def de_string(texto):
        """Converte uma string como '3+4j' para NumeroComplexo"""
        texto = texto.replace(" ", "").replace("(", "").replace(")", "")
        
        if "j" not in texto:
            return NumeroComplexo(float(texto), 0)
        
        if texto == "j":
            return NumeroComplexo(0, 1)
        elif texto == "-j":
            return NumeroComplexo(0, -1)
        
        if "+" in texto and texto.index("+") > 0:
            partes = texto.split("+")
            real = float(partes[0])
            imag_str = partes[1].replace("j", "")
            imag = float(imag_str) if imag_str else 1
        elif "-" in texto[1:]:
            pos_menos = texto.index("-", 1)
            real = float(texto[:pos_menos])
            imag_str = texto[pos_menos+1:].replace("j", "")
            imag = -float(imag_str) if imag_str else -1
        else:
            imag_str = texto.replace("j", "")
            if imag_str == "" or imag_str == "+":
                imag = 1
            elif imag_str == "-":
                imag = -1
            else:
                imag = float(imag_str)
            real = 0
        
        return NumeroComplexo(real, imag)
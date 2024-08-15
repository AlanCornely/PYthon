from abc import ABC, abstractmethod

# Classe abstrata Operacao
class Operacao(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

# Classes concretas que herdam de Operacao
class Soma(Operacao):
    def calcular(self, a, b):
        return a + b

class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b

class Multiplicacao(Operacao):
    def calcular(self, a, b):
        return a * b

class Divisao(Operacao):
    def calcular(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida."

# Classe Calculadora com métodos públicos e protegidos
class Calculadora:
    def __init__(self):
        self._resultado = 0
        self._operacao = None

    def definir_operacao(self, operacao):
        self._operacao = operacao

    def calcular(self, a, b):
        if self._operacao:
            self._resultado = self._operacao.calcular(a, b)
            return self._resultado
        else:
            return "Nenhuma operação definida."

    def get_resultado(self):
        return self._resultado

    def reset(self):
        self._resultado = 0

# Função principal para rodar o programa
def main():
    calc = Calculadora()

    while True:
        print("\nMenu de Operações:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        escolha = input("Escolha a operação (1/2/3/4) ou 5 para sair: ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            calc.definir_operacao(Soma())
        elif escolha == '2':
            calc.definir_operacao(Subtracao())
        elif escolha == '3':
            calc.definir_operacao(Multiplicacao())
        elif escolha == '4':
            calc.definir_operacao(Divisao())
        else:
            print("Escolha inválida.")
            continue
        
        resultado = calc.calcular(num1, num2)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

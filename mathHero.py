class MageOfAddition:
    def add(self, a, b):
        return a + b

class WarriorOfSubtraction:
    def subtract(self, a, b):
        return a - b

class RangerOfMultiplication:
    def multiply(self, a, b):
        return a * b

class ClericOfDivision:
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não permitida!"

# Criação dos objetos (heróis)
mage = MageOfAddition()
warrior = WarriorOfSubtraction()
ranger = RangerOfMultiplication()
cleric = ClericOfDivision()


def formula1() :
    # numeros para o cálculo
    x1 = 10
    x2 = 5
    x3 = 4
    x4 = 2
    x5 = 3

    # (x1 + x2) * x3 * x4 - x5
    step1 = mage.add(x1, x2)  # (x1 + x2)
    step2 = ranger.multiply(step1, x3)  # (x1 + x2) * x3
    step3 = ranger.multiply(step2, x4)  # (x1 + x2) * x3 * x4
    resultado = warrior.subtract(step3, x5)  # (x1 + x2) * x3 * x4 - x5

    print("Resultado da Fórmula 1:", resultado)


def menu() :
    while True :
        
        print("-------escolha uma missão-------")
        print("1. Missão 1")
        print("2. Missão 2")
        print("3. Missão 3")
        print("4. Missão 4")
        print("--------------------------------")
        escolha = input(("escolha uma missão: "))

        if escolha == 1 :
            print("--------------------------------")
            print("Missão: você deve derrotar o troll executando o seguinte comando\n ((x1+x2)*x3)/x4)-x5\n")
            print("-------escolha a classe que deve começar-------")
            print("1) Mago da adição. ")
            print("2) Arqueiro da multiplicação. ")
            print("1) Guerreiro da subtração. ")
            print("1) Clérigo da divisão. ")
            escolha2 = input(("escolha a classe que iniviará o comando: "))

            if escolha2 == 1 :


# Resolver o enigma mágico
# Substituam as variáveis x1, x2, x3, x4, x5 pelos valores apropriados para cada fórmula

if __name__ == "__mathHero__" :
    menu()
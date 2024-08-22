class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print(f"Item '{item}' adicionado à pilha.")
        else:
            print("Erro: A pilha está cheia. Não é possível adicionar mais elementos.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item '{item}' removido da pilha.")
            return item
        else:
            print("Erro: A pilha está vazia. Não há elementos para remover.")
            return None

    def peek(self):
        if not self.is_empty():
            item = self.stack[-1]
            print(f"Item no topo da pilha: '{item}'")
            return item
        else:
            print("Erro: A pilha está vazia. Não há elementos no topo.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

# Programa principal
def main():
    max_size = int(input("Digite o tamanho máximo da pilha: "))
    stack = Stack(max_size)

    while True:
        print("\nEscolha uma operação:")
        print("1. Push (adicionar elemento)")
        print("2. Pop (remover elemento)")
        print("3. Peek (ver elemento no topo)")
        print("4. Sair")
        escolha = input("Opção: ")

        if escolha == "1":
            item = input("Digite o elemento a ser adicionado: ")
            stack.push(item)
        elif escolha == "2":
            stack.pop()
        elif escolha == "3":
            stack.peek()
        elif escolha == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print(f"Estado atual da pilha: {stack}")

if __name__ == "__main__":
    main()
#GRUPO : KAUAN DOS ANJOS VIEIRA, LUCAS VINICIUS, BRUNO VITOR


class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie
        self._vacinado = False  # Isso vai ser o controle de vacinação

    def calcular_preco_servico(self):
        pass

    def mostrar_informacoes(self):
        vacinado_status = "Vacinado" if self._vacinado else "Não vacinado"
        return f"Nome: {self._nome}, Idade: {self._idade}, Espécie: {self._especie}, Status de Vacinação: {vacinado_status}" #Adicionando apenas o status de vacinação

    def vacinar(self):
        self._vacinado = True


class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50


class Gato(Animal):
    def calcular_preco_servico(self):
        return 40


class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30


class Coelho(Animal):  # Decidi colocar mais um animal no menu para aumentar a lista
    def calcular_preco_servico(self):
        return 25


def menu():
    animais = []

    while True:
        print("\n1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Vacinar seu pet")
        print("5. Sair")

        opcao = input("Escolha a opção: ")

        if opcao == '1':
            nome = input("Qual o nome do animal? ")
            idade = int(input("Qual a idade do animal? "))
            especie = input("Qual a espécie de animal (Cachorro, Gato, Passaro, Coelho)? ")

            if especie.lower() == 'cachorro':
                animal = Cachorro(nome, idade, especie)
            elif especie.lower() == 'gato':
                animal = Gato(nome, idade, especie)
            elif especie.lower() == 'passaro':
                animal = Passaro(nome, idade, especie)
            elif especie.lower() == 'coelho':
                animal = Coelho(nome, idade, especie)
            else:
                print("Espécie de animal não reconhecido.")
                continue

            animais.append(animal)
            print(f"O {especie.lower()} {nome} foi cadastrado com sucesso!")

        elif opcao == '2':
            if not animais:
                print("Nenhum animal foi cadastrado ainda.")
            else:
                for idx, animal in enumerate(animais):
                    print(f"{idx + 1}. {animal.mostrar_informacoes()}")

        elif opcao == '3':
            if not animais:
                print("Nenhum animal foi cadastrado ainda.")
            else:
                idx = int(input("Escolha o número do animal (Consulte o animal para saber o número dele): ")) - 1
                if 0 <= idx < len(animais):
                    animal = animais[idx]
                    preco = animal.calcular_preco_servico()
                    print(f"O preço do serviço para {animal._nome} é R$ {preco}.")
                else:
                    print("Número de animal inválido.")

        elif opcao == '4':
            if not animais:
                print("Nenhum animal foi cadastrado ainda.")
            else:
                idx = int(input("Escolha o número do animal para vacinar (Consulte o animal para saber o número dele): ")) - 1
                if 0 <= idx < len(animais):
                    animal = animais[idx]
                    animal.vacinar() 
                    print(f"{animal._nome} foi vacinado com sucesso!")
                else:
                    print("Número de animal inválido.")

        elif opcao == '5':
            break
        else:
            print("Insira um número válido!")


if __name__ == "__main__":
    menu()

class Crianca:
    def __init__(self):
        self.criancas = []

    def adicionar_crianca(self, nome, id_crianca):
        crianca = {"nome": nome, "id": id_crianca}
        self.criancas.append(crianca)
        print("Criança adicionada com sucesso.")

    def visualizar_criancas(self):
        print("Lista de Crianças:")
        if self.criancas:
            for crianca in self.criancas:
                print(" ")
                print(f"Nome: {crianca['nome']}, / ID: {crianca['id']}")
        else:
            print("Não há crianças cadastradas.")
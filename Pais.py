class Pais:
    def __init__(self):
        self.pais = []

    def adicionar_pai(self, nome, id):
        pai = {'nome': nome, 'id': id}
        self.pais.append(pai)
        print("Pai adicionado com sucesso.")

    def visualizar_pais(self):
        if self.pais:
            print("Lista de Pais:")
            for pai in self.pais:
                print(f"Nome: {pai['nome']}, / ID: {pai['id']}")
        else:
            print("Não há pais cadastrados.")


class Crianca:
    def __init__(self):
        self.criancas = []
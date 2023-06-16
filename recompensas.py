class Recompensa:
    def __init__(self, id_recompensa, nome_recompensa):
        self.id = id_recompensa
        self.nome = nome_recompensa


class GerenciadorRecompensas:
    def __init__(self):
        self.recompensas = []

    def adicionar_recompensa(self, id_recompensa, nome_recompensa):
        recompensa = Recompensa(id_recompensa, nome_recompensa)
        self.recompensas.append(recompensa)
        print("Recompensa adicionada com sucesso.")

    def remover_recompensa(self, id_recompensa):
        recompensa = self.buscar_recompensa_por_id(id_recompensa)
        if recompensa:
            self.recompensas.remove(recompensa)
            print("Recompensa removida com sucesso.")
        else:
            print("Recompensa não encontrada, tente novamente.")

    def visualizar_recompensas(self):
        if self.recompensas:
            print("Recompensas disponíveis:")
            print("")
            for recompensa in self.recompensas:
                print(f"ID: {recompensa.id}, / Nome: {recompensa.nome}")
                print("")
        else:
            print("Não há recompensas disponíveis no momento.")

    def buscar_recompensa_por_id(self, id_recompensa):
        for recompensa in self.recompensas:
            if recompensa.id == id_recompensa:
                return recompensa
        return None

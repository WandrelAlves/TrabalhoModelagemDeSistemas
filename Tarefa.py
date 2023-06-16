from recompensas import GerenciadorRecompensas
from crianca import Crianca
from Pais import Pais


class Tarefa:
    def __init__(self, id_tarefa, nome_tarefa, id_recompensa,id_crianca,id_pais):
        self.id = id_tarefa
        self.nome = nome_tarefa
        self.id_Reward = id_recompensa
        self.id_Crianca = id_crianca
        self.id_Pais = id_pais
        self.concluida = False

    def concluir(self):
        self.concluida = True


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.gerenciador_recompensas = GerenciadorRecompensas()

    def criar_tarefa(self, id_tarefa, nome_tarefa,id_recompensa,id_crianca,id_pais):
        tarefa = Tarefa(id_tarefa, nome_tarefa,id_recompensa,id_crianca,id_pais)
        self.tarefas.append(tarefa)
        print("Tarefa criada com sucesso.")

    def concluir_tarefa(self, id_tarefa):
        tarefa = self.buscar_tarefa_por_id(id_tarefa)
        if tarefa:
            tarefa.concluir()
            print("Tarefa concluída com sucesso.")
        else:
            print("Tarefa não encontrada.")

    def visualizar_tarefas(self):
        print(" ")
        print("Todas as tarefas:")
        print("")
        if self.tarefas:
            for tarefa in self.tarefas:
                status = "Concluída" if tarefa.concluida else "Pendente"
                print(f"ID: {tarefa.id}, / Nome: {tarefa.nome}, / ID Reward: {tarefa.id_Reward}, / ID Criança: {tarefa.id_Crianca}, / ID pais: {tarefa.id_Pais}, / Status: {status}")

        else:
            print("Não há tarefas registradas.")

    def buscar_tarefa_por_id(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None

from Pais import Pais
from crianca import Crianca
from recompensas import GerenciadorRecompensas
from Tarefa import GerenciadorTarefas

gerenciador_tarefas = GerenciadorTarefas()
gerenciador_recompensas = GerenciadorRecompensas()
gerenciador_criancas = Crianca()
gerenciador_pais = Pais()

while True:
    # Menu principal do programa
    print("----- Sistema de Gestão de Recompensa -----")
    print("1. Adicionar criança")
    print("2. Adicionar pais")
    print("3. Adicionar recompensa")
    print("4. Criar tarefa")
    print("5. Concluir tarefas")
    print("6. Visualizar todas as tarefas")
    print("7. Visualizar recompensas")
    print("8. Visualizar crianca(s)")
    print("9. Visualizar pais")
    print("10. Sair")

    print(" ")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
       # Opção para adicionar uma nova criança
        print("")
        nome = input("Digite o nome da criança: ")
        id = input("Digite o ID da criança: ")
        gerenciador_criancas.adicionar_crianca(nome, id)
        print("")

    elif escolha == "2":
        # Opção para adicionar um novo pai
        print("")
        nome = input("Digite o nome do pai: ")
        id_pai = input("Digite o ID do pai: ")
        gerenciador_pais.adicionar_pai(nome, id_pai)
        print("")


    elif escolha == "3":
        # Opção para adicionar uma nova recompensa
        print("")
        id = input("Digite o ID da recompensa: ")
        nome = input("Digite o nome da recompensa: ")
        gerenciador_recompensas.adicionar_recompensa(id, nome)
        print("")

    elif escolha == "4":
        # Opção para adicionar uma nova tarefa
        print("")
        id = input("Digite o ID da tarefa: ")
        nome = input("Digite o nome da tarefa: ")
        id_Reward = input("Digite o ID da Reward: ")
        id_crianca = input("Digite o ID da criança que irá fazer essa tarefa: ")
        id_pais = input("Digite o ID do pais responsavél: ")
        gerenciador_tarefas.criar_tarefa(id, nome, id_Reward,id_crianca,id_pais)
        print("")

    elif escolha == "5":
         # Opção para concluir uma tarefa
        id = input("Digite o ID da tarefa a ser concluída: ")
        gerenciador_tarefas.concluir_tarefa(id)

        print("")
        print("APERTE ENTER PARA CONTINUAR!")
        input("")

        print("Continuando o programa...")

    elif escolha == "6":
        # Opção para visualizar todas as tarefas registradas no sistema
        gerenciador_tarefas.visualizar_tarefas()
        print("")
        print("APERTE ENTER PARA CONTINUAR!")
        input("")

        print("Continuando o programa...")

    elif escolha == "7":
        # Opção para visualizar o total de recompensas no sistema
        gerenciador_recompensas.visualizar_recompensas()
        print("")
        print("APERTE ENTER PARA CONTINUAR!")
        input("")

        print("Continuando o programa...")


    elif escolha == "8":
         # Opção para visualizar todas as crianças cadastradas
        gerenciador_criancas.visualizar_criancas()
        print("")
        print("APERTE ENTER PARA CONTINUAR!")
        input("")

        print("Continuando o programa...")

    elif escolha == "9":
       # Opção para visualizar todos os pais cadastrados
        gerenciador_pais.visualizar_pais()
        print("")
        print("APERTE ENTER PARA CONTINUAR!")
        input("")

        print("Continuando o programa...")

    
    elif escolha == "10":
        # Opção para sair do programa
        print("Saindo do programa...")
        break


    else:
        # Caso seja digitada uma opção inválida, exibe uma mensagem de erro
        print("Opção inválida. Digite novamente.")
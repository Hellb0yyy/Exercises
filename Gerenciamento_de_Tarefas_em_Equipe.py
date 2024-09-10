
lista_tarefas = {}

def adicionar_tarefa(tarefas, descricao, status, prioridade):
    novo_id = max(tarefas.keys(), default=0) + 1  
    tarefas[novo_id] = {
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade
    }
    print(f"Tarefa '{descricao}' adicionada com sucesso!\n")

def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for id_tarefa, detalhes in tarefas.items():
            print(f"ID: {id_tarefa}, Descrição: {detalhes['descricao']}, Status: {detalhes['status']}, Prioridade: {detalhes['prioridade']}")
        print()

def filtrar_tarefas(tarefas, status=None, prioridade=None):
    tarefas_filtradas = {}
    for id_tarefa, detalhes in tarefas.items():
        if (status and detalhes['status'] != status) or (prioridade and detalhes['prioridade'] != prioridade):
            continue
        tarefas_filtradas[id_tarefa] = detalhes
    return tarefas_filtradas

def menu():
    while True:
        print("Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Todas as Tarefas")
        print("3. Filtrar Tarefas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            status = input("Status da tarefa (pendente, em andamento, concluída): ")
            prioridade = input("Prioridade da tarefa (alta, média, baixa): ")
            adicionar_tarefa(lista_tarefas, descricao, status, prioridade)

        elif opcao == "2":
            print("Tarefas cadastradas:")
            visualizar_tarefas(lista_tarefas)

        elif opcao == "3":
            status = input("Digite o status para filtrar (pendente, em andamento, concluída) ou deixe em branco para não filtrar: ")
            prioridade = input("Digite a prioridade para filtrar (alta, média, baixa) ou deixe em branco para não filtrar: ")
            tarefas_filtradas = filtrar_tarefas(lista_tarefas, status if status else None, prioridade if prioridade else None)
            visualizar_tarefas(tarefas_filtradas)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.\n")

menu()

agenda=[]
def adicinar_contato(agenda):
    contato_nome = input("Digite o nome: ")
    contato_numero = int(input('Digite seu telefone: '))
    contato = {'nome': contato_nome, 'telefone': contato_numero}
    agenda.append(contato)
    return agenda

def listar_contato(agenda):
    if len(agenda) > 0:
        print ('-----------------------------------------------')
        for i, contato in enumerate(agenda):
            print(f'{i+1}. Nome: {contato["nome"]} | Telefone: {contato["telefone"]}')
    else :
        print('Agenda está vasia')

def buscar_contato(agenda, buscar):
    if len(agenda) > 0:
        for contato in agenda:
            if buscar.lower() == contato['nome'].lower():
              print(f' Nome: {contato["nome"]} | Telefone: {contato["telefone"]}')
              return buscar
        print('Contato não encontrado.')
    else :
        print('Agenda está vazia')
    
def deletar_contato(agenda, deletar):
    for i, contato in enumerate(agenda):
         if deletar.lower() == contato['nome'].lower():
            agenda.pop(i)
            print('Contato deletado com sucesso!')
            return
    print('Contato não encontrado.')

def menu_interativo():  
    print ('-----------------------------------------------')
    print (f'1. Adicionar contato novo')
    print (f'2. Mostrar contatos')
    print (f'3. Buscar contato')
    print (f'4. Deletar contato')
    print (f'5. Sair')
    print ('-----------------------------------------------')
    menu = int(input('Digite sua opção: '))
    return menu

menu = menu_interativo()

while menu != 5 :
    if menu == 1 :
        adicinar_contato(agenda)
        print('Contato adicionado com sucesso!')
    elif menu == 2 :
        listar_contato(agenda)
        print ('-----------------------------------------------')
        print('Esses são todos os contatos adicinados')
    elif menu == 3:
        buscar=input('Digite o nome para efetuar a busca:')
        buscar_contato(agenda, buscar)
    elif menu == 4:
        deletar=input('Digite o nome para deletar:')
        deletar_contato(agenda, deletar)
    else :
        print('Numero invalido, tente novamente')
    menu = menu_interativo()

print('Programa finalizado!')
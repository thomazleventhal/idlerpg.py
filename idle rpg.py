import random
import time
import os

# ADICIONAR CONTEUDO: INIMIGOS DIFERENTES E ESPADAS DIFERENTES E UM FIM?
# cores e sons
# critico talvez?
# dodge chance talvez?

os.system('')

def nome_equip(jogador, equiploja):
    for i in range(len(equiploja)):
        if jogador["equipamento"] == equiploja[i]["id"]:
            return equiploja[i]["nome"]

def exibe_status(jogador, equiploja, levelup=False): # Função basica que mostra os status do jogador caso necessário
    print('-'*50)
    if levelup:
        print('\033[92mSeus status aumentaram!\033[0m')
        for i, j in jogador.items():
            if i != "vida_atual" and i != "exp" and i != "nivel" and i != "nome" and i != "ouro" and i != 'pocao' and i != "equipamento":
                time.sleep(0.2)
                print(f'\033[36m{i}: {j}\033[0m')
    else:
        for i, j in jogador.items():
                time.sleep(0.2)
                if i == "pocao":
                    if j == True: j = "possui"
                    else: j = "não possui"
                elif i == "equipamento":
                    j = nome_equip(jogador, equiploja)
                print(f'{i}: {j}')
    print('-'*50)

def curandeiro(jogador): # O curandeiro, onde se pode pagar ouro para obter cura
    custo_cura = (jogador["vida"] - jogador["vida_atual"]) // 2
    try:
        escolha = int(input('Você passa pelos panos na porta da casa do curandeiro.\nAo te ver, o curandeiro diz:\n\033[36m"Bem-vindo a meu estabelecimento! Necessita de meus serviços?\033[0m\n1- Sim, por favor\n2- Não, obrigado (Retornar a praça principal)\n'))
    except ValueError:
        print('\033[31mDigite apenas números válidos!\033[0m')
        return curandeiro(jogador)
    if escolha == 1:
        if jogador["vida"] == jogador["vida_atual"]:
            print('Sua vida já está cheia')
        elif jogador["vida_atual"] == 0 and jogador["ouro"] < custo_cura:
            print('O curandeiro diz:\n\033[36m"Vejo que está muito ferido e que não possuí muito dinheiro.\nIrei te curar pelo preço que puder pagar, tudo bem?"\033[0m')
            try:
                escolha2 = int(input('Dar \033[31mtodo seu ouro\033[0m em troca da cura?\n1- Sim\n2- Não\n'))
            except ValueError:
                print('\033[31mDigite apenas números válidos!\033[0m')
                return curandeiro(jogador)
            if escolha2 < 1 or escolha2 > 2:
                print('\033[31mEscolha apenas opções válidas!\033[0m')
                return curandeiro(jogador)
            elif escolha2 == 1:
                 print("O curandeiro coloca as mãos sobre seus ferimentos, e após um leve brilho verde, você não sente mais dor alguma.\n\033[32mSua vida se regenerou ao máximo!\033[0m")
                 jogador['ouro'] = 0
                 jogador['vida_atual'] == jogador['vida']
        else:
            try:
                curarounao = int(input(f'O curandeiro diz:\n\033[36m"Para te curar completamente, cobrarei \033[33m{custo_cura} de ouro\033[0m, tudo bem?"\033[0m\n1- Sim, por favor\n2- Não, obrigado (Retornar a praça principal)\n'))
            except ValueError:
                print('\033[31mDigite apenas números válidos!\033[0m')
                return curandeiro(jogador)
            if curarounao == 1:
                if jogador["ouro"] < custo_cura:
                    print('Você não possui ouro suficiente para isso.')
                else:
                    print("O curandeiro coloca as mãos sobre seus ferimentos, e após um leve brilho verde, você não sente mais dor alguma.\n\033[32mSua vida se regenerou ao máximo!\033[0m")
                    jogador["ouro"] -= custo_cura
                    jogador["vida_atual"] == jogador["vida"]
            elif curarounao < 1 or curarounao > 2:
                print('\033[31mEscolha apenas opções válidas!\033[0m')
                return curandeiro(jogador)
    elif escolha < 1 or escolha > 2:
        print('\033[31mEscolha apenas opções válidas!\033[0m')
        return curandeiro(jogador)

def loja(jogador, iloja, equiploja): #loja onde o jogador pode comprar itens

    print(f'Você passa entra pela porta e cumprimenta o lojista\nEle diz:\n\033[36m"Bem-vindo a minha loja, o que deseja comprar?"\033[0m (Você possui {jogador["ouro"]} de ouro)')
    for i in range(len(iloja)):
        print(f'{i+1}- {iloja[i]["nome"]} (\033[33m{iloja[i]["preco"]} de ouro\033[0m)\n    {iloja[i]["desc"]}')
    for i in range(len(equiploja)):
            if equiploja[i]["id"] == jogador["equipamento"]+1:
                print(f'{len(iloja)+1}- {equiploja[i]["nome"]} (\033[33m{equiploja[i]["preco"]} de ouro\033[0m)\n    {equiploja[i]["desc"]}')

    try:
        escolha = int(input(f'{len(iloja) + jogador["equipamento"]+2}- Voltar para a praça principal\n'))
    except ValueError:
        print('\033[31mDigite apenas números válidos!\033[0m')
        return loja(jogador, iloja, equiploja)

    if escolha > len(iloja):
        if jogador['ouro'] < equiploja[jogador["equipamento"]+1]["preco"]:
            print('Você não possui dinheiro suficiente para isso.')
        else:
            print('\033[36m"Ótima escolha, faça bom proveito..."\033[0m')
            jogador['ouro'] -= equiploja[jogador["equipamento"]+1]["preco"]
            jogador['equipamento'] = equiploja[jogador["equipamento"]+1]['id']
            jogador['dano_min'] += equiploja[jogador["equipamento"]]["dano_min"]
            jogador['dano_max'] += equiploja[jogador["equipamento"]]["dano_max"]
            
            jogador['dano_min'] -= equiploja[jogador["equipamento"]-1]["dano_min"]
            jogador['dano_max'] -= equiploja[jogador["equipamento"]-1]["dano_max"]
            
    else:
        if jogador['ouro'] < iloja[escolha-1]["preco"]:
            print('Você não possui dinheiro suficiente para isso.')
        else:
            print('\033[36m"Ótima escolha, faça bom proveito..."\033[0m')
            jogador['ouro'] -= iloja[escolha-1]["preco"]
            if iloja[escolha-1]["nome"] == "Poção":
                if jogador['pocao'] == True:
                    print('Você não pode carregar mais de um desse item!')
                    return loja(jogador, iloja, equiploja)
                jogador['pocao'] = True
            
    if escolha < 1 or escolha > len(iloja)+2:
        print('\033[31mEscolha apenas opções válidas!\033[0m')
        return loja(jogador, iloja, equiploja)
    
def arena(jogador, inimigos): # A arena, onde o usuario pode escolher com qual monstro lutar para conseguir ficar mais forte
    print('\033[94mBem-vindo a arena!\ncom quem deseja lutar?/033[0m')
    
    for i in range(len(inimigos)):
        print(f'{i+1}- {inimigos[i]["nome"]} | Nível: {inimigos[i]["nivel"]}')

    try:  
        escolha = int(input(f'{len(inimigos)+1}- Voltar para a praça principal\n'))
    except ValueError:
        print('\033[31mDigite apenas números válidos!\033[0m')
        return arena(jogador, inimigos)
    
    if escolha < 1 or escolha > len(inimigos)+1:
        print('\033[31mEscolha apenas opções válidas!\033[0m')
        return arena(jogador, inimigos)

    
    elif escolha <= len(inimigos):    
        print('\033[94mSe prepare!\033[0m')
        if luta(jogador, inimigos[escolha-1]):
            print(f'\033[94mParabéns pela vitória! Talvez seja uma boa ideia se curar um pouco.\033[0m')
        else:
            print(f'\033[94mCaramba, Esse inimigo era muito forte! Talvez você devesse treinar mais\nNão esqueça de se curar, pois sua vida está em 0!\033[0m')
        subiu_de_nivel(jogador)
    

def menu(jogador, inimigos, iloja, equiploja): # o menu principal do jogo, onde o jogador pode escolher o que fazer
    print('O que deseja fazer?')
    try:
        escolha = int(input('1- Arena\n2- Loja\n3- Curandeiro\n4- Status\n'))
    except ValueError:
        print('\033[31mDigite apenas números válidos!\033[0m')
        return
    if escolha == 1:
        if jogador["vida_atual"] == 0:
            print("\033[94mVocê está exausto demais para lutar na arena, tente se curar um pouco.\033[0m")
        else: arena(jogador, inimigos)
    elif escolha == 2: loja(jogador, iloja, equiploja)
    elif escolha == 3: curandeiro(jogador)
    elif escolha == 4: exibe_status(jogador, equiploja)
    else: print('\033[31mEscolha apenas opções válidas!\033[0m')
        
    


def subiu_de_nivel(jogador): #função chamada para verificar caso o jogador tenha subido de nível.
                             # caso ele tenha subido de nivel, a função aumenta seus status e printa isso no terminal
    barreira_de_xp = 10 * 2**(jogador["nivel"] - 1)

    #if jogador['exp'] > jogador['exp'] * 2: checa_novamente = True

    if jogador['exp'] >= barreira_de_xp:
        jogador['nivel'] += 1
        print('-'*50)
        print(f'\033[92mSUBIU DE NÍVEL!\033[0m\n{jogador["nivel"]-1} -> {jogador["nivel"]}')
        print('Sua vida se regenerou ao máximo!')
        time.sleep(0.5)
        jogador['vida'] += 10
        jogador['vida_atual'] = jogador['vida']
        if jogador['nivel'] % 2 == 0:
            jogador['dano_min'] += 1
            jogador['dano_max'] += 1
            jogador['defesa'] += 2
        exibe_status(jogador, [], levelup=True)
        input('Pressione [ENTER] para prosseguir')

    #if checa_novamente: return subiu_de_nivel(jogador)
    



def luta(jogador, inimigo): #função utilizada pra começar uma luta quando o jogador está na arena
    inimigo_atual = inimigo.copy()
    print('-'*50)
    print(f'\033[32m{jogador["nome"]}\033[0m está contra {inimigo_atual["nome"]}')
    print('-'*50)

    while jogador["vida_atual"] > 0 and inimigo_atual["vida_atual"] > 0:
        print('-'*50)
        if jogador['vida_atual'] >= jogador['vida'] * 0.10: print(f'{jogador["nome"]}: \033[32m{jogador["vida_atual"]} de vida\033[0m | {inimigo_atual["nome"]}: {inimigo_atual["vida_atual"]} de vida')
        else: print(f'{jogador["nome"]}: \033[31m{jogador["vida_atual"]} de vida\033[0m | {inimigo_atual["nome"]}: {inimigo_atual["vida_atual"]} de vida')
        print('-'*50)
        time.sleep(1)
        
        if jogador['vida_atual'] <= jogador['vida'] * 0.25 and jogador['pocao'] == True:
            jogador['pocao'] = False
            print(f'{jogador["nome"]} bebe sua poção, \033[32mse regenerando por completo\033[0m')
            jogador['vida_atual'] = jogador['vida']

        #dano do jogador
        dano_causado_jogador = random.randint(jogador["dano_min"], jogador["dano_max"]) - inimigo_atual["defesa"]
        if dano_causado_jogador <= 0: dano_causado_jogador = 1
        print(f'{jogador["nome"]} \033[31mataca e atinge o(a)\033[0m {inimigo_atual["nome"]}, causando \033[31m{dano_causado_jogador}\033[0m de dano...')
        inimigo_atual["vida_atual"] -= dano_causado_jogador
        time.sleep(1)

        if inimigo_atual["vida_atual"] <= 0: #checagem de morte
            print(f'\033[92mVocê venceu!\033[0m\nGanhando \033[96m{inimigo_atual["exp_dado"]} de experiência\033[0m e \033[33m{inimigo_atual["ouro_dado"]} de ouro.\033[0m')
            jogador["exp"] += inimigo_atual["exp_dado"]
            jogador["ouro"] += inimigo_atual["ouro_dado"]
            return True

        #dano do inimigo
        dano_causado_inimigo = random.randint(inimigo_atual["dano_min"], inimigo_atual["dano_max"]) - jogador["defesa"]
        if dano_causado_inimigo <= 0: dano_causado_inimigo = 1
        print(f'{inimigo_atual["nome"]} \033[31mataca e atinge o(a)\033[0m {jogador["nome"]}, causando \033[31m{dano_causado_inimigo}\033[0m de dano...')
        jogador["vida_atual"] -= dano_causado_inimigo
        if jogador["vida_atual"] < 0: jogador["vida_atual"] = 0
        time.sleep(1)

    else:
        if inimigo["vida_atual"] <= 0 and jogador["vida_atual"] > 0:
            print(f'\033[92mVocê venceu!\033[0m\nGanhando \033[96m{inimigo_atual["exp_dado"]} de experiência\033[0m e \033[33m{inimigo_atual["ouro_dado"]} de ouro.\033[0m')
            jogador["exp"] += inimigo_atual["exp_dado"]
            jogador["ouro"] += inimigo_atual["ouro_dado"]
            time.sleep(1)
            return True
        
        print('Você perdeu!')
        time.sleep(1)
        return False


def main():
    jogador_base = { #Referência dos status base do jogador (nivel 1)
        "nome": input('Olá, como você se chama? '),
        "vida": 100,
        "vida_atual": 100,
        "dano_min": 10,
        "dano_max": 15,
        "defesa": 5,
        "exp": 0,
        "nivel": 1,
        "ouro": 0,
        "equipamento": 0,
        "pocao": False
        }
    jogador = jogador_base.copy()

    
    inimigos = [ #Lista de inimigos do jogo para fácil acesso
    {"nome": "Rato",
    "vida": 80,
    "vida_atual": 80,
    "dano_min": 5,
    "dano_max": 10,
    "defesa": 5,
    "exp_dado": 5,
    "ouro_dado": 10,
    "nivel": 1},
    
    {"nome": "Goblin",
    "vida": 160,
    "vida_atual": 160,
    "dano_min": 10,
    "dano_max": 18,
    "defesa": 6,
    "exp_dado": 9,
    "ouro_dado": 20,
    "nivel": 5},
    
    {"nome": "Orc",
    "vida": 220,
    "vida_atual": 220,
    "dano_min": 17,
    "dano_max": 25,
    "defesa": 7,
    "exp_dado": 15,
    "ouro_dado": 30,
    "nivel": 10},
    
    {"nome": "Gigante",
    "vida": 300,
    "vida_atual": 300,
    "dano_min": 23,
    "dano_max": 30,
    "defesa": 10,
    "exp_dado": 25,
    "ouro_dado": 45,
    "nivel": 15},
    
    {"nome": "Dragão",
    "vida": 500,
    "vida_atual": 500,
    "dano_min": 30,
    "dano_max": 45,
    "defesa": 15,
    "exp_dado": 50,
    "ouro_dado": 70,
    "nivel": '∞'},
    ]

    iloja = [ #Lista de itens na loja que não são equipamentos
    {"nome": "Poção de cura",
     "preco": 80,
     "desc": "Você usará a poção automaticamente quando estiver com menos de 25% de vida"
     },
    ]

    equiploja = [ #lista de equipamentos na loja (armas)
    {"nome": "N/A",
     "preco": 0,
     "desc": "Bom, não da pra ficar pior que isso né?",
     "dano_min": 0,
     "dano_max": 0,
     "id": 0
     },

    {"nome": "Espada de madeira",
     "preco": 100,
     "desc": "Uma espada simples, mas suficiente para algumas coisas.",
     "dano_min": 3,
     "dano_max": 3,
     "id": 1
    },
    {"nome": "Espada de bronze",
     "preco": 200,
     "desc": "Não é ótima, mas com certeza melhor que a de madeira.",
     "dano_min": 5,
     "dano_max": 5,
     "id": 2
     },
    {"nome": "Espada de prata",
     "preco": 500,
     "desc": "A melhor espada de prata que se pode encontrar na cidade! (provavelmente a única também)",
     "dano_min": 7,
     "dano_max": 7,
     "id": 3
     },
    {"nome": "Espada de ouro",
     "preco": 1000,
     "desc": "Uma espada cara, mas sua usabilidade faz valer a pena.",
     "dano_min": 10,
     "dano_max": 10,
     "id": 4
     },
    {"nome": "Espada de diamante",
     "preco": 1500,
     "desc": "Essa com certeza da conta de tudo. A melhor que se pode encontrar por aqui.",
     "dano_min": 14,
     "dano_max": 14,
     "id": 5
     },
    ]

   
    while True:
        menu(jogador, inimigos, iloja, equiploja)


if __name__ == "__main__":
    main()

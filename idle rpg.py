import random
import time

# fazer loja() (pensei em um item só, que seria uma poção. ela seria usada automaticamente quando o jogador caisse abaixo de x% de vida)
    # talvez de pra colocar equipamentos fazendo um sistema mais simples (quando vc compra um, vc substitui o anterior e aparece um mais novo na loja)
# critico talvez?
# dodge chance talvez?

def nome_equip(jogador, equiploja):
    for i in range(len(equiploja)):
        if jogador["equipamento"] == equiploja[i]["id"]:
            return equiploja[i]["nome"]

def exibe_status(jogador, equiploja, levelup=False): # Função basica que mostra os status do jogador caso necessário
    print('-'*50)
    if levelup:
        print('Seus status aumentaram!')
        for i, j in jogador.items():
            if i != "vida_atual" and i != "exp" and i != "nivel" and i != "nome" and i != "ouro" and i != 'pocao' and i != "equipamento":
                time.sleep(0.2)
                print(f'{i}: {j}')
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
        escolha = int(input('Você passa pelos panos na porta da casa do curandeiro.\nAo te ver, o curandeiro diz:\n"Bem-vindo a meu estabelecimento! Necessita de meus serviços?\n1- Sim, por favor\n2- Não, obrigado (Retornar a praça principal)\n'))
    except ValueError:
        print('Digite apenas números válidos!')
        return curandeiro(jogador)
    if escolha == 1:
        if jogador["vida"] == jogador["vida_atual"]:
            print('Sua vida já está cheia')
        elif jogador["vida_atual"] == 0 and jogador["ouro"] < custo_cura:
            print('O curandeiro diz:\n"Vejo que está muito ferido e que não possuí muito dinheiro.\nIrei te curar pelo preço que puder pagar, tudo bem?"')
            try:
                escolha2 = int(input('Dar todo seu ouro em troca da cura?\n1- Sim\n2- Não\n'))
            except ValueError:
                print('Digite apenas números válidos!')
                return curandeiro(jogador)
            if escolha2 < 1 or escolha2 > 2:
                print('Escolha apenas opções válidas!')
                return curandeiro(jogador)
            elif escolha2 == 1:
                 print("O curandeiro coloca as mãos sobre seus ferimentos, e após um leve brilho verde, você não sente mais dor alguma.\nSua vida se regenerou ao máximo!")
                 jogador['ouro'] = 0
                 jogador['vida_atual'] == jogador['vida']
        else:
            try:
                curarounao = int(input(f'O curandeiro diz:\n"Para te curar completamente, cobrarei {custo_cura} de ouros, tudo bem?"\n1- Sim, por favor\n2- Não, obrigado (Retornar a praça principal)\n'))
            except ValueError:
                print('Digite apenas números válidos!')
                return curandeiro(jogador)
            if curarounao == 1:
                if jogador["ouro"] < custo_cura:
                    print('Você não possui ouro suficiente para isso.')
                else:
                    print("O curandeiro coloca as mãos sobre seus ferimentos, e após um leve brilho verde, você não sente mais dor alguma.\nSua vida se regenerou ao máximo!")
                    jogador["ouro"] -= custo_cura
                    jogador["vida_atual"] == jogador["vida"]
            elif curarounao < 1 or curarounao > 2:
                print('Escolha apenas opções válidas!')
                return curandeiro(jogador)
    elif escolha < 1 or escolha > 2:
        print('Escolha apenas opções válidas!')
        return curandeiro(jogador)

def loja(jogador, iloja, equiploja): #loja onde o jogador pode comprar itens

    print(f'Você passa entra pela porta e cumprimenta o lojista\nEle diz:\n"Bem-vindo a minha loja, o que deseja comprar?" (Você possui {jogador["ouro"]} de ouro)')
    for i in range(len(iloja)):
        print(f'{i+1}- {iloja[i]["nome"]} ({iloja[i]["preco"]} de ouro)\n    {iloja[i]["desc"]}')
    for i in range(len(equiploja)):
            if equiploja[i]["id"] == jogador["equipamento"]+1:
                print(f'{len(iloja)+1}- {equiploja[i]["nome"]} ({equiploja[i]["preco"]} de ouro)\n    {equiploja[i]["desc"]}')
    try:
        escolha = int(input(f'{len(iloja) + jogador["equipamento"]+2}- Voltar para a praça principal\n'))
    except ValueError:
        print('Digite apenas números válidos!')
        return loja(jogador, iloja, equiploja)
    if escolha > len(iloja):
        if jogador['ouro'] < equiploja[jogador["equipamento"]+1]["preco"]:
            print('Você não possui dinheiro suficiente para isso.')
        else:
            print('"Ótima escolha, faça bom proveito..."') #VOCE PAROU AQUI !!! FAÇA A MECANICA DE COMPRA DE FATO E A MUDANÇA DE STATS (parte mais dificil)
            jogador['ouro'] -= equiploja[jogador["equipamento"]+1]["preco"]
            jogador['equipamento'] = equiploja[jogador["equipamento"]+1]['id']
            jogador['dano_min'] += equiploja[jogador["equipamento"]]["dano_min"]
            jogador['dano_max'] += equiploja[jogador["equipamento"]]["dano_max"]
            
            
    else:
        if jogador['ouro'] < iloja[escolha-1]["preco"]:
            print('Você não possui dinheiro suficiente para isso.')
        else:
            print('"Ótima escolha, faça bom proveito..."')
            jogador['ouro'] -= iloja[escolha-1]["preco"]
            if iloja[escolha-1]["nome"] == "Poção":
                jogador['pocao'] = True
            
    if escolha < 1 or escolha > len(iloja)+2:
        print('Escolha apenas opções válidas!')
        return loja(jogador, iloja, equiploja)
    
def arena(jogador, inimigos): # A arena, onde o usuario pode escolher com qual monstro lutar para conseguir ficar mais forte
    print('Bem-vindo a arena!\ncom quem deseja lutar?')
    
    for i in range(len(inimigos)):
        print(f'{i+1}- {inimigos[i]["nome"]} | Nível: {inimigos[i]["nivel"]}')

    try:  
        escolha = int(input(f'{len(inimigos)+1}- Voltar para a praça principal\n'))
    except ValueError:
        print('Digite apenas números válidos!')
        return arena(jogador, inimigos)
    
    if escolha < 1 or escolha > len(inimigos)+1:
        print('Escolha apenas opções válidas!')
        return arena(jogador, inimigos)

    
    elif escolha <= len(inimigos):    
        print('Se prepare!')
        if luta(jogador, inimigos[escolha-1]):
            print('Parabéns pela vitória! Talvez seja uma boa ideia se curar um pouco.')
        else:
            print(f'Caramba, Esse inimigo era muito forte! Talvez você devesse treinar mais\nNão esqueça de se curar, pois sua vida está em 0!')
        subiu_de_nivel(jogador)
    

def menu(jogador, inimigos, iloja, equiploja): # o menu principal do jogo, onde o jogador pode escolher o que fazer
    print('O que deseja fazer?')
    try:
        escolha = int(input('1- Arena\n2- Loja\n3- Curandeiro\n4- Status '))
    except ValueError:
        print('Digite apenas números válidos!')
        return
    if escolha == 1:
        if jogador["vida_atual"] == 0:
            print("Você está exausto demais para lutar na arena, tente se curar um pouco.")
        else: arena(jogador, inimigos)
    elif escolha == 2: loja(jogador, iloja, equiploja)
    elif escolha == 3: curandeiro(jogador)
    elif escolha == 4: exibe_status(jogador, equiploja)
    else: print('Escolha apenas opções válidas!')
        
    


def subiu_de_nivel(jogador): #função chamada para verificar caso o jogador tenha subido de nível.
                             # caso ele tenha subido de nivel, a função aumenta seus status e printa isso no terminal
    barreira_de_xp = 10 * 2**(jogador["nivel"] - 1)

    #if jogador['exp'] > jogador['exp'] * 2: checa_novamente = True

    if jogador['exp'] >= barreira_de_xp:
        jogador['nivel'] += 1
        print('-'*50)
        print(f'SUBIU DE NÍVEL!\n{jogador["nivel"]-1} -> {jogador["nivel"]}')
        print('Sua vida se regenerou ao máximo!')
        print('-'*50)
        time.sleep(0.5)
        jogador['vida'] += 10
        jogador['vida_atual'] = jogador['vida']
        if jogador['nivel'] % 2 == 0:
            jogador['dano_min'] += 2
            jogador['dano_max'] += 3
            jogador['defesa'] += 2
        exibe_status(jogador, [], levelup=True)
        input('Pressione [ENTER] para prosseguir')

    #if checa_novamente: return subiu_de_nivel(jogador)
    



def luta(jogador, inimigo): #função utilizada pra começar uma luta quando o jogador está na arena
    inimigo_atual = inimigo.copy()
    print('-'*50)
    print(f'{jogador["nome"]} está contra {inimigo_atual["nome"]}')
    print('-'*50)

    while jogador["vida_atual"] > 0 and inimigo_atual["vida_atual"] > 0:
        print('-'*50)
        print(f'{jogador["nome"]}: {jogador["vida_atual"]} de vida | {inimigo_atual["nome"]}: {inimigo_atual["vida_atual"]} de vida')
        print('-'*50)
        time.sleep(1)
        
        if jogador['vida_atual'] <= jogador['vida'] * 0.25 and jogador['pocao'] == True:
            jogador['pocao'] = False
            print(f'{jogador["nome"]} bebe sua poção, se regenerando por completo')
            jogador['vida_atual'] = jogador['vida']

        #dano do jogador
        dano_causado_jogador = random.randint(jogador["dano_min"], jogador["dano_max"]) - inimigo_atual["defesa"]
        if dano_causado_jogador <= 0: dano_causado_jogador = 1
        print(f'{jogador["nome"]} ataca e atinge o(a) {inimigo_atual["nome"]}, causando {dano_causado_jogador} de dano...')
        inimigo_atual["vida_atual"] -= dano_causado_jogador
        time.sleep(1)

        if inimigo_atual["vida_atual"] <= 0: #checagem de morte
            print(f'Você venceu!\nGanhando {inimigo_atual["exp_dado"]} de experiência e {inimigo_atual["ouro_dado"]} de ouro.')
            jogador["exp"] += inimigo_atual["exp_dado"]
            jogador["ouro"] += inimigo_atual["ouro_dado"]
            return True

        #dano do inimigo
        dano_causado_inimigo = random.randint(inimigo_atual["dano_min"], inimigo_atual["dano_max"]) - jogador["defesa"]
        if dano_causado_inimigo <= 0: dano_causado_inimigo = 1
        print(f'{inimigo_atual["nome"]} ataca e atinge o(a) {jogador["nome"]}, causando {dano_causado_inimigo} de dano...')
        jogador["vida_atual"] -= dano_causado_inimigo
        if jogador["vida_atual"] < 0: jogador["vida_atual"] = 0
        time.sleep(1)

    else:
        if inimigo["vida_atual"] <= 0 and jogador["vida_atual"] > 0:
            print(f'Você venceu!\nGanhando {inimigo_atual["exp_dado"]} de experiência e {inimigo_atual["ouro_dado"]} de ouro.')
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
    "exp_dado": 8,
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
    ]

    iloja = [
    {"nome": "Poção de cura",
     "preco": 80,
     "desc": "Você usará a poção automaticamente quando estiver com menos de 25% de vida"},
    ]

    equiploja = [
    {"nome": "N/A",
     "preco": 0,
     "desc": "Bom, não da pra ficar pior que isso né?",
     "dano_min": 0,
     "dano_max": 0,
     "id": 0
     },

    {"nome": "Espada de madeira",
     "preco": 100,
     "desc": "Uma espada simples, mas suficiente para algumas coisas",
     "dano_min": 3,
     "dano_max": 3,
     "id": 1
    },
    {"nome": "Espada de cobre",
     "preco": 200,
     "desc": "Não é ótima, mas com certeza melhor que a de madeira",
     "dano_min": 3,
     "dano_max": 3,
     "id": 2
     },
    ]

   
    while True:
        menu(jogador, inimigos, iloja, equiploja)


if __name__ == "__main__":
    main()

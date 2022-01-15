import os
import random
from time import sleep

#-------------------
#Criando Funções
#-------------------

def limpa():
    return os.system('clear')

def rodar(n:int):
    d = [0] * n
    s = 0
    print('Obteve: ')
    for i in range(n):
        d[i] = random.randint(1,6)
        s = s + d[i]
        print(d[i])
    return s

def sino(str: str):
    str = str.upper()
    while (str in ['S', 'N', 'SIM', 'NAO', 'NÃO']) == False :
        str = input('Opção inválida. Tente novamente: [s/n]')
        str = str.upper()
    return str

def numcerto(n: int, min: int, max: int):
    while (n in range(min,max+1)) == False:
        n = int(input('Opção inválida, digite um número entre {} e {}: '.format(min, max)))
    return n

def escolcerta(num,lis):
    while (num in lis) == False:
        num = input('Opção inválida, digite uma opção certa: ')
    return num

def estado(p):
    print('{:10} HABILIDADE {:2}    ENERGIA {:2}    SORTE {:2}'.format(p[0], p[1], p[2], p[3]))

def sorte(p):
    input('Enter para jogar dois dados.')
    n = rodar(2)
    if n > p[3]:
        input('{} não teve sorte.'.format(p[0]))
        return False
    else:
        input('{} teve sorte.'.format(p[0]))
        return True

def SORTE(p,i):
    p[3] = p[3] + i[3] // 2
    if p[3] > i[3]:
        p[3] = i[3]
    return p

def HABILIDADE(p,i):
    p[1] = p[1] + i[1] // 2
    if p[1] > i[1]:
        p[1] = i[1]
    return p

def ENERGIA(p,i):
    p[2] = p[2] + i[2] // 2
    if p[2] > i[2]:
        p[2] = i[2]   
    return p

def batalCPD(p,c):
    aux = p
    p[0], p[1], p[2] = 'Copia de {}'.format(c[0]), c[1], c[2]
    p = batalha(p,c)
    p[0], p[1], p[2] = aux[0], aux[1], aux[2]
    if c[2] > 0:
        p = batalha(p,c)
    return p

def batalha(p,c):
    while p[2] > 0 and c[2] > 0:
        limpa()
        estado(p)
        estado(c)
        input('\nEnter para jogar dois dados da criatura.')
        n = rodar(2)
        print('{} tem força de ataque {}'.format(c[0], n + c[1]))
        gc = n + c[1]
        input('\nEnter para jogar dois dados para {}'.format(p[0]))
        n = rodar(2)
        print('{} tem força de ataque {}'.format(p[0], n + p[1]))
        gp = n + p[1]
        if gc < gp:
            print('\n{} feriu a criatura'.format(p[0]))
            sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n]'))
            sn = sino(sn) 
            if sn in ['S', 'SIM']:
                so = sorte(p)
                p[3] = p[3] - 1
                if so:
                    s = 2
                else:
                    s = - 1
            elif sn in ['N', 'NAO', 'NÃO']:
                s = 0
            input('{} perde {} pontos de energia'.format(c[0], 2 + s))
            c[2] = c[2] - 2 - s
        elif gp < gc:
            print('\n{} feriu a {}'.format(c[0], p[0]))
            sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n]'))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                so = sorte(p)
                p[3] = p[3] - 1
                if so:
                    s = 1
                else:
                    s = - 1
            elif sn in ['N', 'NAO', 'NÃO']:
                s = 0
            input('{} perde {} pontos de energia'.format(p[0], 2 - s))
            p[2] = p[2] - 2 + s
        else:
            input('\nAmbos se defenderam dos golpes')
    return p

def batalmult(p,cr):
    n = 0
    while (n + 1 < len(cr)) and p[2] > 0:
        c = cr[n]
        p = batalha(p,c)
        n = n + 1
            
    return p

def fujasorte(p):
    sn = input('{} esta tentando fugir e foi ferido na tentativa.\nQuer testar sorte para determinar a gravidade do ferimento? [s/n]'.format(p[0]))
    sn = sino(sn)
    if sn in ['S', 'SIM']:
        so = sorte(p)
        if so:
            s = 1
        else:
            s = - 1
    else:
        s = 0
    p[2] = p[2] - 2 + s
    input('{} perde {} pontos de ENERGIA'.format(p[0], 2 - s))
    return p

#-------------------
#Criando personagem
#-------------------

limpa()
print('Criando personagem')
nome = 'Dennis'
#nome = input('Digite seu nome: ')
#input('\nEnter para jogar um dado.')
n = rodar(1)
print('Sua HABILIDADE inicial é {}'.format(n + 6))
hab0 = 6 + n
#input('\nEnter para jogar dois dados.')
n = rodar(2)
print('Sua ENERGIA inicial é {}'.format(n + 12))
ene0 = 12 + n
#input('\nEnter para jogar um dado.')
n = rodar(1)
print('Sua SORTE inicial é {}'.format(n + 6))
sor0 = 6 + n
pers0 = [nome, hab0, ene0, sor0]
perso = pers0.copy()
input('Enter para continuar.')

#------------------
# Escolhendo MAGIA
#------------------

limpa()
estado(perso)
#input('\nEnter para jogar dois dados e determinar a MAGIA')
n = rodar(2)
MAGIA0 = 6 + n
MAGIA = MAGIA0
print('MAGIA = {}'.format(MAGIA0))
print('Você pode escolher um total de {} encantos mágicos.\nEscolha sabiamente:\n'.format(MAGIA))
#sleep(2)
print('Cópia de Criatura\n')
print('Este encanto permitirá que você faça aparecer uma réplica perfeita de qualquer criatura contra a')
print('qual você esteja lutando. A réplica terá os mesmos índices de HABILIDADE e ENERGIA e os')
print('mesmos poderes do original. Mas a réplica estará sob seu controle, e você poderá, por exemplo,')
print('instruí-la para que ataque a criatura original e ficar assistindo a batalha de camarote!\n')
print('Quantos encantos de Copia de criatura você quer?')
#CDC = int(input('Restam {}\n'.format(MAGIA)))
CDC = 1
CDC = numcerto(CDC,0,MAGIA)
MAGIA = MAGIA - CDC

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nPercepção Extra-Sensorial\n')
print('Com este encanto, você poderá sintonizar comprimentos de ondas psíquicas. Isso poderá ajudá-lo a')
print('ler a mente de uma criatura ou descobrir o que está por trás de uma porta trancada. Porém, às vezes,')
print('este encanto pode dar informações equivocadas, se houver mais de uma fonte psíquica perto de uma')
print('outra.\n')
print('Quantos encantos de Percepção Extra-Sensorial você quer?')
#PES = int(input('Restam {}\n'.format(MAGIA)))
PES = 0
PES = numcerto(PES,0,MAGIA)
MAGIA = MAGIA - PES

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nFogo\n')
print('Todas as criaturas têm medo do fogo, e este encanto dá o poder de fazer aparecer fogo segundo a')
print('sua vontade. Você poderá causar uma pequena explosão no chão que queimará por vários segundos')
print('ou criar uma barreira de fogo para manter criaturas à distância.\n')
print('Quantos encantos de Fogo você quer?')
#Fog = int(input('Restam {}\n'.format(MAGIA)))
Fog = 0
Fog = numcerto(Fog,0,MAGIA)
MAGIA = MAGIA - Fog

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nOuro dos Tolos\n')
print('Este encanto transformará pedra comum em uma pilha do que parece ser ouro. Contudo, o encanto é')
print('apenas uma forma de encanto da ilusão - embora mais confiável do que o Encanto da ilusão abaixo')
print('- e a pilha de ouro logo voltará a ser pedra.\n')
print('Quantos encantos de Ouro dos Tolos você quer?')
#ODT = int(input('Restam {}\n'.format(MAGIA)))
ODT = 0
ODT = numcerto(ODT,0,MAGIA)
MAGIA = MAGIA - ODT

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nIlusão\n')
print('Este é um encanto poderoso, mas que não é muito confiável. Através deste encanto, você poderá')
print('criar uma ilusão convincente (por exemplo, que você se transformou em serpente, ou que o chão')
print('está coberto de carvão em brasa) para enganar uma criatura. O encanto ficará imediatamente sem')
print('efeito se acontecer qualquer coisa que desfaça a ilusão (por exemplo, você convence uma criatura')
print('que se transformou em uma serpente e então imediatamente atinge sua cabeça com um golpe de')
print('espada!). É eficiente sobre tudo com criaturas inteligentes.\n')
print('Quantos encantos de Ilusão você quer?')
#I = int(input('Restam {}\n'.format(MAGIA)))
I = 0
I = numcerto(I,0,MAGIA)
MAGIA = MAGIA - I

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nLevitação\n')
print('Você pode lançar este encanto sobre objetos, adversários ou até sobre você mesmo. Livra quem o')
print('recebe dos efeitos da gravidade e assim fará com que tudo que esteja sob a sua influência flutue')
print('livremente no ar, sob o seu controle.\n')
print('Quantos encantos de Levitação você quer?')
#L = int(input('Restam {}\n'.format(MAGIA)))
L = 1
L = numcerto(L,0,MAGIA)
MAGIA = MAGIA - L

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nSorte\n')
print('Este encanto, juntamente com os encantos de Habilidade e Energia, é especial porque pode ser')
print('lançado a qualquer momento durante a sua aventura, a não ser durante uma batalha. Você não')
print('precisa esperar que apareça a opção em uma página. Uma vez lançado, recuperará o seu índice de')
print('SORTE em metade de seu índice de SORTE Inicial (se a sua SORTE inicial for um número ímpar,')
print('subtraia o ½ de sobra). Este encanto nunca levará o seu índice de SORTE a um número superior a')
print('seu nível Inicial Portanto, se você lançar dois encantos da SORTE juntos, o seu índice de SORTE')
print('voltará apenas a ser igual a seu nível Inicial.\n')
print('Quantos encantos de Sorte você quer?')
#S = int(input('Restam {}\n'.format(MAGIA)))
S = 0
S = numcerto(S,0,MAGIA)
MAGIA = MAGIA - S

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nEscudo\n')
print('Ao lançar este encanto, você cria um escudo invisível à sua frente que o protegerá de objetos')
print('físicos, por exemplo flechas, espadas ou criaturas. O escudo não tem efeito contra a magia e,')
print('evidentemente, se nada fora dele pode tocar em você, você também não poderá tocar em nada fora')
print('dele.\n')
print('Quantos encantos de Escudo você quer?')
#Es = int(input('Restam {}\n'.format(MAGIA)))
Es = 1
Es = numcerto(Es,0,MAGIA)
MAGIA = MAGIA - Es

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nHabilidade\n')
print('Este encanto restabelecerá o seu índice de HABILIDADE, aumentando-o em metade de seu valor')
print('Inicial, e pode ser lançado a qualquer momento durante a sua aventura, a não ser em uma batalha.')
print('O Encanto da Habilidade funciona exatamente da mesma maneira que a sorte.\n')
print('Quantos encantos de Habilidade você quer?')
#H = int(input('Restam {}\n'.format(MAGIA)))
H = 1
H = numcerto(H,0,MAGIA)
MAGIA = MAGIA - H

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nEnergia\n')
print('Este encanto recuperará o seu índice de Energia, aumentando-o em metade de seu valor Inicial, e')
print('pode ser lançado a qualquer momento durante a sua aventura. Veja o Encanto da Sorte para')
print('conhecer as regras completas.\n')
print('Quantos encantos de Energia você quer?')
#En = int(input('Restam {}\n'.format(MAGIA)))
En = 1
En = numcerto(En,0,MAGIA)
MAGIA = MAGIA - En

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nForça\n')
print('Este encanto tem o efeito de aumentar muito a sua força, e é muito útil quando se luta contra')
print('criaturas fortes. Porem, deve ser utilizado com cautela, já que é difícil controlar a sua própria força')
print('quando ela aumenta demais.\n')
print('Quantos encantos de Força você quer?')
#For = int(input('Restam {}\n'.format(MAGIA)))
For = 0
For = numcerto(For,0,MAGIA)
MAGIA = MAGIA - For

limpa()
estado(perso)
print('\nMAGIA = {}'.format(MAGIA0))
print('\nFraqueza\n')
print('Criaturas fortes são reduzidas por este encanto a miseráveis fracotes. Não tem efeito contra todas as')
print('criaturas, mas, quando tem efeito, a criatura se torna frágil e muito menos perigosa em uma batalha.\n')
print('Quantos encantos de Fraqueza você quer?')
#Fr = int(input('Restam {}\n'.format(MAGIA)))
Fr = MAGIA
Fr = numcerto(Fr,0,MAGIA)
MAGIA = MAGIA - Fr

ENCANTOS = [CDC, PES, Fog, ODT, I, L, S, Es, H, En, For,Fr]

#ITEMS

ITEM = [['Miríade de bolso', 0], ['Aranha em um vidro', 1], ['Pequenas amoras', 0], ['Adaga', 0], ['Velo de Ouro', 0], ['Espelho de Prata', 1], ['Escova de Cabelo', 0]]
CRIATURA = [['GARK', 7, 11, 0], ['FERA DAS GARRAS', 9, 14, 0], ['HOMEM-ARANHA', 7, 5, 0]]

#ADAGA: Ela causará automaticamente a perda de dois pontos de ENERGIA sem necessidade de jogar dados para conhecer a Força de Ataque. Mas você só poderá usá-la uma vez.

# Começa a História
limpa()
print('HISTÓRIA\n')
print('O ordeiro e generoso povo do Vale dos Salgueiros vive há oito anos sob o terror e medo do')
print('feiticeiro Balthus Dire. Terror – porque o poder dele é realmente aterrorizante - e medo causados')
print('pela notícia que acabou chegando aos ouvidos desse povo, vinda dos domínios do feiticeiro, de que')
#sleep(4)
print('seus ambiciosos planos de conquista começariam pelo próprio Vale.\n')
print('Um fiel Semi-Elfo enviado em uma missão de espionagem à Torre Negra voltou galopando para o')
print('Vale há três dias com uma mensagem desesperada. Do interior das cavernas de Rocha Escarpada,')
print('Balthus Dire tinha recrutado um exército de Caóticos e se preparava para atacar com eles o Vale')
print('dentro de uma semana.\n')
#sleep(4)
print('O bom Rei Salamon era um homem de ação. Foram enviados mensageiros por todo o Vale no')
print('mesmo dia para preparar as defesas e convocar os homens para a guerra. Foram enviados também')
print('cavaleiros à Grande Floresta de Yore para avisar aos Semi-Elfos que moravam lá e fazer um apelo')
print('para que se aliassem às forças. O Rei Salamon era também um homem sábio. Ele sabia muito bem')
print('que as notícias inevitavelmente chegariam aos ouvidos do Grande Mago de Yore, um mestre da')
print('magia branca de grandes poderes, que vivia nas profundezas da floresta. O mago era velho e não')
print('resistiria a uma batalha destas proporções. Mas ele havia ensinado suas artes a vários jovens magos,')
print('e talvez um de seus discípulos de magia ajudasse o rei e seus súditos com coragem e ambição.\n')
#sleep(4)
print('Você é o aluno brilhante do Grande Mago de Yore. Ele tem sido um Mestre duro, e sua própria')
print('impaciência muitas vezes foi mais forte do que você. Talvez um pouco precipitadamente, você')
print('partiu de imediato para a corte de Salamon. O rei recebeu-o entusiasticamente e explicou seu plano.')
print('A batalha poderia ser evitada sem derramamento de sangue se Balthus fosse assassinado antes que')
print('seu exército pudesse ser reunido.\n')
#sleep(4)
print('A missão que você tem pela frente é extremamente perigosa. Balthus Dire está cercado, em sua')
print('Cidadela, por uma multidão de criaturas assombrosas. Embora a Magia seja a sua arma mais forte,')
print('haverá momentos em que você terá que confiar em sua espada para sobreviver.\n')
#sleep(4)
print('O Rei Salamon expôs a você como seria a sua missão e o advertiu dos perigos que estavam à sua')
print('frente. Há um caminho melhor para atravessar a Cidadela. Se você o descobrir, terá êxito com um')
print('mínimo de risco para a sua pessoa. Talvez você precise de várias viagens para descobrir o caminho')
print('mais fácil para atravessar a Cidadela.\n')
#sleep(4)
print('Você deixa o Vale dos Salgueiros na longa caminhada para a Torre Negra. No sopé da colina de')
print('Rocha Escarpada, você pode ver sua silhueta contra o céu escuro...\n')
input('Enter para continuar.')


# Historia

def his1(p,enc,ite):
    n = int(input('O sol se põe. Enquanto o crepúsculo se transforma em escuridão, você começa a subir a colina na direção da ameaçadora forma que se desenha contra o céu noturno. A Cidadela fica a menos de uma hora de escalada.\n\nA uma certa distância de seus muros, você pára para descansar - um erro, uma vez que, dessa posição, ela parece um espectro medonho do qual não se pode escapar. Os cabelos no seu pescoço se arrepiam enquanto você a observa.\n\nMas você se envergonha de seus medos. Com inflexível decisão, você marcha adiante na direção do portão principal, onde você sabe que encontrará guardas à sua espera. Você considera suas opções. Já pensou em se apresentar como um especialista em plantas medicinais que veio tratar de um guarda com febre. Poderia também se dizer um comerciante ou artesão - talvez um carpinteiro. Poderia até mesmo ser um nômade que buscasse abrigo para a noite.\n\nEnquanto você pondera as possibilidades, e as histórias que terá que contar aos guardas, acaba chegando à trilha principal que conduz aos portões. Duas lanternas brilham em cada um dos lados da porta levadiça.\n\nVocê ouve grunhidos abafados ao se aproximar, e vê duas criaturas de aparência absurda. Do lado esquerdo está uma criatura horrível, com a cabeça de um cachorro e o corpo de um grande macaco, flexionando seus braços fortíssimos. Do outro lado, encontra-se de fato o seu oposto, com a cabeça de um macaco no corpo de um cachorro grande. Este último guarda se aproxima nas suas quatro patas. Pára a alguns metros de distância diante de você, ergue-se sobre as patas traseiras e dirige a palavra a você.\n\nPor qual das histórias você optará?\n1. Você se apresentará como um especialista em plantas medicinais?\n2. Você dirá que é um comerciante?\n3. Você pedirá abrigo para pernoitar?\n\nDigite o número da sua história: '))
    n = numcerto(n,1,3)
    if n == 1:
        n = 261
    elif n == 2:
        n = 230
    else:
        n = 20
    return [p, enc, ite, n]

h = [his1]

def his2(p,enc,ite):
    n = int(input('Um pouco adiante na passagem há uma porta do lado direito. Esta porta está coberta por estranhos\ncaracteres, em uma linguagem que você não compreende. Você tentará abrir a porta (escolha 1)\nou continuará seguindo a passagem (escolha 2)?\n\nDigite sua opção: '))
    n = numcerto(n, 1, 2)
    if  n== 1:
        n = 142
    else:
        n = 343
    return [p, enc, ite, n]

h = h + [his2]

def his3(p,enc,ite):
    n = int(input('O que você oferecerá a eles?\n\n1. Uma Miríade de Bolso? (Possui {})\n2. Uma Aranha em um Vidro? (Possui {})\n3. Um punhado de Pequenas Amoras? (Possui {})\n\nSe você não puder oferecer nenhuma dessas coisas, poderá desembainhar a sua espada (escolha 4)ou se dirigir para a porta mais distante (escolha 5).\n'.format(ite[0][1], ite[1][1], ite[2][1])))
    c = [ite[0][1], ite[1][1], ite[2][1], 1, 1]
    n = numcerto(n, 1, 5)
    while c[n - 1] == 0:
        n = int(input('Não possui esse item, tente novamente: '))
        n = numcerto(n, 1, 5)
    if n == 1:
        ite[0][1] = ite[0][1] - 1
        n = 327
    elif n == 2:
        ite[1][1] = ite[1][1] - 1
        n = 59
    elif n == 3:
        ite[1][1] = ite[1][1] - 1
        n = 236
    elif n == 4:
        n = 286
    else:
        n = 366
    return [p, enc, ite, n]

h = h + [his3]

def his4(p,enc,ite):
    print('Você faz aparecer uma bola de fogo e a manda voando no rosto da criatura. Porém, fica assistindo\ndesanimado ao vê-la ricochetear sem nenhum efeito! Você pode lançar rapidamente um Encanto de\nCópia de Criatura, ou desembainhar a sua espada.\nEncantos de Copia Criatura = {}\n'.format(enc[0]))
    if enc[0] == 0:
        input('Você não possui encantos de Copia de Criatura!')
        n = 303
    else:
        n = int(input('1. Lanzar encanto de Criatura.\n2. Desembainar espada.\n\nDigite sua opção: '))
        n = numcerto(n, 1, 2)
        if n == 1:
            enc[0] = enc[0] - 1
            n = 190
        else:
            n = 303
    return [p, enc, ite, n]

h = h + [his4]    

def his5(p, enc, ite):
    n = int(input('Você experimenta a maçaneta da porta e ela gira, abrindo para um outro corredor. Logo adiante, a\npassagem vira para a direita e termina pouco depois em outra porta. Nesta porta há um letreiro que\ndiz "Por Favor Toque a Campainha para Chamar o Mordomo". Uma corda - evidentemente a\ncampainha - pende ao lado da porta. Você toca a campainha conforme indicado (escolha 1) ou\nexperimenta a maçaneta da porta (escolha 2)?\n\nDigite sua opção: '))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 40
    else:
        n = 361
    return [p, enc, ite, n]

h = h + [his5]

def his6(p, enc, ite):
    input('o caminho segue ao longo do rio por vários metros e depois volta a penetrar na rocha. Você segue o\ncaminho por algum tempo.')
    n = 367
    return [p, enc, ite, n]

h = h + [his6]

def his7(p, enc, ite):
    print('A porta está trancada. Você pode tentar pô-la abaixo, batendo nela com o ombro, ou\npode lançar um Encanto da Força sobre você mesmo e tentar arrancar a porta das suas dobradiças.\n')
    if enc[10] == 0:
        input('Você não possui encantos de Força')
        n = 268
    else:
        n = int(input('1. Bater a porta com o ombro.\n2. Usar encanto da Força.\n\nDigite sua opção: '))
        n = numcerto(n, 1, 2)
        if n == 2:
            enc[10] = enc[10] - 1
            n = 116
        else:
            n = 268
    return [p, enc, ite, n]

h = h + [his7]

def his8(p, enc, ite):
    input('Ela observa espantada o aparecimento de uma réplica perfeita dela mesma entre vocês dois. Ela\nrecua um pouco, e você orienta a sua criação para o ataque. Mas, quando elas se aproximam uma da\noutra, acontece uma coisa estranha. Elas parecem ser incapazes de chegar perto uma da outra, como\nduas extremidades giratórias, e sempre separam-se bruscamente de um salto. Porém, sua própria\ncópia pelo menos forçou a criatura a se afastar de você para uma certa distância, permitindo que\nvocê corra para a entrada principal da Cidadela.\n')
    n = 218
    return [p, enc, ite, n]

h = h + [his8]

def his9(p, enc, ite):
    input('Sob o seu Encanto da Ilusão, a multidão de espectadores olha você começar a jogar. Você observa\numas duas rodadas e a tensão cresce. Você resolve que é melhor sair do aposento sem mais perda de\ntempo.\n')
    n = 31
    return [p, enc, ite, n]

h = h + [his9]

def his10(p, enc, ite):
    input('Você tateia pela rocha e acaba por encontrar uma pequena alavanca. Ao puxar esta alavanca, a face\nda rocha esfarela um pouco e aparece uma pequena abertura. Você sobe por esta abertura e chega a\numa passagem. Descendo a passagem para a esquerda, você pode ver uma porta e resolve\ninvestigar.\n')
    n = 249
    return [p, enc, ite, n]

h = h + [his10]

def his11(p, enc, ite):
    print('Você pode usar:\n\n1. Um Encanto do Ouro dos Tolos = {}\n2. Um Encanto de Cópia de Criatura = {}\n3. Um Encanto da Percepção Extra-Sensorial = {}\n4. Um Encanto da Fraqueza = {}\n'.format(enc[3], enc[0], enc[1], enc[11]))
    print('Se você não tiver nenhum desses encantos, terá que desembainhar a sua espada e lutar.')
    if (enc[3] + enc[0] + enc[1] + enc[11]) == 0:
        n = 249
        input('Você não possui nenhum desses encantos.!')
    else:
        n = int(input('Escolha o encanto que deseja usar: '))
        n = numcerto(n, 1, 4)
        e = [enc[3], enc[0], enc[1], enc[11]]
        while e[n - 1] == 0:
            n = int(input('Você não possui esse encanto, por favor escolha outro: '))
            n = numcerto(n, 1, 4)
    if n == 1:
        n = 36
        enc[3] = enc[3] - 1
    elif n == 2:
        n = 262
        enc[0] = enc[0] - 1
    elif n == 3:
        n = 128
        enc[1] = enc[1] - 1
    else:
        n = 152
        enc[11] = enc[11] - 1
    return [p, enc, ite, n]

h = h + [his11]

def his12(p, enc, ite):
    n = int(input('Ele fica parado diante de você, respirando pesadamente. O Encanto dele evidentemente foi bastante exaustivo. Você pode usar essa oportunidade para:\n\n1. Deslocar-se rapidamente para o armário das armas.\n2. Pular para debaixo da mesa.\n3. Correr para a janela.\n\nDigite sua opção: '))
    n = numcerto(n, 1, 3)
    if n == 1:
        n = 274
    elif n == 2:
        n = 335
    else:
        n = 78
    return [p, enc, ite, n]

h = h + [his12]

def his13(p, enc, ite):
    print('A maçaneta gira e você abre a porta para um outro aposento, onde há bastante atividade. Três\nvelhas feias, com narizes e queixos compridos, circulam pelo aposento - que parece ser alguma\nespécie de cozinha - pegando vários ingredientes dos armários e acrescentando-os a um caldo\ndentro de um grande caldeirão. Há um pedaço de carne assando em um espeto, embaixo de uma\ngrande chaminé. Olhando mais atentamente, você descobre que a carne, na verdade, não é de um\nanimal, mas sim um Anão inteiro que escurece ao fogo. Uma das mulheres olha para você e diz:\n"Ah, você deve ser o novo empregado...ou é a próxima refeição?", com o que todas as três\ncomeçam a dar gargalhadas e gritos enquanto riem.')
    n = int(input('1. Você deixará que elas acreditem que você é o novo empregado que elas estão esperando; ou\n2. Quer investigar o aposento com mais vagar.\n\nDigite sua opção: '))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 302
    else:
        n = 215
    return [p, enc, ite, n]

h = h + [his13]

def his14(p, enc, ite):
    print('A sombra do muro dificulta muito a visão. Uma pedra solta desliza, e você perde o equilíbrio,\noscilando à beira do que você tem consciência de que deve ser um poço profundo. Teste a sua\nSorte. Se você tiver sorte, recupera o equilíbrio e caminha em segurança. Você pode então dar a\nvolta no poço e continuar. Se você não tiver sorte, cai lá dentro.')
    if p[3] == 0:
        so = False
        input('Você não tem sorte!')
    else:
        so = sorte(p)
        p[3] = p[3] - 1
    if so:
        n = 79
    else:
        n = 100
    return [p, enc, ite, n]

h = h + [his14]

def his15(p, enc, ite):
    input('A adaga é realmente uma obra de arte e sem dúvida valia um bom preço. A lâmina é feita de metal\nbrilhante, e o cabo é de um couro verde peculiar, com pedras incrustadas. Você lê uma inscrição\nque diz que esta é uma adaga de arremesso encantada que nunca erra. Em um combate futuro, você\npoderá usar esta adaga para arremessar em um adversário. Ela causará automaticamente a perda de\ndois pontos de ENERGIA sem necessidade de jogar dados para conhecer a Força de Ataque. Mas\nvocê só poderá usá-la uma vez. Você põe a adaga em seu cinturão e parte na direção da Cidadela.\n')
    ite[3][1] = ite[3][1] + 1
    n = 245
    return [p, enc, ite, n]

h = h + [his15]

def his16(p, enc, ite):
    input('''Resolva esta batalha:
    
GARK        HABILIDADE 7        ENERGIA 11
    
Depois de quatro Séries de Ataques, você poderá Fugir por uma das portas na extremidade mais distante do aposento.
''')
    c = CRIATURA[0].copy()
    cont = 0
    while p[2] > 0 and c[2] > 0:
        if ite[3][1] > 0:
            sn = str(input('Deseja utilizar a Adaga do cinto? [s/n]'))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        limpa()
        estado(p)
        print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
        input('\nEnter para jogar dois dados da criatura.')
        n = rodar(2)
        print('{} tem força de ataque {}'.format(c[0], n + c[1]))
        gc = n + c[1]
        input('\nEnter para jogar dois dados para {}'.format(p[0]))
        n = rodar(2)
        print('{} tem força de ataque {}'.format(p[0], n + p[1]))
        gp = n + p[1]
        if gc < gp:
            print('\n{} feriu a criatura'.format(p[0]))
            s = 0
            if p[3] > 1:
                sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n]'))
                sn = sino(sn) 
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 2
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(c[0], 2 + s))
            c[2] = c[2] - 2 - s
        elif gp < gc:
            print('\n{} feriu a {}'.format(c[0], p[0]))
            s = 0
            if p[3] > 0:
                sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n]'))
                sn = sino(sn)
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 1
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(p[0], 2 - s))
            p[2] = p[2] - 2 + s
        else:
            input('\nAmbos se defenderam dos golpes')
        cont = cont + 1
        if cont > 3 and c[2] > 0:
            f = str(input('Deseja fugir? [s/n]'))
            f = sino(f)
            if f in ['S', 'SIM']:
                p = fujasorte(p)
                c[2] = 0
                n = 99
                if p[2] < 1:
                    input('{} não conseguiu fugir e perde a batalha. A aventura acaba por aqui.')
        elif c[2] < 1:
            n = 180
        elif p[2] < 1:
            input('{} perdeu a batalha. A aventura acaba por aqui\n'.format(p[0]))
    return [p, enc, ite, n]

h = h + [his16]

def his17(p, enc, ite):
    input('Todo tipo de alimentos estranhos podem ser encontrados nos armários. Globos oculares, línguas,\nlagartixas, frascos de líquidos, ervas e frutos silvestres de diferentes formas e tamanhos. Uma\ngarrafa em especial, contendo um líquido verde transparente, chama a sua atenção. Você não tem\ntempo para ler o rótulo no momento, por isso você a põe no bolso rapidamente, enquanto elas não\nestão olhando. Você lhes diz que a cozinha parece estar em ordem e sai pela porta do lado oposto da\ncozinha.\n')
    n = 93
    return [p, enc, ite, n]

h = h + [his17]

def his18(p, enc, ite):
    n= int(input('Ele aponta para uma seção logo acima do chão, que você examina. Finalmente, você escolhe um\nvolume e senta para ler. Balthus Dire aparentemente é o terceiro de uma linhagem de Feiticeiros\nSenhores da Guerra que governa a Torre Negra e o Reino da Rocha Escarpada. Chegou ao poder\ndepois da morte de seu pai, Craggen Dire, há alguns anos atrás. Os Dires são mestres de Magia\nNegra há gerações, mas sua força e poder duram somente no período noturno; a luz do sol é uma\nespécie de veneno para eles. Pouco tempo depois da morte de seu pai, Balthus Dire casou-se com\nLady Lucretia, ela também uma Feiticeira de Magia Negra, e desde então eles vem reinando juntos\nsobre o Reino da Rocha Escarpada. Ao terminar o livro, você repara que o bibliotecário está com a\nmão junto ao ouvido, aparentemente escutando alguma coisa. Ele dirige a você um olhar\ninquisitivo. Você pode\n\n1. Procurar outro livro útil, que possa ajudá-lo na sua empreitada\n2. Tentar sair da biblioteca pela porta atrás dele.\n\nDigite sua opção: '))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 84
    else:
        n = 31
    return [p, enc, ite, n]

h = h + [his18]

def his19(p, enc, ite):
    print('A escada geme quando você põe o pé nela. Você tenta subir o mais silenciosamente possível, mas a\nmadeira velha range sob o seu peso. De repente, um dos degraus estala, como se acionasse um\ndispositivo de algum tipo. Para sua surpresa, todos os degraus: viram para baixo! Você está agora\nde pé em uma rampa lisa e inclinadíssima! Por mais que você tente, não consegue manter o\nequilíbrio e acaba escorregando pela rampa, rolando de ponta cabeça. Se você quiser usar um\nEncanto da Levitação, poderá voar e descer, fora de perigo, na sacada em cima.\n')
    if enc[5] == 0:
        input('Você não possui o encanto de Levitação')
        n = 254
    else:
        sn = str(input('Deseja usar o Encanto de levitação? [s/n] '))
        sn = sino(sn)
        if sn in ['S', 'SIM']:
            enc[5] = enc[5] - 1
            n = 363
        else:
            n = 254
    return [p, enc, ite, n]

h = h + [his19]

def his20(p, enc, ite):
    print('O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece - \nVocê terá que procurar abrigo em outro lugar. Você pode:\n\n1. Se resignar a lutar.\n2. Pegar uma pedra e lançar um Encanto do Ouro dos Tolos sobre ela, oferecendo-a como uma pepita\nde ouro, para suborná-los, convencendo-os a deixar você entrar.\n')
    if enc[3] == 0:
        input('Você não possui o encanto de Ouro dos Tolos! ')
        n = 288
    else:
        n = int(input('Digite sua opção: '))
        n = numcerto(n)
        if n == 1:
            enc[3] = enc[3] - 1
            n = 96
        else:
            n = 288
    return [p, enc, ite, n]

h = h + [his20]

def his21(p, enc, ite):
    print('''"O que traz você a estas paragens?" ela pergunta. Você conta a ela sua história, evitando
    cuidadosamente revelar a sua verdadeira missão. Ela aconselha você a afastar-se desse lugar, caso
    conheça alguma magia. As criaturas que você encontrou até agora não se comparam com as que
    habitam o interior da Torre da Cidadela propriamente dita. Ela diz que você jamais encontrará o
    senhor sem conseguir primeiro o Velo e deseja sorte para você em sua missão.
    ''')
    p[3] = p[3] + 2
    input('{} ganhou 2 pts de SORTE'.format(p[0]))    
    n = 6
    return [p, enc, ite, n]

h = h + [his21]

def his22(p, enc, ite):
    print('Você abre a porta e sai em um corredor longo e oscuro.') 
    n = 188
    return [p, enc, ite, n]

h = h + [his22]

def his23(p, enc, ite):
    print('''Você abre a porta e sai em uma passagem que continua direto para frente por algum tempo. Vira
    para a esquerda, depois para a direita, até que você chega a um arco à sua frente que dá para um
    grande aposento. Você caminha na direção do aposento e entra nele.''') 
    n = 169
    return [p, enc, ite, n]

h = h + [his23]

def his24(p, enc, ite):
    print('''Você prova o vinho e, enquanto está apreciando o seu sabor, ouve um ruído tilintante. Você se vira
para olhar na direção de onde o ruído está vindo e fica horrorizado ao ver que as garrafas nas
prateleiras estão se mexendo sozinhas. Uma garrafa voa do lugar onde está e se projeta na sua
direção, errando por pouco a sua cabeça e se espatifando na parede atrás de você. Uma outra voa na
sua direção, depois outra, até que você está recebendo uma chuva de garrafas vindas de todas as
direções. Você toma consciência de que sua única defesa é usar o Encanto do Escudo. Lance este
encanto, se você puder.\n''')
    if enc[7] > 0:
        enc[7] = enc[7] - 1
        input('Você possui agora {} Encantos de escudo.'.format(enc[7]))
        n = 372
    else:
        input('Você não possui encantos de escudo')
        n = 219
    return [p, enc, ite, n]

h = h + [his24]

def his25(p, enc, ite):
    print('''A porta abre, dando para um aposento grande e circular. Você coça a cabeça, intrigado. No centro
do aposento, vê uma pequena "ilha", cercada por um fosso largo, na qual está uma arca, trancada
por ferrolhos metálicos. O fosso é largo demais para ser pulado e é muito fundo. Logo na entrada,
há um pedaço de corda. Existe uma outra porta do outro lado do aposento, dando para fora dele. Você\n''')

    if enc[10] == 0:
        n = int(input('''1. Ignora a caixa e contorna o fosso até a outra porta?
2. Pega a corda e formula um plano?

Digite sua opção: '''))
        n = numcerto(n, 1, 2)
    else:
        n = int(input('''1. Ignora a caixa e contorna o fosso até a outra porta?
2. Pega a corda e formula um plano?
3. Lança um Encanto da Força e salta sobre o fosso?

Digite sua opção: '''))
        n = numcerto(n, 1, 3)
    if n == 1:
        n = 206
    elif n == 2:
        n = 239
    else:
        enc[10] = enc[10] - 1
        n = 133
    return [p, enc, ite, n]

h = h + [his25]

def his26(p, enc, ite):
    if (enc[2] + enc[11] + enc[0]) == 0:
        input('Você não pode aplicar nenhum encanto, volte e escolha outra opção.')
        n = 304
    else:
        n = int(input('''Você lançará:
        
1. Um encanto de Fogo?              (possui {})
2. Um encanto de Fraqueza?          (possui {})
3. Um encanto de Cópia de Criatura? (possui {})

Digite sua opção: '''.format(enc[2], enc[11], enc[0])))
        n = numcerto(n, 1, 3)
    l = True
    while l:
        if n == 1 and enc[2] > 0:
            enc[2] = enc[2] - 1
            n = 87
            l = False
        elif n == 2 and enc[11] > 0:
            enc[11] = enc[11] - 1
            n = 345
            l = False
        elif n == 3 and enc[0] > 0:
            enc[0] = enc[0] - 1
            n = 101
            l = False
        else:
            n = int(input('Você não possui esse encanto, digite outra opção: '))
            n = numcerto(n, 1, 3)
    return [p, enc, ite, n]

h = h + [his26]

def his27(p, enc, ite):
    print('''Quando você mostra as Peças de Ouro, as três criaturas interrompem seu caminho. Eles engasgam
ao olhar para suas moedas. Uma mão invisível as agarra e coloca no chão. Elas olham para você, e
uma voz pede mais. Você pega todas as suas Peças de Ouro e joga no centro do aposento. Uma voz
soa, dizendo: "Bem, estranho, você é realmente bem-vindo na casa dos MIKS. Agradecemos o seu
presente. Se está seguindo adiante, vá pela porta à sua frente, mas tome cuidado com os Ganjees.
Desejamos sorte para você na sua jornada." Você pode acrescentar um ponto de SORTE pelos votos
de sucesso dos Miks e sair pela porta à sua frente.\n''')
    p[3] = p[3] + 1
    input('Sua sorte é {}'.format(p[3]))
    n = 206
    return [p, enc, ite, n]

h = h + [his27]

def his28(p, enc, ite):
    n = int(input('''Você lança o Encanto e faz aparecer uma bola de fogo nas suas mãos. Eles interrompem seu
caminho e observam você atentamente. Você joga a bola na direção deles, e eles gritam de medo,
rolando aterrorizados para longe de você, com medo de seus óbvios poderes. Enquanto você ainda
tem controle sobre o Encanto, cria mais três bolas de fogo menores e as arremessa sobre cada um
deles. Eles uivam e se dispersam, rolando pelo corredor para longe de você. Você pode agora
prosseguir

1. pela passagem da esquerda ou
2. pela passagem da direita.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 243
    else:
        n = 2
    return [p, enc, ite, n]
    
h = h + [his28]

def his29(p, enc, ite):
    n = int(input('''Cautelosamente, você se aproxima do homenzinho. Ao chegar perto, um único olho se abre e olha
diretamente no seu rosto. Um sorriso largo se espalha de orelha a orelha na criatura e ela
desaparece! "Bom dia para você!" diz uma vozinha chilreante atrás de você, e, ao voltar-se, você o
vê ali, ainda sorrindo. "Sou O'Seamus, o Duende!", ele diz, dando risinhos, e estende a mão para
você. Ele parece suficientemente amigável

1. Você aperta a mão dele e tenta fazer amizade ou
2. Você desembainha sua espada.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 271
    else:
        n = 131
    return [p, enc, ite, n]
    
h = h + [his29]

def his30(p, enc, ite):
    print('''A fera é imensamente poderosa. Você desembainha a sua espada e a batalha começa:

FERA DAS GARRAS         HABILIDADE: 9       ENERGIA: 14''')
    c = CRIATURA[1].copy()
    cont = 0
    while p[2] > 0 and c[2] > 0 and cont < 4:
        if ite[3][1] > 0:
            sn = str(input('Deseja utilizar a Adaga do cinto? [s/n]'))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        limpa()
        estado(p)
        print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
        input('\nEnter para jogar dois dados da criatura.')
        n = rodar(2)
        print('{} tem força de ataque {}'.format(c[0], n + c[1]))
        gc = n + c[1]
        input('\nEnter para jogar dois dados para {}'.format(p[0]))
        n = rodar(2)
        print('{} tem força de ataque {}'.format(p[0], n + p[1]))
        gp = n + p[1]
        if gc < gp:
            print('\n{} feriu a criatura'.format(p[0]))
            s = 0
            if p[3] > 1:
                sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n]'))
                sn = sino(sn) 
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 2
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(c[0], 2 + s))
            c[2] = c[2] - 2 - s
            cont = cont + 1
        elif gp < gc:
            print('\n{} feriu a {}'.format(c[0], p[0]))
            s = 0
            if p[3] > 0:
                sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n]'))
                sn = sino(sn)
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 1
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(p[0], 2 - s))
            p[2] = p[2] - 2 + s
        else:
            input('\nAmbos se defenderam dos golpes')
    if cont == 4 or c[2] < 1:
        n = 241
    elif p[2] < 1:
        input('{} perdeu a batalha. A aventura acaba por aqui\n'.format(p[0]))
    return [p, enc, ite, n]

h = h + [his30]

def his31(p, enc, ite):
    input('''Você sai do aposento pela porta do outro lado, a qual abre para uma passagem curta que termina em
uma grande porta de madeira. A maçaneta desta porta gira, deixando que você entre em uma grande
câmara.

Enter para continuar: ''')
    n = 169
    return [p, enc, ite, n]
    
h = h + [his31]

def his32(p, enc, ite):
    input('''Passando por sobre os corpos, você se aproxima do portão e chama o porteiro, para em seguida se
esconder na escuridão quando ele se aproxima. Ele vê os corpos e sai para investigar, e, enquanto
isso, você aproveita para esgueirar-se rapidamente pelo portão e trancá-lo do lado de fora.

Enter para continuar: ''')
    n = 251
    return [p, enc, ite, n]
    
h = h + [his32]

def his33(p, enc, ite):
    input('''Quando você tenta se levantar, o Orca e o Goblin agarram você e o seguram no chão, enquanto o
Anão avança com sua clava.

Enter para continuar: ''')
    n = 213
    return [p, enc, ite, n]
    
h = h + [his33]

def his34(p, enc, ite):
    n = int(input('''A chave gira e, retirando a tranca, você abre a caixa, encontrando outra chave, dessa vez talhada em
um metal verde cintilante. Você

1. Experimentará esta nova chave na terceira caixa.
2. Sairá do aposento com as duas chaves.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 89
    else:
        n = 237
    return [p, enc, ite, n]
    
h = h + [his34]

def his35(p, enc, ite):
    n = int(input('''Você se concentra na sua Ilusão.
    
1. Você pode convencê-lo de que ele está sendo atacado por um inimigo.
2. Você pode fazer com que você desapareça, na esperança de que ele virá procurar por você.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 364
    else:
        n = 246
    return [p, enc, ite, n]
    
h = h + [his35]

def his36(p, enc, ite):
    input('''"Bah!", diz o Gark," não é tão fácil me enganar. Jogue fora estes pedaços de latão." A criatura tem a
idéia de que, se você está oferecendo um suborno, deve ser um invasor, o que - para um Gark - é
uma demonstração assombrosa de raciocínio lógico! Ele dá um tapa em você com sua mão enorme,
jogando você sem sentidos no chão. As últimas palavras que você se lembra antes de desmaiar são
ditas pelo Gark orgulhoso: "Para a cadeia com esse aqui!".

Enter para continuar: ''')
    n = 234
    return [p, enc, ite, n]
    
h = h + [his36]

def his37(p, enc, ite):
    input('''Você puxa a pele e a criatura solta silvos altos. Todas as suas cabeças recuam,e ela permanece
quieta, observando você. Há uma porta do outro lado do aposento, e você lentamente se desloca na
direção dela. Quando você está na metade do caminho, uma das cabeças se projeta e arranca o velo
das suas mãos. Mas, ao invés de atacar você, a Hidra se encolhe de volta em um dos cantos. Você
segue para a porta cautelosamente.

Enter para continuar: ''')
    ite[4][1] = ite[4][1] - 1
    n = 229
    return [p, enc, ite, n]
    
h = h + [his37]

def his38(p, enc, ite):
    n = int(input('''A porta abre para uma passagem curta, calçada com pedras pequenas. A uma pequena distância
mais adiante, uma porta elaboradamente entalhada assinala o fim da passagem. Mas, logo antes da
porta, uma passagem lateral sai para a esquerda. Você se aproximada porta, tentando escutar
quaisquer sinais de vida do lado de dentro. Quando sua mão toca a maçaneta, uma voz diz: "Não
bata; simplesmente entre!" vinda de dentro.
    
1. Você entrará no aposento, conforme as instruções.
2. Você resolverá desistir desse aposento e tomar a passagem que sai para a esquerda.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 132
    else:
        n = 306
    return [p, enc, ite, n]
    
h = h + [his38]

def his39(p, enc, ite):
    print('''Você pega o Vidro e, ao fazer isso, os Ganjees ficam ofegantes. "Racknee!" diz uma voz. "Você
voltou!" E com estas palavras; uma mão invisível arranca o vidro das suas mãos, coloca-o no chão e
abre a tampa. O Homem-Aranha volta-se na sua direção e solta um pequeno grunhido. Você
desembainha a sua espada quando a fera avança a passos rápidos para você, furiosamente. Você terá
que lutar contra esta criatura:

HOMEM-ARANHA        HABILIDADE: 9       ENERGIA: 14''')
    ite[1][1] = ite[1][1] - 1
    c = CRIATURA[1].copy()
    cont = 0
    while c[2] > 0 and cont < 1:
        if ite[3][1] > 0:
            sn = str(input('Deseja utilizar a Adaga do cinto? [s/n]'))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        limpa()
        estado(p)
        print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
        input('\nEnter para jogar dois dados da criatura.')
        n = rodar(2)
        print('{} tem força de ataque {}'.format(c[0], n + c[1]))
        gc = n + c[1]
        input('\nEnter para jogar dois dados para {}'.format(p[0]))
        n = rodar(2)
        print('{} tem força de ataque {}'.format(p[0], n + p[1]))
        gp = n + p[1]
        if gc < gp:
            print('\n{} feriu a criatura'.format(p[0]))
            s = 0
            if p[3] > 1:
                sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n]'))
                sn = sino(sn) 
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 2
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(c[0], 2 + s))
            c[2] = c[2] - 2 - s
        elif gp < gc:
            print('\n{} feriu a {}'.format(c[0], p[0]))
            s = 0
            '''if p[3] > 0:
                sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n]'))
                sn = sino(sn)
                if sn in ['S', 'SIM']:
                    so = sorte(p)
                    p[3] = p[3] - 1
                    if so:
                        s = 1
                    else:
                        s = - 1
            input('{} perde {} pontos de energia'.format(p[0], 2 - s))
            p[2] = p[2] - 2 + s'''
            cont = cont + 1
        else:
            input('\nAmbos se defenderam dos golpes')
    if cont == 1:
        n = 208
    elif c[2] < 1:
        input('{} ganhou a batalha.\n'.format(p[0]))
        n = 248
    return [p, enc, ite, n]

h = h + [his39]

def his40(p, enc, ite):
    n = int(input('''Depois de vários minutos, a porta se abre lentamente, e uma criatura corcunda e deformada, com
dentes podres, cabelos desgrenhados e roupas esfarrapadas, aparece na sua frente. "Sim senhor (heh,
heh) - o que posso fazer pelo senhor?" rosna a criatura semi-humana."Estou sendo esperado", você
responde e passa por ele, atravessando a porta com confiança. Ele fica um pouco surpreso com seu
comportamento e gagueja, sem saber se entra em conflito com você ou não. "Onde é a recepção?"
você pergunta. Ele olha para você de soslaio com um dos olhos e faz um gesto na direção de uma
bifurcação para a esquerda, a pouca distância dali.
    
1. Você acreditará nele e tomará a bifurcação para a esquerda. (vá para 243)
2. não confiará nesta criatura imprevisível e tomará a bifurcação da direita.

Digite sua opção: '''))
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 243
    else:
        n = 2
    return [p, enc, ite, n]
    
h = h + [his40]

def his41(p, enc, ite):
    input('''As três mulheres se juntam, fazendo um círculo, e sussurram umas com as outras. Com um risinho,
uma delas volta-se para você e diz: "Está bem, estranho, nós vamos ajudá-lo no seu caminho." Ela
fita você com olhos frios de pedra e aponta primeiro para você, e depois para a parede atrás dela. O
aposento fica escuro, você sente uma sensação de movimento e, quando a escuridão clareia, você
está em outro aposento.

Digite Enter para continuar: ''')
    n = 257
    return [p, enc, ite, n]
    
h = h + [his41]

def his42(p, enc, ite):
    print('''Ela pisca, e os jatos de fogo desaparecem. O que você oferecerá a ela?
    
1. Um Espelho de prata (Possui {})
2. Uma Escova de Cabelo (Possui {})
3. Um vidro contendo o Homem-Aranha (Possui {})
'''.format(ite[5][1], ite[6][1], ite[1][1]))
    if ite[5][1] + ite[6][1] + ite[1][1] > 0 :
        n = int(input('Digite sua opção: '))
        n = numcerto(n,1,3)
        while (n == 1 and ite[5][1] == 0) or (n == 2 and ite[6][1] == 0) or (n == 3 and ite[1][1] == 0):
            n = int(input('Não possui esse item, digite novamente: '))
            n = numcerto(n,1,3)
        if n == 1 :
            ite[5][1] = ite[5][1] - 1
            n = 138
        elif n == 2 :
            ite[6][1] = ite[6][1] - 1
            n = 91
        else :
            ite[1][1] = ite[1][1] - 1
            n = 223
    else :
        n = int(input('''Você não tem nenhuma dessas coisas, terá que dar alguma desculpa, dizendo que perdeu o
presente, e voltar para a sacada, onde pode escolher

1. a porta do meio.
2. a porta mais distante.

Digite sua opção: '''))
        n = numcerto(n,1,2)
        if n == 1:
            n = 64
        else:
            n = 304
    return [p, enc, ite, n]
    
h = h + [his42]

def his43(p, enc, ite):
    input('''Quando você lança o encanto, ele afrouxa o aperto. Gradualmente, sua força diminui, até que ele
acaba por soltar o aperto e cai para trás, ofegante, no chão. Desconte mais um ponto de ENERGIA
enquanto trata de seu braço ferido. Você pode prosseguir no seu caminho.

ENERGIA = {}

Digite Enter para continuar: '''.format(p(2) - 1))
    p[2] = p[2] - 1
    n = 14
    return [p, enc, ite, n]
    
h = h + [his43]

def his44(p, enc, ite):
    n = int(input('''O aposento pára de sacudir e você cai no chão. O armário das armas está trancado, mas você pode
arrebentar a fechadura. Ou pode tirar a sua mochila e procurar uma arma para usar. O que você fará:

1. Escolher uma arma do armário?
2. Pegar um artefato na mochila?

Digite sua opção: '''))
    n = numcerto(n,1,2)
    if n == 1:
        n = 353
    else:
        n = 277
    return [p, enc, ite, n]
    
h = h + [his44]

def his45(p, enc, ite):
    n = int(input('''Se seu estômago aguentar, você poderá experimentar:

1. Um pouco de carne pendurada.
2. Um pedaço de fruta.
3. Uma fatia de queijo.
4. Um naco de pão.

Digite sua opção: '''))
    n = numcerto(n,1,4)
    if n == 1:
        n = 166
    elif n == 2:
        n = 313
    elif n == 3:
        n = 253
    else:
        n = 97
    return [p, enc, ite, n]
    
h = h + [his45]










#n = 1
while perso[2] > 0:
    limpa()
    estado(perso)

#    if ENCANTOS[8] + ENCANTOS[9] + ENCANTOS[6] > 0: # Encanto Habilidade, Energia ou Sorte
#        sn = 'S'
#        while sn in ['S', 'SIM']:
#            sn = input('\nDesejar usar um encantamento agora? [s/n] ')
#            sn = sino(sn)
#            if sn in ['S', 'SIM']:
#                n = int(input('1. Encantos de habilidade = {}\n2. Encantos de energia = {}\n3. Encantos de sorte = {}\n4. Não usar encantoa\n\nDigite sua opção: '.format(ENCANTOS[8], ENCANTOS[9], ENCANTOS[6])))
#                n = numcerto(n,1,4)
#                enc = [ENCANTOS[8], ENCANTOS[9], ENCANTOS[6], 1]
#                while enc[n - 1] == 0:
#                    n = int(input('Você não posue esse encantamento, por favor escolha de novo: '))
#                    n = numcerto(n,1,3)
#                if n == 1:
#                    perso, ENCANTOS[8] = HABILIDADE(perso,pers0), ENCANTOS[8] - 1
#                    print('Nova Habilidade de Dennis = {}'.format(perso[1]))
#                elif n == 2:
#                    perso, ENCANTOS[9] = ENERGIA(perso,pers0), ENCANTOS[9] - 1
#                    print('Nova Energia de Dennis = {}'.format(perso[2]))            
#                elif n == 3:
#                    perso, ENCANTOS[6] = SORTE(perso,pers0), ENCANTOS[6] - 1
#                    print('Nova Sorte de Dennis = {}'.format(perso[3]))
#                else :
#                    sn = 'N'

    print(n)
    n = int(input('A cual capitulo vamos? '))


    limpa()
    estado(perso)
    print('')
    [perso, ENCANTOS, ITEM, n] = h[n-1](perso,ENCANTOS,ITEM)
    if perso[2] < 1:
        sn = str(input('Quer continuar a aventura? [s/n]'))
        sn = sino(sn)
        if sn == 'S' or sn == 'SIM':
            perso[2] = pers0.copy()
            print('Sua energia foi restaurada')
        else:
            break

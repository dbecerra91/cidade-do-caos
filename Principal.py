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
        str = input('Opção inválida. Tente novamente: [s/n] ')
        str = str.upper()
    return str

def esnumero(variavel) :
    vf = variavel.isdigit()
    while vf == False :
        variavel = input('Digite um número: ')
        vf = variavel.isdigit()
    variavel = int(variavel)
    return variavel

def numcerto(n, min: int, max: int) :
    n = esnumero(n)
    while (n in range(min,max+1)) == False:
        n = input('Opção inválida, digite um número entre {} e {}: '.format(min, max))
        n = esnumero(n)
    return n

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
        p[3] = i[3].copy()
    return p

def HABILIDADE(p,i):
    p[1] = p[1] + i[1] // 2
    if p[1] > i[1]:
        p[1] = i[1].copy()
    return p

def ENERGIA(p,i):
    p[2] = p[2] + i[2] // 2
    if p[2] > i[2]:
        p[2] = i[2].copy()
    return p

def fujasorte(p):
    sn = input('{} esta tentando fugir e foi ferido na tentativa.\nQuer testar sorte para determinar a gravidade do ferimento? [s/n] '.format(p[0]))
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

def criarpersonagem():
    limpa()
    print('Criando personagem')
    nome = 'Dennis'
    #nome = srt(input('Digite o nome do personagem: '))
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
    input('Enter para continuar.')
    return [nome, hab0, ene0, sor0]

#------------------
# Escolhendo MAGIA
#------------------


def criarmagia() :
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
    #CDC = input('Restam {}\n'.format(MAGIA))
    CDC = 1
    #CDC = numcerto(CDC,0,MAGIA)
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
    #PES = input('Restam {}\n'.format(MAGIA))
    PES = 0
    #PES = numcerto(PES,0,MAGIA)
    MAGIA = MAGIA - PES

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nFogo\n')
    print('Todas as criaturas têm medo do fogo, e este encanto dá o poder de fazer aparecer fogo segundo a')
    print('sua vontade. Você poderá causar uma pequena explosão no chão que queimará por vários segundos')
    print('ou criar uma barreira de fogo para manter criaturas à distância.\n')
    print('Quantos encantos de Fogo você quer?')
    #Fog = input('Restam {}\n'.format(MAGIA))
    Fog = 1
    #Fog = numcerto(Fog,0,MAGIA)
    MAGIA = MAGIA - Fog

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nOuro dos Tolos\n')
    print('Este encanto transformará pedra comum em uma pilha do que parece ser ouro. Contudo, o encanto é')
    print('apenas uma forma de encanto da ilusão - embora mais confiável do que o Encanto da ilusão abaixo')
    print('- e a pilha de ouro logo voltará a ser pedra.\n')
    print('Quantos encantos de Ouro dos Tolos você quer?')
    #ODT = input('Restam {}\n'.format(MAGIA))
    ODT = 0
    #ODT = numcerto(ODT,0,MAGIA)
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
    #I = input('Restam {}\n'.format(MAGIA))
    I = 0
    #I = numcerto(I,0,MAGIA)
    MAGIA = MAGIA - I

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nLevitação\n')
    print('Você pode lançar este encanto sobre objetos, adversários ou até sobre você mesmo. Livra quem o')
    print('recebe dos efeitos da gravidade e assim fará com que tudo que esteja sob a sua influência flutue')
    print('livremente no ar, sob o seu controle.\n')
    print('Quantos encantos de Levitação você quer?')
    #L = input('Restam {}\n'.format(MAGIA))
    L = 1
    #L = numcerto(L,0,MAGIA)
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
    #S = input('Restam {}\n'.format(MAGIA))
    S = 0
    #S = numcerto(S,0,MAGIA)
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
    #Es = input('Restam {}\n'.format(MAGIA))
    Es = 1
    #Es = numcerto(Es,0,MAGIA)
    MAGIA = MAGIA - Es

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nHabilidade\n')
    print('Este encanto restabelecerá o seu índice de HABILIDADE, aumentando-o em metade de seu valor')
    print('Inicial, e pode ser lançado a qualquer momento durante a sua aventura, a não ser em uma batalha.')
    print('O Encanto da Habilidade funciona exatamente da mesma maneira que a sorte.\n')
    print('Quantos encantos de Habilidade você quer?')
    #H = input('Restam {}\n'.format(MAGIA))
    H = 1
    #H = numcerto(H,0,MAGIA)
    MAGIA = MAGIA - H

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nEnergia\n')
    print('Este encanto recuperará o seu índice de Energia, aumentando-o em metade de seu valor Inicial, e')
    print('pode ser lançado a qualquer momento durante a sua aventura. Veja o Encanto da Sorte para')
    print('conhecer as regras completas.\n')
    print('Quantos encantos de Energia você quer?')
    #En = input('Restam {}\n'.format(MAGIA))
    En = 1
    #En = numcerto(En,0,MAGIA)
    MAGIA = MAGIA - En

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nForça\n')
    print('Este encanto tem o efeito de aumentar muito a sua força, e é muito útil quando se luta contra')
    print('criaturas fortes. Porem, deve ser utilizado com cautela, já que é difícil controlar a sua própria força')
    print('quando ela aumenta demais.\n')
    print('Quantos encantos de Força você quer?')
    #For = input('Restam {}\n'.format(MAGIA))
    For = 1
    #For = numcerto(For,0,MAGIA)
    MAGIA = MAGIA - For

    limpa()
    estado(perso)
    print('\nMAGIA = {}'.format(MAGIA0))
    print('\nFraqueza\n')
    print('Criaturas fortes são reduzidas por este encanto a miseráveis fracotes. Não tem efeito contra todas as')
    print('criaturas, mas, quando tem efeito, a criatura se torna frágil e muito menos perigosa em uma batalha.\n')
    print('Quantos encantos de Fraqueza você quer?')
    #Fr = input('Restam {}\n'.format(MAGIA))
    Fr = MAGIA
    #Fr = numcerto(Fr,0,MAGIA)
    MAGIA = MAGIA - Fr

    ENCANTOS = [CDC, PES, Fog, ODT, I, L, S, Es, H, En, For,Fr]

    return ENCANTOS

ITEM0 = [['Miríade de bolso', 0], ['Aranha em um vidro', 0], ['Pequenas amoras', 0], ['Adaga', 0], ['Velo de Ouro', 0], ['Espelho de Prata', 0], ['Escova de Cabelo', 0], ['Vidro de Unguento', 0], ['Peças de Ouro', 0], ['Essência de Erva de Porco', 0]]
CRIATURA = [['GARK', 7, 11, 0], ['FERA DAS GARRAS', 9, 14, 0], ['HOMEM-ARANHA', 7, 5, 0], ['TENTÁCULO', 15, 2, 0], ['COBRA DE ESGOTO', 6, 7, 0]]

pers0 = criarpersonagem()
perso = pers0.copy()
ENCANTOS = criarmagia()
ITEM = ITEM0.copy()

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
    n = input('''O sol se põe. Enquanto o crepúsculo se transforma em escuridão, você começa a subir a colina na direção da ameaçadora forma que se desenha contra o céu noturno. A Cidadela fica a menos de uma hora de escalada.
    
A uma certa distância de seus muros, você pára para descansar - um erro, uma vez que, dessa posição, ela parece um espectro medonho do qual não se pode escapar. Os cabelos no seu pescoço se arrepiam enquanto você a observa.

Mas você se envergonha de seus medos. Com inflexível decisão, você marcha adiante na direção do portão principal, onde você sabe que encontrará guardas à sua espera. Você considera suas opções. Já pensou em se apresentar como um especialista em plantas medicinais que veio tratar de um guarda com febre. Poderia também se dizer um comerciante ou artesão - talvez um carpinteiro. Poderia até mesmo ser um nômade que buscasse abrigo para a noite.

Enquanto você pondera as possibilidades, e as histórias que terá que contar aos guardas, acaba chegando à trilha principal que conduz aos portões. Duas lanternas brilham em cada um dos lados da porta levadiça.

Você ouve grunhidos abafados ao se aproximar, e vê duas criaturas de aparência absurda. Do lado esquerdo está uma criatura horrível, com a cabeça de um cachorro e o corpo de um grande macaco, flexionando seus braços fortíssimos. Do outro lado, encontra-se de fato o seu oposto, com a cabeça de um macaco no corpo de um cachorro grande. Este último guarda se aproxima nas suas quatro patas. Pára a alguns metros de distância diante de você, ergue-se sobre as patas traseiras e dirige a palavra a você.

Por qual das histórias você optará?

1. Você se apresentará como um especialista em plantas medicinais?
2. Você dirá que é um comerciante?\n3. Você pedirá abrigo para pernoitar?

Digite sua opção: ''')
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
    n = input('''Um pouco adiante na passagem há uma porta do lado direito. Esta porta está coberta por estranhos
caracteres, em uma linguagem que você não compreende. Você:

1. tentará abrir a porta?
2. ontinuará seguindo a passagem?

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if  n == 1:
        n = 142
    else:
        n = 343
    return [p, enc, ite, n]

h = h + [his2]

def his3(p,enc,ite):
    print('''O que você oferecerá a eles?

1. Uma Miríade de Bolso?            (Possui {})
2. Uma Aranha em um Vidro?          (Possui {})
3. Um punhado de Pequenas Amoras?   (Possui {})
'''.format(ite[0][1], ite[1][1], ite[2][1]))
    if ite[0][1] + ite[1][1] + ite[2][1] > 0:
        n = input('Digite sua opção: ')
        n = numcerto(n, 1, 3)
        while (n == 1 and ite[0][1] == 0) or (n == 2 and ite[1][1] == 0) or (n == 3 and ite[2][1] == 0):
            n = input('Você não possui esse item, tente outra opção: ')
            n = numcerto(n, 1, 3)
        if n == 1:
            ite[0][1] = ite[0][1] - 1
            n = 327
        elif n == 2:
            ite[1][1] = ite[1][1] - 1
            n = 59
        elif n == 3:
            ite[2][1] = ite[2][1] - 1
            n = 236
    else :
        n = input('''Você não pode oferecer nenhuma dessas coisas, Você poderá
    
1. Desembainhar a sua espada.
2. Se dirigir para a porta mais distante.
    
Digite sua opção: ''')
        n = numcerto(n, 1, 2)
        if n == 1:
            n = 286
        else:
            n = 366
    return [p, enc, ite, n]

h = h + [his3]

def his4(p,enc,ite):
    print('''Você faz aparecer uma bola de fogo e a manda voando no rosto da criatura. Porém, fica assistindo
desanimado ao vê-la ricochetear sem nenhum efeito! Você pode lançar rapidamente um Encanto de
Cópia de Criatura, ou desembainhar a sua espada.

Encantos de Copia Criatura = {}
'''.format(enc[0]))
    if enc[0] == 0:
        input('Você não possui encantos de Copia de Criatura!')
        n = 303
    else:
        n = input('1. Lanzar encanto de Copia de Criatura.\n2. Desembainar espada.\n\nDigite sua opção: ')
        n = numcerto(n, 1, 2)
        if n == 1:
            enc[0] = enc[0] - 1
            n = 190
        else:
            n = 303
    return [p, enc, ite, n]

h = h + [his4]    

def his5(p, enc, ite):
    n = input('''Você experimenta a maçaneta da porta e ela gira, abrindo para um outro corredor. Logo adiante, a
passagem vira para a direita e termina pouco depois em outra porta. Nesta porta há um letreiro que
diz "Por Favor Toque a Campainha para Chamar o Mordomo". Uma corda - evidentemente a
campainha - pende ao lado da porta.

1. Você toca a campainha conforme indicado?
2. Você experimenta a maçaneta da porta?

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 40
    else:
        n = 361
    return [p, enc, ite, n]

h = h + [his5]

def his6(p, enc, ite):
    input('''O caminho segue ao longo do rio por vários metros e depois volta a penetrar na rocha. Você segue o
caminho por algum tempo.''')
    n = 367
    return [p, enc, ite, n]

h = h + [his6]

def his7(p, enc, ite):
    print('''A porta está trancada. Você pode tentar pô-la abaixo, batendo nela com o ombro, ou
pode lançar um Encanto da Força sobre você mesmo e tentar arrancar a porta das suas dobradiças.
''')
    if enc[10] == 0:
        input('Você não possui encantos de Força.')
        n = 268
    else:
        n = input('''1. Bater a porta com o ombro.
2. Usar encanto da Força.   (Possui {})

Digite sua opção: '''.format(enc[10]))
        n = numcerto(n, 1, 2)
        if n == 2:
            enc[10] = enc[10] - 1
            n = 116
        else:
            n = 268
    return [p, enc, ite, n]

h = h + [his7]

def his8(p, enc, ite):
    input('''Ela observa espantada o aparecimento de uma réplica perfeita dela mesma entre vocês dois. Ela
recua um pouco, e você orienta a sua criação para o ataque. Mas, quando elas se aproximam uma da
outra, acontece uma coisa estranha. Elas parecem ser incapazes de chegar perto uma da outra, como
duas extremidades giratórias, e sempre separam-se bruscamente de um salto. Porém, sua própria
cópia pelo menos forçou a criatura a se afastar de você para uma certa distância, permitindo que
você corra para a entrada principal da Cidadela.''')
    n = 218
    return [p, enc, ite, n]

h = h + [his8]

def his9(p, enc, ite):
    input('''Sob o seu Encanto da Ilusão, a multidão de espectadores olha você começar a jogar. Você observa
umas duas rodadas e a tensão cresce. Você resolve que é melhor sair do aposento sem mais perda de
tempo.''')
    n = 31
    return [p, enc, ite, n]

h = h + [his9]

def his10(p, enc, ite):
    input('''Você tateia pela rocha e acaba por encontrar uma pequena alavanca. Ao puxar esta alavanca, a face
da rocha esfarela um pouco e aparece uma pequena abertura. Você sobe por esta abertura e chega a
uma passagem. Descendo a passagem para a esquerda, você pode ver uma porta e resolve
investigar.''')
    n = 249
    return [p, enc, ite, n]

h = h + [his10]

def his11(p, enc, ite):
    print('''Você pode usar:

1. Um Encanto do Ouro dos Tolos                 (Possui {})
2. Um Encanto de Cópia de Criatura              (Possui {})
3. Um Encanto da Percepção Extra-Sensorial      (Possui {})
4. Um Encanto da Fraqueza                       (Possui {})
'''.format(enc[3], enc[0], enc[1], enc[11]))
    if (enc[3] + enc[0] + enc[1] + enc[11]) == 0:
        n = 249
        input('Você não possui nenhum desses encantos, terá que desembainhar a sua espada e lutar.')
    else:
        n = input('Escolha o encanto que deseja usar: ')
        n = numcerto(n, 1, 4)
        e = [enc[3], enc[0], enc[1], enc[11]]
        while e[n - 1] == 0:
            n = input('Você não possui esse encanto, por favor escolha outro: ')
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
    n = input('''Ele fica parado diante de você, respirando pesadamente. O Encanto dele evidentemente foi bastante exaustivo. Você pode usar essa oportunidade para:
    
1. Deslocar-se rapidamente para o armário das armas.
2. Pular para debaixo da mesa.
3. Correr para a janela.

Digite sua opção: ''')
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
    n = input('''A maçaneta gira e você abre a porta para um outro aposento, onde há bastante atividade. Três
velhas feias, com narizes e queixos compridos, circulam pelo aposento - que parece ser alguma
espécie de cozinha - pegando vários ingredientes dos armários e acrescentando-os a um caldo
dentro de um grande caldeirão. Há um pedaço de carne assando em um espeto, embaixo de uma
grande chaminé. Olhando mais atentamente, você descobre que a carne, na verdade, não é de um
animal, mas sim um Anão inteiro que escurece ao fogo. Uma das mulheres olha para você e diz:
"Ah, você deve ser o novo empregado...ou é a próxima refeição?", com o que todas as três
começam a dar gargalhadas e gritos enquanto riem.

1. Você deixará que elas acreditem que você é o novo empregado que elas estão esperando; ou
2. Quer investigar o aposento com mais vagar.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 302
    else:
        n = 215
    return [p, enc, ite, n]

h = h + [his13]

def his14(p, enc, ite):
    print('''A sombra do muro dificulta muito a visão. Uma pedra solta desliza, e você perde o equilíbrio,
oscilando à beira do que você tem consciência de que deve ser um poço profundo. Teste a sua
Sorte. Se você tiver sorte, recupera o equilíbrio e caminha em segurança. Você pode então dar a
volta no poço e continuar. Se você não tiver sorte, cai lá dentro.
''')
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
    input('''A adaga é realmente uma obra de arte e sem dúvida valia um bom preço. A lâmina é feita de metal
brilhante, e o cabo é de um couro verde peculiar, com pedras incrustadas. Você lê uma inscrição
que diz que esta é uma adaga de arremesso encantada que nunca erra. Em um combate futuro, você
poderá usar esta adaga para arremessar em um adversário. Ela causará automaticamente a perda de
dois pontos de ENERGIA sem necessidade de jogar dados para conhecer a Força de Ataque. Mas
você só poderá usá-la uma vez. Você põe a adaga em seu cinturão e parte na direção da Cidadela.''')
    ite[3][1] = ite[3][1] + 1
    n = 245
    return [p, enc, ite, n]

h = h + [his15]

def his16(p, enc, ite):
    input('''Resolva esta batalha:
    
GARK        HABILIDADE 7        ENERGIA 11
    
Depois de quatro Séries de Ataques, você poderá Fugir por uma das portas na extremidade mais distante do aposento.''')
    c = CRIATURA[0].copy()
    cont = 0
    while p[2] > 0 and c[2] > 0:
        if ite[3][1] > 0:
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            sn = str(input('\nDeseja utilizar a Adaga do cinto? [s/n] '))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        if c[2] > 0 :
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
                    sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n] '))
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
                    sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n] '))
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
            f = str(input('Deseja tentar fugir? [s/n] '))
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
            n = 1
    return [p, enc, ite, n]

h = h + [his16]

def his17(p, enc, ite):
    input('''Todo tipo de alimentos estranhos podem ser encontrados nos armários. Globos oculares, línguas,
lagartixas, frascos de líquidos, ervas e frutos silvestres de diferentes formas e tamanhos. Uma
garrafa em especial, contendo um líquido verde transparente, chama a sua atenção. Você não tem
tempo para ler o rótulo no momento, por isso você a põe no bolso rapidamente, enquanto elas não
estão olhando. Você lhes diz que a cozinha parece estar em ordem e sai pela porta do lado oposto da
cozinha.''')
    n = 93
    return [p, enc, ite, n]

h = h + [his17]

def his18(p, enc, ite):
    n = input('''Ele aponta para uma seção logo acima do chão, que você examina. Finalmente, você escolhe um
volume e senta para ler. Balthus Dire aparentemente é o terceiro de uma linhagem de Feiticeiros
Senhores da Guerra que governa a Torre Negra e o Reino da Rocha Escarpada. Chegou ao poder
depois da morte de seu pai, Craggen Dire, há alguns anos atrás. Os Dires são mestres de Magia
Negra há gerações, mas sua força e poder duram somente no período noturno; a luz do sol é uma
espécie de veneno para eles. Pouco tempo depois da morte de seu pai, Balthus Dire casou-se com
Lady Lucretia, ela também uma Feiticeira de Magia Negra, e desde então eles vem reinando juntos
sobre o Reino da Rocha Escarpada. Ao terminar o livro, você repara que o bibliotecário está com a
mão junto ao ouvido, aparentemente escutando alguma coisa. Ele dirige a você um olhar
inquisitivo. Você pode

1. Procurar outro livro útil, que possa ajudá-lo na sua empreitada.
2. Tentar sair da biblioteca pela porta atrás dele.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 84
    else:
        n = 31
    return [p, enc, ite, n]

h = h + [his18]

def his19(p, enc, ite):
    print('''A escada geme quando você põe o pé nela. Você tenta subir o mais silenciosamente possível, mas a
madeira velha range sob o seu peso. De repente, um dos degraus estala, como se acionasse um
dispositivo de algum tipo. Para sua surpresa, todos os degraus: viram para baixo! Você está agora
de pé em uma rampa lisa e inclinadíssima! Por mais que você tente, não consegue manter o
equilíbrio e acaba escorregando pela rampa, rolando de ponta cabeça. Se você quiser usar um
Encanto da Levitação, poderá voar e descer, fora de perigo, na sacada em cima.
''')
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
    print('''O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece - 
Você terá que procurar abrigo em outro lugar. Você pode:

1. Se resignar a lutar.
2. Pegar uma pedra e lançar um Encanto do Ouro dos Tolos sobre ela, oferecendo-a como uma pepita
   de ouro, para suborná-los, convencendo-os a deixar você entrar.
''')
    if enc[3] == 0:
        input('Você não possui o encanto de Ouro dos Tolos! Vai ter que lutar.')
        n = 288
    else:
        n = input('Digite sua opção: ')
        n = numcerto(n, 1, 2)
        if n == 2:
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
senhor sem conseguir primeiro o Velo e deseja sorte para você em sua missão.''')
    p[3] = p[3] + 2
    input('{} ganhou 2 pts de SORTE.'.format(p[0]))    
    n = 6
    return [p, enc, ite, n]

h = h + [his21]

def his22(p, enc, ite):
    input('Você abre a porta e sai em um corredor longo e oscuro.') 
    n = 188
    return [p, enc, ite, n]

h = h + [his22]

def his23(p, enc, ite):
    input('''Você abre a porta e sai em uma passagem que continua direto para frente por algum tempo. Vira
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
        input('Você usa o encanto e fica com {} Encantos de escudo.'.format(enc[7]))
        n = 372
    else:
        input('Você não possui encantos de escudo.')
        n = 219
    return [p, enc, ite, n]

h = h + [his24]

def his25(p, enc, ite):
    print('''A porta abre, dando para um aposento grande e circular. Você coça a cabeça, intrigado. No centro
do aposento, vê uma pequena "ilha", cercada por um fosso largo, na qual está uma arca, trancada
por ferrolhos metálicos. O fosso é largo demais para ser pulado e é muito fundo. Logo na entrada,
há um pedaço de corda. Existe uma outra porta do outro lado do aposento, dando para fora dele. Você\n''')

    if enc[10] == 0:
        n = input('''1. Ignora a caixa e contorna o fosso até a outra porta?
2. Pega a corda e formula um plano?

Digite sua opção: ''')
        n = numcerto(n, 1, 2)
    else:
        n = input('''1. Ignora a caixa e contorna o fosso até a outra porta?
2. Pega a corda e formula um plano?
3. Lança um Encanto da Força e salta sobre o fosso?

Digite sua opção: ''')
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
        n = input('''Você lançará:
        
1. Um encanto de Fogo?              (possui {})
2. Um encanto de Fraqueza?          (possui {})
3. Um encanto de Cópia de Criatura? (possui {})

Digite sua opção: '''.format(enc[2], enc[11], enc[0]))
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
            n = input('Você não possui esse encanto, digite outra opção: ')
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
    input('Sua sorte agora é {}.'.format(p[3]))
    n = 206
    return [p, enc, ite, n]

h = h + [his27]

def his28(p, enc, ite):
    n = input('''Você lança o Encanto e faz aparecer uma bola de fogo nas suas mãos. Eles interrompem seu
caminho e observam você atentamente. Você joga a bola na direção deles, e eles gritam de medo,
rolando aterrorizados para longe de você, com medo de seus óbvios poderes. Enquanto você ainda
tem controle sobre o Encanto, cria mais três bolas de fogo menores e as arremessa sobre cada um
deles. Eles uivam e se dispersam, rolando pelo corredor para longe de você. Você pode agora
prosseguir pela pasagem da

1. Esquerda.
2. Direita.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 243
    else:
        n = 2
    return [p, enc, ite, n]
    
h = h + [his28]

def his29(p, enc, ite):
    n = input('''Cautelosamente, você se aproxima do homenzinho. Ao chegar perto, um único olho se abre e olha
diretamente no seu rosto. Um sorriso largo se espalha de orelha a orelha na criatura e ela
desaparece! "Bom dia para você!" diz uma vozinha chilreante atrás de você, e, ao voltar-se, você o
vê ali, ainda sorrindo. "Sou O'Seamus, o Duende!", ele diz, dando risinhos, e estende a mão para
você. Ele parece suficientemente amigável. Você:

1. Aperta a mão dele e tenta fazer amizade.
2. Desembainha sua espada.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 271
    else:
        n = 131
    return [p, enc, ite, n]
    
h = h + [his29]

def his30(p, enc, ite):
    input('''A fera é imensamente poderosa. Você desembainha a sua espada e a batalha começa:

FERA DAS GARRAS         HABILIDADE: 9       ENERGIA: 14''')
    c = CRIATURA[1].copy()
    cont = 0
    while p[2] > 0 and c[2] > 0 and cont < 4:
        if ite[3][1] > 0:
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            sn = str(input('\nDeseja utilizar a Adaga do cinto? [s/n] '))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        if c[2] > 0 :
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            input('\nEnter para jogar dois dados da criatura.')
            n = rodar(2)
            print('{} tem força de ataque {}.'.format(c[0], n + c[1]))
            gc = n + c[1]
            input('\nEnter para jogar dois dados para {}.'.format(p[0]))
            n = rodar(2)
            print('{} tem força de ataque {}.'.format(p[0], n + p[1]))
            gp = n + p[1]
            if gc < gp:
                print('\n{} feriu a criatura.'.format(p[0]))
                s = 0
                if p[3] > 1:
                    sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n] '))
                    sn = sino(sn) 
                    if sn in ['S', 'SIM']:
                        so = sorte(p)
                        p[3] = p[3] - 1
                        if so:
                            s = 2
                        else:
                            s = - 1
                input('{} perde {} pontos de energia.'.format(c[0], 2 + s))
                c[2] = c[2] - 2 - s
                cont = cont + 1
            elif gp < gc:
                print('\n{} feriu a {}'.format(c[0], p[0]))
                s = 0
                if p[3] > 0:
                    sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n] '))
                    sn = sino(sn)
                    if sn in ['S', 'SIM']:
                        so = sorte(p)
                        p[3] = p[3] - 1
                        if so:
                            s = 1
                        else:
                            s = - 1
                input('{} perde {} pontos de energia.'.format(p[0], 2 - s))
                p[2] = p[2] - 2 + s
            else:
                input('\nAmbos se defenderam dos golpes.')
    if cont == 4 or c[2] < 1:
        if cont == 4 :
            input('Você atingiu a criatura 4 vezes.')
        n = 241
    elif p[2] < 1:
        input('{} perdeu a batalha. A aventura acaba por aqui.\n'.format(p[0]))
        n = 1
    return [p, enc, ite, n]

h = h + [his30]

def his31(p, enc, ite):
    input('''Você sai do aposento pela porta do outro lado, a qual abre para uma passagem curta que termina em
uma grande porta de madeira. A maçaneta desta porta gira, deixando que você entre em uma grande
câmara.''')
    n = 169
    return [p, enc, ite, n]
    
h = h + [his31]

def his32(p, enc, ite):
    input('''Passando por sobre os corpos, você se aproxima do portão e chama o porteiro, para em seguida se
esconder na escuridão quando ele se aproxima. Ele vê os corpos e sai para investigar, e, enquanto
isso, você aproveita para esgueirar-se rapidamente pelo portão e trancá-lo do lado de fora.''')
    n = 251
    return [p, enc, ite, n]
    
h = h + [his32]

def his33(p, enc, ite):
    input('''Quando você tenta se levantar, o Orca e o Goblin agarram você e o seguram no chão, enquanto o
Anão avança com sua clava.''')
    n = 213
    return [p, enc, ite, n]
    
h = h + [his33]

def his34(p, enc, ite):
    n = input('''A chave gira e, retirando a tranca, você abre a caixa, encontrando outra chave, dessa vez talhada em
um metal verde cintilante. Você

1. Experimentará esta nova chave na terceira caixa.
2. Sairá do aposento com as duas chaves.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 89
    else:
        n = 237
    return [p, enc, ite, n]
    
h = h + [his34]

def his35(p, enc, ite):
    n = input('''Você se concentra na sua Ilusão.
    
1. Você pode convencê-lo de que ele está sendo atacado por um inimigo.
2. Você pode fazer com que você desapareça, na esperança de que ele virá procurar por você.

Digite sua opção: ''')
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
ditas pelo Gark orgulhoso: "Para a cadeia com esse aqui!".''')
    n = 234
    return [p, enc, ite, n]
    
h = h + [his36]

def his37(p, enc, ite):
    input('''Você puxa a pele e a criatura solta silvos altos. Todas as suas cabeças recuam,e ela permanece
quieta, observando você. Há uma porta do outro lado do aposento, e você lentamente se desloca na
direção dela. Quando você está na metade do caminho, uma das cabeças se projeta e arranca o velo
das suas mãos. Mas, ao invés de atacar você, a Hidra se encolhe de volta em um dos cantos. Você
segue para a porta cautelosamente.''')
    n = 229
    return [p, enc, ite, n]
    
h = h + [his37]

def his38(p, enc, ite):
    n = input('''A porta abre para uma passagem curta, calçada com pedras pequenas. A uma pequena distância
mais adiante, uma porta elaboradamente entalhada assinala o fim da passagem. Mas, logo antes da
porta, uma passagem lateral sai para a esquerda. Você se aproximada porta, tentando escutar
quaisquer sinais de vida do lado de dentro. Quando sua mão toca a maçaneta, uma voz diz: "Não
bata; simplesmente entre!" vinda de dentro.
    
1. Você entrará no aposento, conforme as instruções.
2. Você resolverá desistir desse aposento e tomar a passagem que sai para a esquerda.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1:
        n = 132
    else:
        n = 306
    return [p, enc, ite, n]
    
h = h + [his38]

def his39(p, enc, ite):
    input('''Você pega o Vidro e, ao fazer isso, os Ganjees ficam ofegantes. "Racknee!" diz uma voz. "Você
voltou!" E com estas palavras; uma mão invisível arranca o vidro das suas mãos, coloca-o no chão e
abre a tampa. O Homem-Aranha volta-se na sua direção e solta um pequeno grunhido. Você
desembainha a sua espada quando a fera avança a passos rápidos para você, furiosamente. Você terá
que lutar contra esta criatura:

HOMEM-ARANHA        HABILIDADE: 9       ENERGIA: 14''')
    c = CRIATURA[2].copy()
    cont = 0
    while c[2] > 0 and cont < 1:
        if ite[3][1] > 0:
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            sn = str(input('\nDeseja utilizar a Adaga do cinto? [s/n] '))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('{} perde {} pontos de energia'.format(c[0], 2))
        if c[2]> 0 :
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
                    sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n] '))
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
                    sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n] '))
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
    n = input('''Depois de vários minutos, a porta se abre lentamente, e uma criatura corcunda e deformada, com
dentes podres, cabelos desgrenhados e roupas esfarrapadas, aparece na sua frente. "Sim senhor (heh,
heh) - o que posso fazer pelo senhor?" rosna a criatura semi-humana."Estou sendo esperado", você
responde e passa por ele, atravessando a porta com confiança. Ele fica um pouco surpreso com seu
comportamento e gagueja, sem saber se entra em conflito com você ou não. "Onde é a recepção?"
você pergunta. Ele olha para você de soslaio com um dos olhos e faz um gesto na direção de uma
bifurcação para a esquerda, a pouca distância dali. Você:
    
1. Acreditará nele e tomará a bifurcação para a esquerda.
2. Não confiará nesta criatura imprevisível e tomará a bifurcação da direita.

Digite sua opção: ''')
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
está em outro aposento.''')
    n = 257
    return [p, enc, ite, n]
    
h = h + [his41]

def his42(p, enc, ite):
    print('''Ela pisca, e os jatos de fogo desaparecem. O que você oferecerá a ela?
    
1. Um Espelho de prata              (Possui {})
2. Uma Escova de Cabelo             (Possui {})
3. Um vidro contendo o Homem-Aranha (Possui {})
'''.format(ite[5][1], ite[6][1], ite[1][1]))
    if ite[5][1] + ite[6][1] + ite[1][1] > 0 :
        n = input('Digite sua opção: ')
        n = numcerto(n,1,3)
        while (n == 1 and ite[5][1] == 0) or (n == 2 and ite[6][1] == 0) or (n == 3 and ite[1][1] == 0):
            n = input('Não possui esse item, digite novamente: ')
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
        n = input('''Você não tem nenhuma dessas coisas, terá que dar alguma desculpa, dizendo que perdeu o
presente, e voltar para a sacada, onde pode escolher

1. A porta do meio.
2. A porta mais distante.

Digite sua opção: ''')
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
'''.format(p[2] - 1))
    p[2] = p[2] - 1
    n = 14
    return [p, enc, ite, n]
    
h = h + [his43]

def his44(p, enc, ite):
    n = input('''O aposento pára de sacudir e você cai no chão. O armário das armas está trancado, mas você pode
arrebentar a fechadura. Ou pode tirar a sua mochila e procurar uma arma para usar. O que você fará:

1. Escolher uma arma do armário?
2. Pegar um artefato na mochila?

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1:
        n = 353
    else:
        n = 277
    return [p, enc, ite, n]
    
h = h + [his44]

def his45(p, enc, ite):
    n = input('''Se seu estômago aguentar, você poderá experimentar:

1. Um pouco de carne pendurada.
2. Um pedaço de fruta.
3. Uma fatia de queijo.
4. Um naco de pão.

Digite sua opção: ''')
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

def his46(p, enc, ite):
    n = input('''Com um gesto, você estica a mão para frente e aponta o chão sob os pés do feiticeiro. Fumaça e
chamas irrompem do chão. Balthus Dire salta para trás, um pouco admirado, e em seguida fecha os
olhos para se concentrar. Ao se abrirem, você vê um fogo que queima dentro das próprias pupilas, e
ele avança por entre as chamas que você criou. Pegando um punhado de pedras em brasa, ele atira
isso em você.

1. Você se abaixa para se desviar.
2. Você pula para o lado.

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1:
        n = 195
    else:
        n = 74
    return [p, enc, ite, n]

h = h + [his46]

def his47(p, enc, ite):
    print('''Que Encanto você usará:
    
1. Encanto de Cópia de Criatura     (Possui {})
2. Encanto da Ilusão                (Possui {})
3. Encanto de Levitação             (Possui {})
'''.format(enc[0], enc[4], enc[5]))
    if enc[0] + enc[4] + enc[5] > 0 :
        n = input('Digite sua opção: ')
        n = numcerto(n,1,3)
        while (n == 1 and enc[0] == 0) or (n == 2 and enc[4] == 0) or (n == 3 and enc[5] == 0):
            n = input('Não possui esse Encanto, digite novamente: ')
            n = numcerto(n,1,3)
        if n == 1 :
            enc[0] = enc[0] - 1
            n = 8
        elif n == 2 :
            enc[4] = enc[4] - 1
            n = 173
        else :
            enc[5] = enc[5] - 1
            n = 259
    else :
        n = input('''Você não possui nenhum desses encantos, terá que recuar na direção do monumento no centro do
pátio e se esconder dela.''')
        n = 209
    return [p, enc, ite, n]
    
h = h + [his47]

def his48(p, enc, ite):
    n = input('''"Nunca!" grita o feiticeiro, voltando das sombras para enfrentar você. Dessa vez, é você quem sente
o tremor do medo, ao ver que ele também se transformou - mas em uma criatura que poderia fazer
com que um Demônio do Fogo ficasse paralisado. O rosto de Balthus Dire tornou-se feio e com
feições de bruxa, e seus cabelos agora são pequenas serpentes que se contorcem e soltam silvos.

1. Você fugirá desta criatura.
2. Você avançará com seu Tridente.

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1:
        n = 232
    else:
        n = 199
    return [p, enc, ite, n]

h = h + [his48]

def his49(p, enc, ite):
    input('''A criatura fica olhando fixamente para você com ar inquisitivo, como se estivesse insegura em
relação a você.''')
    n = 255
    return [p, enc, ite, n]

h = h + [his49]

def his50(p, enc, ite):
    n = 164
    return [p, enc, ite, n]

h = h + [his50]

def his51(p, enc, ite):
    print('''Você distribui loucamente golpes com sua espada, mas não consegue atingir a criatura. Ou ela é
extremamente rápida, ou não possui um corpo sólido que possa ser atingido. Seus dentes estão
agora rasgando a sua carne, e você sente sangue na perna. Você terá que se proteger com sua
mágica ou enfrentar uma morte certa, trazida por esta criatura que não se vê. Você

1. Lançará um Encanto da Força      (Possui {})
2. Lançará um Encanto da Fraqueza   (Possui {})'''.format(enc[10], enc[11]))
    if enc[10] + enc[11] > 0 :
        n = input('''3. Não quer lançar nenhum dos dois. 
        
Digite sua opção: ''')
        n = numcerto(n,1,3)
        while (n == 1 and enc[10] == 0) or (n == 2 and enc[11] == 0):
            n = input('Não possui esse Encanto, digite novamente: ')
            n = numcerto(n,1,3)
        if n == 1 :
            enc[10] = enc[10] - 1
            n = 301
        elif n == 2 :
            enc[11] = enc[11] - 1
            n = 159
        else :
            n = 280
    else :
        n = input('''Você não possui nenhum desses encantos.''')
        n = 280
    return [p, enc, ite, n]
    
h = h + [his51]

def his52(p, enc, ite):
    n = input('''A porta abre e você segue adiante, batendo-a para que se feche atrás de você. Pouca distância à
frente, você chega a um cruzamento de três caminhos, no qual você toma a passagem que vai na
direção norte. Ela continua por vários metros, conduzindo a uma outra porta. Você pode ouvir risos
e vozes alegres do outro lado. Cautelosamente, você abre a porta que dá para um grande aposento,
onde um grupo de mais ou menos doze criaturas, de todas as formas, tamanhos e cores, estão se
divertindo com jogos. Quando você entra no aposento, uma voz grita: "Olhem esse deve ser Glaz-
Doz-Fut!", com o que todos eles cumprimentam você, convidando-o para juntar-se à brincadeira.
Evidentemente eles estão esperando alguém e confundiram você com o convidado que está
faltando.

1. Você continua fingindo e junta-se a eles.
2. Você dirá a eles que estão enganados e tentará chegar até a porta do outro lado do aposento.

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1 :
        n = 385
    else :
        n = 227
    return [p, enc, ite, n]
    
h = h + [his52]

def his53(p, enc, ite):
    print('''"Para que eu quero suas amoras?" ela ri. "Meu apetite morreu com meu corpo!" E, quando você
olha mais de perto, pode ver que ela também não é nada além de um Fantasma. Ela flutua no ar,
vindo na sua direção.''')
    n = 194
    return [p, enc, ite, n]
    
h = h + [his53]

def his54(p, enc, ite):
    print('''Você procura dentro de sua mochila. O que você pegará:

1. Um Vidro de Unguento?            (Possui {})
2. Uma Miríade de Bolso?            (Possui {})
3. Peças de ouro?                   (Possui {})
'''.format(ite[7][1], ite[0][1], ite[8][1]))
    if ite[7][1] + ite[0][1] + ite[8][1] > 0 :
        n = input('Digite sua opção: ')
        n = numcerto(n,1,3)
        while (n == 1 and ite[7][1] == 0) or (n == 2 and ite[0][1] == 0) or (n == 3 and ite[8][1] == 0):
            n = input('Não possui esse item, digite novamente: ')
            n = numcerto(n,1,3)
        if n == 1 :
            ite[7][1] = ite[7][1] - 1
            n = 287
        elif n == 2 :
            ite[0][1] = ite[0][1] - 1
            n = 160
        else :
            ite[8][1] = ite[8][1] - 1
            n = 27
    else :
        input('Você não tem nenhuma dessas coisas, terá que retornar e escolher de novo.')
        n = 104
    return [p, enc, ite, n]
    
h = h + [his54]

def his55(p, enc, ite):
    n = input('''Você segue a passagem por algum tempo. Ela vira para a direita e acaba chegando a um beco sem
saída. Você pode: 

1. Retornar para a bifurcação e tomar a outra passagem.
2. Procurar passagens secretas.

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1 :
        n = 249
    else :
        n = 10
    return [p, enc, ite, n]
    
h = h + [his55]

def his56(p, enc, ite):
    n = input('''O ELFO NEGRO que se aproxima de você é raquítico e maltrapilho. Ele pergunta se você é um
convidado ou um aventureiro. Você diz que é um convidado que veio até embaixo para provar o
vinho que ele guarda em sua famosa Adega de Vinhos. Com um certo orgulho, ele mostra a você as
garrafas de safras que ele guarda para seu Senhor, o Feiticeiro. Algumas delas, ele afirma, possuem
poderes mágicos. Ele pergunta se você não quer experimentar o vinho. Você prefere provar:

1. O Vinho Tinto?
2. O Vinho Branco?
3. O Vinho Rosé?

4. Recusar a oferta dele e seguir adiante no seu caminho?

Digite sua opção: ''')
    n = numcerto(n,1,4)
    if n == 1 :
        n = 120
    elif n == 2 :
        n = 163
    elif n == 3 :
        n = 334
    else :
        n = 95
    return [p, enc, ite, n]
    
h = h + [his56]

def his57(p, enc, ite):
    so = sorte(p)
    p[3] = p[3] - 1
    if so :
        n = 150
    else :
        n = 233
    return [p, enc, ite, n]
    
h = h + [his57]

def his58(p, enc, ite):
    n = input('''Quando você entra, os Gremlins esvoaçam e guincham excitados, depois voam, passando por você
e saindo pela porta noite adentro. Você agora está sozinho com os cálices. Você se arriscará a beber
alguma coisa? Se o fizer, escolherá:

1. O líquido claro?
2. O líquido vermelho?
3. O líquido leitoso?

4. Ou sairá e prosseguirá na direção da Cidadela?

Digite sua opção: ''')
    n = numcerto(n,1,4)
    if n == 1 :
        n = 298
    elif n == 2 :
        n = 267
    elif n == 3 :
        n = 92
    else :
        n = 156
    return [p, enc, ite, n]
    
h = h + [his58]

def his59(p, enc, ite):
    input('''Eles ficam revoltados com seu presente e correm para o canto do aposento, se escondendo embaixo
das camas. Um tanto desconcertado com o comportamento deles, você deixa o vidro no chão e
segue na direção da porta do outro lado do aposento.''')
    n = 140
    return [p, enc, ite, n]
    
h = h + [his59]

def his60(p, enc, ite):
    print('''As criaturas ficam desconfiadas quando você as pressiona, buscando informações. O Anão salta
rapidamente de pé, brandindo uma clava de madeira, enquanto o Goblin e o Orca pegam espadas e
olham com raiva para você. A namorada do Goblin grita e recua vários passos, enquanto os outros
avançam na sua direção. Você terá que lutar contra eles. Você pode usar um Encanto Mágico:

1. Encanto da Levitação     (Possui {})
2. Encanto da Ilusão        (Possui {})
3. Ou poderá puxar a sua espada e lutar.
'''.format(enc[5], enc[4]))
    if enc[4] + enc[5] < 1 :
        input('''Você não possui nenhúm desses encantos terá puxar sua espada e lutar.''')
        n = 213
    else :
        n = input('Digite sua opção: ')
        n = numcerto(n,1,3)
        while ( n == 1 and enc[5] < 1 ) or ( n == 2 and enc[4] < 1 ) :
            n = input('Não possui esse encanto, Digite outra opção: ')
            n = numcerto(n,1,3)
        if n == 1 :
            enc[5] = enc[5] - 1
            n = 33
        elif n == 2 :
            enc[4] = enc[4] - 1
            n = 295
        else :
            n = 295
    return [p, enc, ite, n]
    
h = h + [his60]

def his61(p, enc, ite):
    input('''Você avança com sua espada. O Devlin pára... e salta sobre você!. Você golpeia com sua espada,
mas não consegue fazer nenhum mal à criatura, que está agora em cima de você. O corpo
incandescente dele está queimando a sua carne e você está em grande agonia. Ainda assim, ele se
mantém firme e você desmaia em choque. Você cai no chão para nunca mais acordar, e o Devlin só
larga quando já tem certeza de que seu corpo está queimado além de qualquer possibilidade de
recuperação. Afinal, você será mesmo a próxima refeição das criaturas da Torre Negra...''')
    p[2], n = 0, 1
    return [p, enc, ite, n]
    
h = h + [his61]

def his62(p, enc, ite):
    print('Com o Gárgula fora de combate, você decide investigar a caixa no pedestal da criatura. Teste a sua Sorte.\n')
    so = sorte(p)
    p[3] = p[3] - 1
    if so :
        input('Pode levar a bolsa com dez Peças de Ouro trancada lá dentro.')
        ite[8][1] = ite[8][1] + 10
    else :
        input('Não consegue abrir a caixa.')
    n = 140
    return [p, enc, ite, n]
    
h = h + [his62]

def his63(p, enc, ite):
    n = input('''Você vai até o índice remissivo e verifica a referência. Ao chegar à página correta, você fica
decepcionado ao descobrir que a seção foi arrancada do livro! Você pode:

1. Olhar os \033[1mCalacorms\033[m.
2. Verificar os \033[1mMiks\033[m.

Digite sua opção: ''')
    n = numcerto(n,1,2)
    if n == 1:
        n = 263
    else :
        n = 135
    return [p, enc, ite, n]
    
h = h + [his63]

def his64(p, enc, ite):
    n = input('''Você ouve junto à porta e consegue escutar vozes esganiçadas rindo e brigando. Você experimenta
a maçaneta e a porta abre. O lado de dentro é um aposento de cores vivas. Há umas poucas camas
pequenas em um canto, e, espalhados pelo chão, há pequenos bonecos de várias criaturas brutas.
Junto à parede do lado direito há uma caixa, e logo adiante da caixa uma porta. No meio do
assoalho, e olhando para você com curiosidade, estão três pequenas criaturas. Têm aparência
humana, mas possuem pele verde, orelhas pontudas e olhos muito apertados. Qual será a sua
atitude? Você:

1. Desembainhará a sua espada e se preparará para lutar contra eles?
2. Procurará em sua mochila alguma coisa para oferecer a eles?
3. Caminhará confiantemente através do aposento para a porta do outro lado?

Digite sua opção: ''')
    n = numcerto(n,1,3)
    if n == 1 :
        n = 286
    elif n == 2 :
        n = 3
    else :
        n = 366
    return [p, enc, ite, n]
    
h = h + [his64]

def his65(p, enc, ite):
    input('Você se ajoelha diante dele e se curva. Ele é de fato o seu senhor agora. Você falhou na sua missão.')
    p[2], n = 0, 1
    return [p, enc, ite, n]
    
h = h + [his65]

def his66(p, enc, ite):
    input('''Eles olham um para o outro e conversam. Um deles se adianta e estende a mão com um pequeno
cubo, que parece ter sido feito de algum tipo de pão ou bolo. A pedido dele, você põe isso na boca e
mastiga. Quando engole, você se sente subitamente forte de novo. Retorne a seus níveis Iniciais de
HABILIDADE e ENERGIA e acrescente um ponto de SORTE. Você agradece a ele pela comida e
a todos pela companhia, depois parte na direção das portas.''')
    n = 270
    p[1] = pers0[1]
    p[2] = pers0[2]
    if p[3] < pers0[3] :
        p[3] = p[3] + 1
    return [p, enc, ite, n]
    
h = h + [his66]

def his67(p, enc, ite):
    print('''Você começa a sua luta contra a criatura. Seu primeiro golpe é certeiro e corta uma das seis
cabeças. As outras cinco avançam sobre você e, para seu horror, mais duas cabeças crescem onde
estava antes a cabeça morta! Uma das cabeças morde profundamente o seu braço. Você perde
quatro pontos de ENERGIA.
''')
    p[2] = p[2] - 4
    if p[2] < 1 :
        input('Você perdeu a batalha contra a criatura.')
        n = 1
    else :
        print('Sua espada obviamente não vai adiantar muito.') 
        if enc[0] < 1 :
            input('Use alguma coisa da sua mochila.')
            n = 226
        else :
            n = input('''Você

1. Usará um Encanto de Cópia de Criatura?   (Possui {})
2. Usará alguma coisa de sua mochila?

Digite sua opção: '''.format(enc[0]))
            n = numcerto(n,1,2)   
            if n == 1 :
                enc[0] = enc[0] - 1
                n = 143
            else :
                n = 226
    return [p, enc, ite, n]
    
h = h + [his67]

def his68(p, enc, ite):
    n = input('''“Por qual eu iria, hein?" ele considera. "Vamos ver... eu não iria por uma das duas portas à esquerda
da porta de maçaneta de cobre, nem a porta à direita da de maçaneta de bronze." Qual delas você
escolherá:
1. A porta de maçaneta de latão?
2. A porta de maçaneta de cobre?
3. A porta de maçaneta de bronze?

Digite sua opção: ''')
    n = numcerto(n, 1, 3)
    if n == 1 :
        n = 207
    elif n == 2 :
        n = 22
    else :
        n = 354
    return [p, enc, ite, n]
    
h = h + [his68]

def his69(p, enc, ite):
    input('''A criatura não é de muita conversa, mas você consegue descobrir que está nas masmorras dos
subterrâneos da Torre Negra e que provavelmente nunca será libertado, a não ser que se já dado aos
Ganjees para o divertimento deles. Quando você pergunta por Balthus Dire, ele fica calado. É
melhor você tentar usar um Encanto para conseguir sair dessa prisão.''')
    n = 193
    return [p, enc, ite, n]
    
h = h + [his69]

def his70(p, enc, ite):
    n = input('''Você voa para cima e mantém-se longe dos botes dele, mas ele não sai do lugar onde está, e não há
meio de você contorná-lo voando para chegar à porta. O Encanto acaba por se esgotar e você tem
que enfrentá-lo de novo. Você:

1. Usa um Encanto da Fraqueza?
2. Usa um Encanto da Força?
3. Desembainha a sua espada?

Digite sua opção: ''')
    n = numcerto(n,1,3)
    if n == 1 :
        n = 307
    elif n == 2 :
        n = 264
    else :
        n = 325
    return [p, enc, ite, n]
    
h = h + [his70]

def his71(p, enc, ite):
    input('''Você desembainha a sua espada e golpeia o tentáculo. O tentáculo não ataca de volta, como uma
criatura normal, mas, ao invés disso, está tentando arrastar você para um grande buraco no chão,
que está se abrindo em torno da base dele. Você não precisa jogar dados para o Tentáculo, uma vez
que ele possui uma Força de Ataque de 15 e um índice de ENERGIA de 2. Jogue para o combate de
maneira normal, mas, se sua própria Força de Ataque ficar abaixo de 15, não subtraia pontos de sua
própria ENERGIA. Porém, se você não derrotar a criatura em três Séries de Ataque, ela conseguirá
arrastar você para seu covil, e sua aventura terá terminado. Se você de fato derrotá-la, poderá
arrancar o tentáculo de sua perna e prosseguir para a entrada principal da Torre Negra. ''')
    c = CRIATURA[3].copy()
    cont = 0
    while c[2] > 0 and cont < 3:
        if ite[3][1] > 0:
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            sn = str(input('\nDeseja utilizar a Adaga do cinto? [s/n] '))
            sn = sino(sn)
            if sn in ['S', 'SIM']:
                ite[3][1] = ite[3][1] - 1
                c[2] = c[2] - 2
                input('\n{} venceu o {}'.format(p[0], c[0]))
        if c[2] > 0 :
            limpa()
            estado(p)
            print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
            gc = c[1]
            input('\nEnter para jogar dois dados para {}'.format(p[0]))
            n = rodar(2)
            print('{} tem força de ataque {}'.format(p[0], n + p[1]))
            gp = n + p[1]
            if gc < gp:
                input('\n{} venceu o {}.'.format(p[0], c[0]))
                c[2] = 0
            else :
                input('\n{}ro ataque realizado.'.format(cont + 1))
                cont = cont + 1
    if cont == 3:
        p[2] = 0
        n = 1
    elif c[2] < 1:
        n = 218
    return [p, enc, ite, n]
    
h = h + [his71]

def his72(p, enc, ite):
    input('''A sorte não está do seu lado. Seu primeiro olhar na direção da criatura com serpentes na cabeça foi
suficiente para selar o seu destino. Você grita de angústia ao sentir que suas juntas começam a
endurecer, e seus membros se tornam pesados e incontroláveis. Sob a ação do olhar da Górgona,
que transforma tudo em pedra, você luta para manter o equilíbrio - mas acaba perdendo-o e cai no
chão. Seu corpo petrificado se despedaça com o impacto, e você agora jaz feito em cacos diante de
Balthus Dire. Você falhou na sua missão.''')
    p[2] = 0
    n = 1
    return [p, enc, ite, n]
    
h = h + [his72]

def his73(p, enc, ite):
    print('''Você pode tentar se livrar da Cobra de Esgoto, ou mantê-la a distância com um encanto.

1. Lutar contra a criatura.

COBRA DE ESGOTO     HABILIDADE 6    ENERGIA 7

2. Lançar um Feitiço de Força (Possui {}).
3. Laçar um Feitiço do Fogo (Possui {}).
'''.format(enc[10], enc[2]))
    if enc[10] + enc[2] > 0 :
        n = input('Digite sua opção: ')
        n = numcerto(n, 1, 3)
        while (n == 2 and enc[10] == 0) or (n == 3 and enc[2] == 0) :
            n = input('Não possui esse fitiço, Digite outra opção: ')
            n = numcerto(n, 1, 3)
        if n == 1 :
            b = True
            f = 0
        elif n == 2:
            b = True
            f = 3
            enc[10] = enc[10] - 1
        else :
            b = False
            enc[2] = enc[2] - 1
            n = 282
    else :
        input('Não possui estes feitiços, terá que lutar.\n')
        b = True
        f = 0
    if b :
        c = CRIATURA[4].copy()
        p[1] = p[1] + f
        while c[2] > 0 and p[2] > 0:
            if ite[3][1] > 0:
                limpa()
                estado(p)
                print('{:10} HABILIDADE {:2}    ENERGIA {:2}'.format(c[0], c[1], c[2]))
                sn = str(input('\nDeseja utilizar a Adaga do cinto? [s/n] '))
                sn = sino(sn)
                if sn in ['S', 'SIM']:
                    ite[3][1] = ite[3][1] - 1
                    c[2] = c[2] - 2
                    input('{} perde {} pontos de energia'.format(c[0], 2))
            if c[2] > 0 :
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
                        sn = str(input('Deseja testar sorte para tentar aumentar o dano? [s/n] '))
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
                        sn = str(input('Deseja testar sorte para tentar diminuir o dano? [s/n] '))
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
        if p[2] < 1:
            input('{} venceu a batalha.\nSua aventura acaba por aqui'.format(c[0]))
            n = 1
        elif c[2] < 1:
            input('{} venceu a batalha.\n'.format(p[0]))
            n = 112
        p[1] = p[1] - f
    return [p, enc, ite, n]
    
h = h + [his73]

def his74(p, enc, ite):
    n = 74

    print('''Ao pular de lado, os olhos do feiticeiro seguem você – e a bola de fogo dele também. Ela atinge
você no peito, derrubando-o no chão. A queimadura custará 4 pontos de ENERGIA.
''')
    p[2] = p[2] - 4
    if p[2] > 0 :
        input('Pode preparar outro Encanto para o seu contra-ataque.')
        n = 377
    else :
        input('Você fica sem energias para continuar.')
        n = 1
    return [p, enc, ite, n]
    
h = h + [his74]

def his75(p, enc, ite):
    input('''Você cruza a soleira, fecha a porta atrás de você e espera algum tempo. Ouve as passadas se
aproximarem e chegarem até a porta. Uma tagarelice incompreensível do outro lado da porta acaba
diminuindo até desaparecer, e você ouve novamente as passadas, desta vez se afastando de você.
Você toca a campainha para chamar o mordomo. ''')
    n = 40
    return [p, enc, ite, n]
    
h = h + [his75]

def his76(p, enc, ite):
    input('''Enquanto você estava tirando suas Amoras da mochila, Balthus Dire ficou se concentrando em um
Encanto. Ele Levanta os olhos e explode numa gargalhada. "Amoras do sono!", ele grita. "O que
você espera que eu faça? Ponha tudo na boca?" Ele estala os dedos e seu Encanto se materializa. ''')
    n = 191
    return [p, enc, ite, n]
    
h = h + [his76]

def his77(p, enc, ite):
    print('''Balthus Dire fica surpreso com seu sucesso. "Então!" ele exclama. "Você se acha mais forte do que
os outros, hein?" Você pode agir rapidamente e lançar um Encanto sobre ele. Qual você escolherá:

1. Um Encanto da Percepção Extra-Sensorial?     (Possui {})
2. Um Encanto do Fogo?                          (Possui {})
3. Um Encanto de Cópia de Criatura?             (Possui {})
'''.format(enc[1], enc[2], enc[0]))
    if (enc[1] + enc[2] + enc[0]) == 0 :
        input('No possui nenhum desse encantos.')
        n = 335
    else :
        n = input('''4. Se preferir não lançar nenhum Encanto.

Digite sua opção: ''')
        n = numcerto(n, 1, 4)
        while (n == 1 and enc[1] == 0) or (n == 2 and enc[2] == 0) or (n == 3 and enc[0] == 0) :
            n = input('Não possui esse Encanto, tente outra opção.')
            n = numcerto(n, 1, 4)
        if n == 1:
            enc[1] = enc[1] - 1
            n = 187
        elif n == 2:
            enc[2] = enc[2] - 1
            n = 46
        elif n == 3 :
            enc[0] = enc[0] - 1
            n = 349
        else :
            n = 335
    return [p, enc, ite, n]
    
h = h + [his77]

def his78(p, enc, ite):
    n = input('''Seus olhos seguem você até a janela. Suas pupilas tornaram-se brancas como o leite. Ele inclina sua
cabeça para trás, pisca uma vez e geme. Jogando a cabeça para frente, ele agora olha fixamente para
você com olhos que se tornaram cor de prata brilhante! Seu olhar é hipnótico, e você terá que agir
rapidamente. Você:

1. Esconde-se por trás de uma das cortinas?
2. Arranca uma das cortinas e joga por cima da cabeça dele?
3. Procura em sua mochila alguma coisa que possa usar?

Digite sua opção: ''')
    n = numcerto(n, 1, 3)
    if n == 1 :
        n = 324
    elif n == 2 :
        n = 124
    else :
        n = 277
    return [p, enc, ite, n]
    
h = h + [his78]

def his79(p, enc, ite):
    input('''No canto mais distante do pátio, você encontra um arbusto diferente, com galhos contorcidos a
partir da haste central, como se estivesse em agonia. As folhas têm a forma de diamantes, com
pequenas amoras por baixo, chatas e com forma de pastilhas. Você pode levar algumas amoras com
você na sua aventura e avançar um pouco mais ao longo do muro para a entrada principal da
Cidadela. ''')
    ite[2][1] = ite[2][1] + 1
    n = 218
    return [p, enc, ite, n]
    
h = h + [his79]

def his80(p, enc, ite):
    n = input('''Quando, você salta por cima da mesa, o feiticeiro gira em torno de si mesmo. Você tropeça e desaba
no chão, ao ver que ele se transformou em uma criatura bem mais perigosa do que você. Seu rosto
agora é o de uma bruxa, e seu cabelo uma massa de serpentes que se contorcem e silvam para você.
Você:

1. Continua o seu ataque.
2. Foge dele.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1 :
        n = 199
    else :
        n = 232
    return [p, enc, ite, n]
    
h = h + [his80]

def his81(p, enc, ite):
    input('''O Macaco-Cachorro ri e diz a você que Kylltrog é um preguiçoso que não serve para nada, e que
não vale a pena salvá-lo. Você solta um suspiro de alívio quando ele caminha de volta e grita para
chamar o porteiro. Alguns momentos depois, o porteiro aparece e abre uma pequena porta para
deixar você entrar. ''')
    n = 251
    return [p, enc, ite, n]
    
h = h + [his81]

def his82(p, enc, ite):
    input('''Você cai no fosso. Freneticamente, você tenta agarrar a borda ao cair, mas sem êxito. Você
despenca pelo poço de ponta cabeça, e sua última lembrança é sua queda final ao chocar-se contra o
solo lá embaixo, o que mata você instantaneamente. Você falhou na sua missão. ''')
    p[2] = 0
    n = 1
    return [p, enc, ite, n]
    
h = h + [his82]

def his83(p, enc, ite):
    input('''O homem é um comerciante. Você diz a ele que vocês são companheiros de profissão, e vocês
conversam por algum tempo sobre preços e lucros dentro da Torre Negra. Ele diz que nunca
permitiram que ele entrasse nos andares acima do térreo da Cidadela, uma vez que os comerciantes
são bastante desprezados lá dentro. Você se despede e segue adiante. ''')
    n = 245
    return [p, enc, ite, n]
    
h = h + [his83]

def his84(p, enc, ite):
    input('''Ao examinar as prateleiras, você ouve uma grande movimentação atrás de você. Você se vira
rapidamente, a tempo de ver criaturas semelhantes a Orcas, armadas e em guarda, materializaram-se
uma após a outra diante de você. Elas avançam e cercam você. O mais alto chega o rosto perto do
seu e solta um bafo de respiração diretamente sobre os seus olhos. O aposento gira e você desaba no
chão, inconsciente. ''')
    n = 234
    return [p, enc, ite, n]
    
h = h + [his84]

def his85(p, enc, ite):
    input('''Você lança seu Feitiço e espera que a bola de fogo apareça na ponta da sua tocha. A tocha se
acende, apenas o suficiente para que você veja que há uma porta do outro lado do aposento, mas
depois se apaga de novo. Os Ganjees riem mais uma vez dos seus esforços para enganá-los. Você
sente uma pancada na cabeça que volta a derrubá-lo no chão. Você perde dois pontos de ENERGIA. ''')
    p[2] = p[2] - 2
    if p[2] < 0 :
        input('Você não tinha energia suficiente para aguentar a pancada. Sua misão acaba por aqui.\n')
        n = 1
    else :
        n = input('''Você:

1. Tentará um Encanto da Ilusão?            (Possui {})
2. Pegará alguma coisa na sua mochila?
3. Desembainhará a sua espada?

Digite sua opção: '''.format(enc[4]))
        n = numcerto(n, 1, 3)
        if n == 1 and enc[4] < 1 :
            n = input('Não possui Encantos de Ilusão, digite outra opção: ')
            n = numcerto(n, 2, 3)
        if n == 1 :
            enc[4] = enc[4] - 1
            n = 395
        elif n == 2 :
            n = 322
        else :
            n = 248
    return [p, enc, ite, n]
    
h = h + [his85]

def his86(p, enc, ite):
    input('''Quando você lança o encanto, as duas criaturas ficam olhando espantadas enquanto você flutua no
ar, passa sobre suas cabeças na direção do portão, sobre a muralha e para o interior da Cidadela.
Você aterrissa do lado de dentro e olha à sua volta. Mas tome cuidado! Eles com certeza avisarão
os guardas da Cidadela.''')
    n = 251
    return [p, enc, ite, n]
    
h = h + [his86]

def his87(p, enc, ite):
    input('''Você cria uma grande bola de fogo nas suas mãos e a lança sobre a criatura. Não adianta nada. O
Gárgula dá um soco em você, e o golpe joga você no chão.''')
    p[2] = p[2] - 2
    if p[2] > 0 :
        input('É melhor evitar esta fera, sair do aposento e tentar a porta do meio da sacada. ')
        n = 64
    else :
        input('Você não consegue se levantar mais do chão. Sua história acaba aqui.\n')
        n = 1
    return [p, enc, ite, n]
    
h = h + [his87]

def his88(p, enc, ite):
    n = input('''A porta é extremamente forte, mas cede mo pouco quando você a golpeia. Você pode tentar golpeá-
la tanto tempo quanto quiser, até que ela ceda de todo. Jogue um dado para cada tentativa. Se
obtiver um seis, você consegue. Para cada tentativa sem êxito, você perderá um ponto
de ENERGIA.

1. Jogar um dado.
2. Usar o Encanto da Força (Possui {}).
3. Tentar a porta do meio.
4. Tentar a porta na outra extremidade da sacada.

Digite sua opção: '''.format(enc[10]))
    n = numcerto(n, 1, 4)
    while (n == 1 and p[2] > 0) or (n == 2 and enc[10] == 0) :
        if n == 1 :
            d = rodar(1)
            if d == 6 :
                input('Você conseguiu.')
                n = 292
            else :
                p[2] = p[2] - 1
                if p[2] > 0 :
                    n = input('Sua ENERGIA é {}\n\nDigite novamente: '.format(p[2]))
                    n = numcerto(n, 1, 4)
                    limpa()
                    estado(p)
                    print('''
A porta é extremamente forte, mas cede mo pouco quando você a golpeia. Você pode tentar golpeá-
la tanto tempo quanto quiser, até que ela ceda de todo. Jogue um dado para cada tentativa. Se
obtiver um seis, você consegue. Para cada tentativa sem êxito, você perderá um ponto
de ENERGIA.

1. Jogar um dado.
2. Usar o Encanto da Força (Possui {}).
3. Tentar a porta do meio.
4. Tentar a porta na outra extremidade da sacada.
'''.format(enc[10]))
                else :
                    input('Sua Energia acabou. Falhou na sua misão.')
                    n = 1
        else :
            n = input('Não possui encantos de Força, Digite outra opção: ')
            n = numcerto(n, 1, 4)
    if n == 2 :
        enc[10] = enc[10] - 1
        n = 170
    elif n == 3 :
        n = 64
    elif n == 4 :
        n = 304
    return [p, enc, ite, n]
    
h = h + [his88]

def his89(p, enc, ite):
    input('''A chave gira, a fechadura se abre e você olha dentro da caixa. Lá dentro há um vidro grande que
contém uma aranha. Mas não é uma aranha comum; esta criatura tem o rosto de um velho. Ele está
falando com você, mas você não consegue entender o que ele está dizendo. Um barulho chama a
sua atenção, você se vira e vê que a porta por onde você entrou está começando a abrir. Você põe o
vidro na sua mochila e parte para a outra porta. ''')
    ite[1][1] = ite[1][1] + 1
    n = 237
    return [p, enc, ite, n]
    
h = h + [his89]

def his90(p, enc, ite):
    n = input('''A passagem se alarga, e você está agora andando ao longo de um rio que corre. Bem à frente, há
uma mulher que parece estar lavando roupa. Ela tem uma cesta com roupas a seu lado, e há vários
conjuntos de ceroula e camiseta de baixo pendurados em um varal atrás dela. Você:

1. Desembainhará a sua espada e avançará, pronto para a luta.
2. Cumprimentará ela e tentará estabelecer uma conversação.
3. Usará um Encanto de Percepção Extra-Sensorial para descobrir quem ela é.

Digite sua opção: ''')
    n = numcerto(n, 1, 3)
    if n == 1 :
        n = 176
    elif n == 2 :
        n = 21
    else :
        n = 329
    return [p, enc, ite, n]
    
h = h + [his90]

def his91(p, enc, ite):
    print('''Ela olha para a sua oferta e seus olhos se arregalam. "Deixe-me ver isso, ela ordena. Você avança
cuidadosamente na direção dela e mostra a escova. Ela pega o objeto e passa vários minutos
admirando-o. - "Isto é de fato uma obra de arte", ela diz, e se levanta da cama para experimentá-la
em frente ao espelho. Ao escovar os cabelos dela, eles assumem um brilho incomum, cintilando
suavemente. Ela fica fascinada com seu presente, e esta é a sua chance de sair sem ser notado pela
porta existente no canto mais distante. Você pode tentar levar com você um Velo de Ouro que se
encontra sobre a cama. Teste a sua Sorte. Se tiver sorte, consegue apanhá-lo rapidamente e pode
sair pela outra porta. Se não tiver sorte, você pode Testar a sua Sorte de novo até que
finalmente tenha sorte. Ou, se a sorte não estiver do seu lado, poderá ignorar o objeto que atrapalha
você e sair de qualquer modo.''')
    sn = 'S'
    while p[3] > 1 and sn in ['S', 'SIM'] :
        sn = str(input('\nTestar sorte [s/n] '))
        sn = sino(sn)
        if sn in ['S', 'SIM']:
            so = sorte(p)
            p[3] = p[3] - 1
            if so:
                ite[4][1] = ite[4][1] + 1
                sn = 'N'
                input('Conseguiu apanhar o Velo de Ouro. ')
            elif p[3] < 2 :
                sn = 'N'
                input('Acabou sua sorte. ')
        else :
            input('Conseguiu sair do aposento.')
    n = 140
    return [p, enc, ite, n]
    
h = h + [his91]

def his92(p, enc, ite):
    input('''O líquido leitoso cheira bem. Você toma um gole e começa a sorrir. Dá um gole maior e explode
em gargalhadas - por motivo nenhum! Não é de se estranhar que os pequenos Grernlins estivessem
gostando tanto. Com a cabeça leve e de bom humor, você sai do aposento para continuar em seu
caminho para a Cidadela. 2 pontos de ENERGIA foram acresentados por este incidente reconfortante. ''')
    p[2] = p[2] + 2
    n = 156
    return [p, enc, ite, n]
    
h = h + [his92]

def his93(p, enc, ite):
    input('''Do lado de fora, você olha para sua garrafa. É uma garrafa de Essência de Erva de Porco,
aparentemente útil para repelir criaturas de base em pedra. Isso pode ser útil, e você a guarda
cuidadosamente em sua mochila. Seguindo em frente pelo corredor, você chega a uma outra porta,
que abre, deixando que você passe para um grande aposento. ''')
    ite[9][1] = ite[9][1] + 1
    n = 169
    return [p, enc, ite, n]
    
h = h + [his93]

def his94(p, enc, ite):
    print('''Você sente o seu próprio poder crescendo. Você corre na direção da porta e a golpeia firme como
ombro... mas ela nem se mexe! Você perde um ponto de ENERGIA pela contusão''', end= '' )
    p[2] = p[2] - 1
    if p[2] < 1 :
        n = 1
        input('. Você perde seu\núltimo ponto de energia.')
    else :
        input(' e bate com força\npára chamar o guarda.')
        n = 118
    return [p, enc, ite, n]
    
h = h + [his94]

def his95(p, enc, ite):
    input('''No lado mais distante da Adega de Vinhos, há uma porta de madeira, que você experimenta. Ela
abre para uma passagem que conduz adiante por vários metros. ''')
    n = 367
    return [p, enc, ite, n]
    
h = h + [his95]

def his96(p, enc, ite):
    input('''Eles aceitam a sua oferta e convocam o porteiro, que abre uma pequena porta dentro da porta
levadiça para deixar você entrar. Você os deixa discutindo por causa da pepita de ouro.''')
    n = 251
    return [p, enc, ite, n]
    
h = h + [his96]

def his97(p, enc, ite):
    print('''O pão está bastante seco e sem gosto. Na verdade, está muito seco - tão seco que logo você está
desesperado por alguma coisa para beber! Sua boca está ressequida e você procura freneticamente
entre os alimentos do aposento algum líquido. Mas não há nada para aplacar a sua sede. Você tem
que deduzir um ponto de HABILIDADE de seu índice atual.''')
    p[1] = p[1] - 1
    n = input('''Você pode agora sair do aposento

1. Pela porta da parede do lado esquerdo.
2. Pela porta oposta à que você usou para entrar.

Digite sua opção: ''')
    n = numcerto(n, 1, 2)
    if n == 1 :
        n = 13
    else :
        n = 281
    return [p, enc, ite, n]
    
h = h + [his97]

def his98(p, enc, ite):
    n = 98
    return [p, enc, ite, n]
    
h = h + [his98]

def his99(p, enc, ite):
    n = 99
    return [p, enc, ite, n]
    
h = h + [his99]

def his100(p, enc, ite):
    n = 100
    return [p, enc, ite, n]
    
h = h + [his100]

def his101(p, enc, ite):
    n = 101
    return [p, enc, ite, n]
    
h = h + [his101]

def his102(p, enc, ite):
    n = 102
    return [p, enc, ite, n]
    
h = h + [his102]

def his103(p, enc, ite):
    n = 103
    return [p, enc, ite, n]
    
h = h + [his103]

def his104(p, enc, ite):
    n = 104
    return [p, enc, ite, n]
    
h = h + [his104]

def his105(p, enc, ite):
    n = 105
    return [p, enc, ite, n]
    
h = h + [his105]

def his106(p, enc, ite):
    n = 106
    return [p, enc, ite, n]
    
h = h + [his106]

def his107(p, enc, ite):
    n = 107
    return [p, enc, ite, n]
    
h = h + [his107]

def his108(p, enc, ite):
    n = 108
    return [p, enc, ite, n]
    
h = h + [his108]

def his109(p, enc, ite):
    n = 109
    return [p, enc, ite, n]
    
h = h + [his109]

def his110(p, enc, ite):
    n = 110
    return [p, enc, ite, n]
    
h = h + [his110]

def his111(p, enc, ite):
    n = 111
    return [p, enc, ite, n]
    
h = h + [his111]

def his112(p, enc, ite):
    n = 112
    return [p, enc, ite, n]
    
h = h + [his112]

def his113(p, enc, ite):
    n = 113
    return [p, enc, ite, n]
    
h = h + [his113]

def his114(p, enc, ite):
    n = 114
    return [p, enc, ite, n]
    
h = h + [his114]

def his115(p, enc, ite):
    n = 115
    return [p, enc, ite, n]
    
h = h + [his115]

def his116(p, enc, ite):
    n = 116
    return [p, enc, ite, n]
    
h = h + [his116]

def his117(p, enc, ite):
    n = 117
    return [p, enc, ite, n]
    
h = h + [his117]

def his118(p, enc, ite):
    n = 118
    return [p, enc, ite, n]
    
h = h + [his118]

def his119(p, enc, ite):
    n = 119
    return [p, enc, ite, n]
    
h = h + [his119]

def his120(p, enc, ite):
    n = 120
    return [p, enc, ite, n]
    
h = h + [his120]

def his121(p, enc, ite):
    n = 121
    return [p, enc, ite, n]
    
h = h + [his121]

def his122(p, enc, ite):
    n = 122
    return [p, enc, ite, n]
    
h = h + [his122]

def his123(p, enc, ite):
    n = 123
    return [p, enc, ite, n]
    
h = h + [his123]

def his124(p, enc, ite):
    n = 124
    return [p, enc, ite, n]
    
h = h + [his124]

def his125(p, enc, ite):
    n = 125
    return [p, enc, ite, n]
    
h = h + [his125]

def his126(p, enc, ite):
    n = 126
    return [p, enc, ite, n]
    
h = h + [his126]

def his127(p, enc, ite):
    n = 127
    return [p, enc, ite, n]
    
h = h + [his127]

def his128(p, enc, ite):
    n = 128
    return [p, enc, ite, n]
    
h = h + [his128]

def his129(p, enc, ite):
    n = 129
    return [p, enc, ite, n]
    
h = h + [his129]

def his130(p, enc, ite):
    n = 130
    return [p, enc, ite, n]
    
h = h + [his130]

def his131(p, enc, ite):
    n = 131
    return [p, enc, ite, n]
    
h = h + [his131]

def his132(p, enc, ite):
    n = 132
    return [p, enc, ite, n]
    
h = h + [his132]

def his133(p, enc, ite):
    n = 133
    return [p, enc, ite, n]
    
h = h + [his133]

def his134(p, enc, ite):
    n = 134
    return [p, enc, ite, n]
    
h = h + [his134]

def his135(p, enc, ite):
    n = 135
    return [p, enc, ite, n]
    
h = h + [his135]

def his136(p, enc, ite):
    n = 136
    return [p, enc, ite, n]
    
h = h + [his136]

def his137(p, enc, ite):
    n = 137
    return [p, enc, ite, n]
    
h = h + [his137]

def his138(p, enc, ite):
    n = 138
    return [p, enc, ite, n]
    
h = h + [his138]

def his139(p, enc, ite):
    n = 139
    return [p, enc, ite, n]
    
h = h + [his139]

def his140(p, enc, ite):
    n = 140
    return [p, enc, ite, n]
    
h = h + [his140]

def his141(p, enc, ite):
    n = 141
    return [p, enc, ite, n]
    
h = h + [his141]

def his142(p, enc, ite):
    n = 142
    return [p, enc, ite, n]
    
h = h + [his142]

def his143(p, enc, ite):
    n = 143
    return [p, enc, ite, n]
    
h = h + [his143]

def his144(p, enc, ite):
    n = 144
    return [p, enc, ite, n]
    
h = h + [his144]

def his145(p, enc, ite):
    n = 145
    return [p, enc, ite, n]
    
h = h + [his145]

def his146(p, enc, ite):
    n = 146
    return [p, enc, ite, n]
    
h = h + [his146]

def his147(p, enc, ite):
    n = 147
    return [p, enc, ite, n]
    
h = h + [his147]

def his148(p, enc, ite):
    n = 148
    return [p, enc, ite, n]
    
h = h + [his148]

def his149(p, enc, ite):
    n = 149
    return [p, enc, ite, n]
    
h = h + [his149]

def his150(p, enc, ite):
    n = 150
    return [p, enc, ite, n]
    
h = h + [his150]

def his151(p, enc, ite):
    n = 151
    return [p, enc, ite, n]
    
h = h + [his151]

def his152(p, enc, ite):
    n = 152
    return [p, enc, ite, n]
    
h = h + [his152]

def his153(p, enc, ite):
    n = 153
    return [p, enc, ite, n]
    
h = h + [his153]

def his154(p, enc, ite):
    n = 154
    return [p, enc, ite, n]
    
h = h + [his154]

def his155(p, enc, ite):
    n = 155
    return [p, enc, ite, n]
    
h = h + [his155]

def his156(p, enc, ite):
    n = 156
    return [p, enc, ite, n]
    
h = h + [his156]

def his157(p, enc, ite):
    n = 157
    return [p, enc, ite, n]
    
h = h + [his157]

def his158(p, enc, ite):
    n = 158
    return [p, enc, ite, n]
    
h = h + [his158]

def his159(p, enc, ite):
    n = 159
    return [p, enc, ite, n]
    
h = h + [his159]

def his160(p, enc, ite):
    n = 160
    return [p, enc, ite, n]
    
h = h + [his160]

def his161(p, enc, ite):
    n = 161
    return [p, enc, ite, n]
    
h = h + [his161]

def his162(p, enc, ite):
    n = 162
    return [p, enc, ite, n]
    
h = h + [his162]

def his163(p, enc, ite):
    n = 163
    return [p, enc, ite, n]
    
h = h + [his163]

def his164(p, enc, ite):
    n = 164
    return [p, enc, ite, n]
    
h = h + [his164]

def his165(p, enc, ite):
    n = 165
    return [p, enc, ite, n]
    
h = h + [his165]

def his166(p, enc, ite):
    n = 166
    return [p, enc, ite, n]
    
h = h + [his166]

def his167(p, enc, ite):
    n = 167
    return [p, enc, ite, n]
    
h = h + [his167]

def his168(p, enc, ite):
    n = 168
    return [p, enc, ite, n]
    
h = h + [his168]

def his169(p, enc, ite):
    n = 169
    return [p, enc, ite, n]
    
h = h + [his169]

def his170(p, enc, ite):
    n = 170
    return [p, enc, ite, n]
    
h = h + [his170]

def his171(p, enc, ite):
    n = 171
    return [p, enc, ite, n]
    
h = h + [his171]

def his172(p, enc, ite):
    n = 172
    return [p, enc, ite, n]
    
h = h + [his172]

def his173(p, enc, ite):
    n = 173
    return [p, enc, ite, n]
    
h = h + [his173]

def his174(p, enc, ite):
    n = 174
    return [p, enc, ite, n]
    
h = h + [his174]

def his175(p, enc, ite):
    n = 175
    return [p, enc, ite, n]
    
h = h + [his175]

def his176(p, enc, ite):
    n = 176
    return [p, enc, ite, n]
    
h = h + [his176]

def his177(p, enc, ite):
    n = 177
    return [p, enc, ite, n]
    
h = h + [his177]

def his178(p, enc, ite):
    n = 178
    return [p, enc, ite, n]
    
h = h + [his178]

def his179(p, enc, ite):
    n = 179
    return [p, enc, ite, n]
    
h = h + [his179]

def his180(p, enc, ite):
    n = 180
    return [p, enc, ite, n]
    
h = h + [his180]

def his181(p, enc, ite):
    n = 181
    return [p, enc, ite, n]
    
h = h + [his181]

def his182(p, enc, ite):
    n = 182
    return [p, enc, ite, n]
    
h = h + [his182]

def his183(p, enc, ite):
    n = 183
    return [p, enc, ite, n]
    
h = h + [his183]

def his184(p, enc, ite):
    n = 184
    return [p, enc, ite, n]
    
h = h + [his184]

def his185(p, enc, ite):
    n = 185
    return [p, enc, ite, n]
    
h = h + [his185]

def his186(p, enc, ite):
    n = 186
    return [p, enc, ite, n]
    
h = h + [his186]

def his187(p, enc, ite):
    n = 187
    return [p, enc, ite, n]
    
h = h + [his187]

def his188(p, enc, ite):
    n = 188
    return [p, enc, ite, n]
    
h = h + [his188]

def his189(p, enc, ite):
    n = 189
    return [p, enc, ite, n]
    
h = h + [his189]

def his190(p, enc, ite):
    n = 190
    return [p, enc, ite, n]
    
h = h + [his190]

def his191(p, enc, ite):
    n = 191
    return [p, enc, ite, n]
    
h = h + [his191]

def his192(p, enc, ite):
    n = 192
    return [p, enc, ite, n]
    
h = h + [his192]

def his193(p, enc, ite):
    n = 193
    return [p, enc, ite, n]
    
h = h + [his193]

def his194(p, enc, ite):
    n = 194
    return [p, enc, ite, n]
    
h = h + [his194]

def his195(p, enc, ite):
    n = 195
    return [p, enc, ite, n]
    
h = h + [his195]

def his196(p, enc, ite):
    n = 196
    return [p, enc, ite, n]
    
h = h + [his196]

def his197(p, enc, ite):
    n = 197
    return [p, enc, ite, n]
    
h = h + [his197]

def his198(p, enc, ite):
    n = 198
    return [p, enc, ite, n]
    
h = h + [his198]

def his199(p, enc, ite):
    n = 199
    return [p, enc, ite, n]
    
h = h + [his199]

def his200(p, enc, ite):
    n = 200
    return [p, enc, ite, n]
    
h = h + [his200]

def his201(p, enc, ite):
    n = 201
    return [p, enc, ite, n]
    
h = h + [his201]

def his202(p, enc, ite):
    n = 202
    return [p, enc, ite, n]
    
h = h + [his202]

def his203(p, enc, ite):
    n = 203
    return [p, enc, ite, n]
    
h = h + [his203]

def his204(p, enc, ite):
    n = 204
    return [p, enc, ite, n]
    
h = h + [his204]

def his205(p, enc, ite):
    n = 205
    return [p, enc, ite, n]
    
h = h + [his205]

def his206(p, enc, ite):
    n = 206
    return [p, enc, ite, n]
    
h = h + [his206]

def his207(p, enc, ite):
    n = 207
    return [p, enc, ite, n]
    
h = h + [his207]

def his208(p, enc, ite):
    n = 208
    return [p, enc, ite, n]
    
h = h + [his208]

def his209(p, enc, ite):
    n = 209
    return [p, enc, ite, n]
    
h = h + [his209]

def his210(p, enc, ite):
    n = 210
    return [p, enc, ite, n]
    
h = h + [his210]

def his211(p, enc, ite):
    n = 211
    return [p, enc, ite, n]
    
h = h + [his211]

def his212(p, enc, ite):
    n = 212
    return [p, enc, ite, n]
    
h = h + [his212]

def his213(p, enc, ite):
    n = 213
    return [p, enc, ite, n]
    
h = h + [his213]

def his214(p, enc, ite):
    n = 214
    return [p, enc, ite, n]
    
h = h + [his214]

def his215(p, enc, ite):
    n = 215
    return [p, enc, ite, n]
    
h = h + [his215]

def his216(p, enc, ite):
    n = 216
    return [p, enc, ite, n]
    
h = h + [his216]

def his217(p, enc, ite):
    n = 217
    return [p, enc, ite, n]
    
h = h + [his217]

def his218(p, enc, ite):
    n = 218
    return [p, enc, ite, n]
    
h = h + [his218]

def his219(p, enc, ite):
    n = 219
    return [p, enc, ite, n]
    
h = h + [his219]

def his220(p, enc, ite):
    n = 220
    return [p, enc, ite, n]
    
h = h + [his220]

def his221(p, enc, ite):
    n = 221
    return [p, enc, ite, n]
    
h = h + [his221]

def his222(p, enc, ite):
    n = 222
    return [p, enc, ite, n]
    
h = h + [his222]

def his223(p, enc, ite):
    n = 223
    return [p, enc, ite, n]
    
h = h + [his223]

def his224(p, enc, ite):
    n = 224
    return [p, enc, ite, n]
    
h = h + [his224]

def his225(p, enc, ite):
    n = 225
    return [p, enc, ite, n]
    
h = h + [his225]

def his226(p, enc, ite):
    n = 226
    return [p, enc, ite, n]
    
h = h + [his226]

def his227(p, enc, ite):
    n = 227
    return [p, enc, ite, n]
    
h = h + [his227]

def his228(p, enc, ite):
    n = 228
    return [p, enc, ite, n]
    
h = h + [his228]

def his229(p, enc, ite):
    n = 229
    return [p, enc, ite, n]
    
h = h + [his229]

def his230(p, enc, ite):
    n = 230
    return [p, enc, ite, n]
    
h = h + [his230]

def his231(p, enc, ite):
    n = 231
    return [p, enc, ite, n]
    
h = h + [his231]

def his232(p, enc, ite):
    n = 232
    return [p, enc, ite, n]
    
h = h + [his232]

def his233(p, enc, ite):
    n = 233
    return [p, enc, ite, n]
    
h = h + [his233]

def his234(p, enc, ite):
    n = 234
    return [p, enc, ite, n]
    
h = h + [his234]

def his235(p, enc, ite):
    n = 235
    return [p, enc, ite, n]
    
h = h + [his235]

def his236(p, enc, ite):
    n = 236
    return [p, enc, ite, n]
    
h = h + [his236]

def his237(p, enc, ite):
    n = 237
    return [p, enc, ite, n]
    
h = h + [his237]

def his238(p, enc, ite):
    n = 238
    return [p, enc, ite, n]
    
h = h + [his238]

def his239(p, enc, ite):
    n = 239
    return [p, enc, ite, n]
    
h = h + [his239]

def his240(p, enc, ite):
    n = 240
    return [p, enc, ite, n]
    
h = h + [his240]

def his241(p, enc, ite):
    n = 241
    return [p, enc, ite, n]
    
h = h + [his241]

def his242(p, enc, ite):
    n = 242
    return [p, enc, ite, n]
    
h = h + [his242]

def his243(p, enc, ite):
    n = 243
    return [p, enc, ite, n]
    
h = h + [his243]

def his244(p, enc, ite):
    n = 244
    return [p, enc, ite, n]
    
h = h + [his244]

def his245(p, enc, ite):
    n = 245
    return [p, enc, ite, n]
    
h = h + [his245]

def his246(p, enc, ite):
    n = 246
    return [p, enc, ite, n]
    
h = h + [his246]

def his247(p, enc, ite):
    n = 247
    return [p, enc, ite, n]
    
h = h + [his247]

def his248(p, enc, ite):
    n = 248
    return [p, enc, ite, n]
    
h = h + [his248]

def his249(p, enc, ite):
    n = 249
    return [p, enc, ite, n]
    
h = h + [his249]

def his250(p, enc, ite):
    n = 250
    return [p, enc, ite, n]
    
h = h + [his250]

def his251(p, enc, ite):
    n = 251
    return [p, enc, ite, n]
    
h = h + [his251]

def his252(p, enc, ite):
    n = 252
    return [p, enc, ite, n]
    
h = h + [his252]

def his253(p, enc, ite):
    n = 253
    return [p, enc, ite, n]
    
h = h + [his253]

def his254(p, enc, ite):
    n = 254
    return [p, enc, ite, n]
    
h = h + [his254]

def his255(p, enc, ite):
    n = 255
    return [p, enc, ite, n]
    
h = h + [his255]

def his256(p, enc, ite):
    n = 256
    return [p, enc, ite, n]
    
h = h + [his256]

def his257(p, enc, ite):
    n = 257
    return [p, enc, ite, n]
    
h = h + [his257]

def his258(p, enc, ite):
    n = 258
    return [p, enc, ite, n]
    
h = h + [his258]

def his259(p, enc, ite):
    n = 259
    return [p, enc, ite, n]
    
h = h + [his259]

def his260(p, enc, ite):
    n = 260
    return [p, enc, ite, n]
    
h = h + [his260]

def his261(p, enc, ite):
    n = 261
    return [p, enc, ite, n]
    
h = h + [his261]

def his262(p, enc, ite):
    n = 262
    return [p, enc, ite, n]
    
h = h + [his262]

def his263(p, enc, ite):
    n = 263
    return [p, enc, ite, n]
    
h = h + [his263]

def his264(p, enc, ite):
    n = 264
    return [p, enc, ite, n]
    
h = h + [his264]

def his265(p, enc, ite):
    n = 265
    return [p, enc, ite, n]
    
h = h + [his265]

def his266(p, enc, ite):
    n = 266
    return [p, enc, ite, n]
    
h = h + [his266]

def his267(p, enc, ite):
    n = 267
    return [p, enc, ite, n]
    
h = h + [his267]

def his268(p, enc, ite):
    n = 268
    return [p, enc, ite, n]
    
h = h + [his268]

def his269(p, enc, ite):
    n = 269
    return [p, enc, ite, n]
    
h = h + [his269]

def his270(p, enc, ite):
    n = 270
    return [p, enc, ite, n]
    
h = h + [his270]

def his271(p, enc, ite):
    n = 271
    return [p, enc, ite, n]
    
h = h + [his271]

def his272(p, enc, ite):
    n = 272
    return [p, enc, ite, n]
    
h = h + [his272]

def his273(p, enc, ite):
    n = 273
    return [p, enc, ite, n]
    
h = h + [his273]

def his274(p, enc, ite):
    n = 274
    return [p, enc, ite, n]
    
h = h + [his274]

def his275(p, enc, ite):
    n = 275
    return [p, enc, ite, n]
    
h = h + [his275]

def his276(p, enc, ite):
    n = 276
    return [p, enc, ite, n]
    
h = h + [his276]

def his277(p, enc, ite):
    n = 277
    return [p, enc, ite, n]
    
h = h + [his277]

def his278(p, enc, ite):
    n = 278
    return [p, enc, ite, n]
    
h = h + [his278]

def his279(p, enc, ite):
    n = 279
    return [p, enc, ite, n]
    
h = h + [his279]

def his280(p, enc, ite):
    n = 280
    return [p, enc, ite, n]
    
h = h + [his280]

def his281(p, enc, ite):
    n = 281
    return [p, enc, ite, n]
    
h = h + [his281]

def his282(p, enc, ite):
    n = 282
    return [p, enc, ite, n]
    
h = h + [his282]

def his283(p, enc, ite):
    n = 283
    return [p, enc, ite, n]
    
h = h + [his283]

def his284(p, enc, ite):
    n = 284
    return [p, enc, ite, n]
    
h = h + [his284]

def his285(p, enc, ite):
    n = 285
    return [p, enc, ite, n]
    
h = h + [his285]

def his286(p, enc, ite):
    n = 286
    return [p, enc, ite, n]
    
h = h + [his286]

def his287(p, enc, ite):
    n = 287
    return [p, enc, ite, n]
    
h = h + [his287]

def his288(p, enc, ite):
    n = 288
    return [p, enc, ite, n]
    
h = h + [his288]

def his289(p, enc, ite):
    n = 289
    return [p, enc, ite, n]
    
h = h + [his289]

def his290(p, enc, ite):
    n = 290
    return [p, enc, ite, n]
    
h = h + [his290]

def his291(p, enc, ite):
    n = 291
    return [p, enc, ite, n]
    
h = h + [his291]

def his292(p, enc, ite):
    n = 292
    return [p, enc, ite, n]
    
h = h + [his292]

def his293(p, enc, ite):
    n = 293
    return [p, enc, ite, n]
    
h = h + [his293]

def his294(p, enc, ite):
    n = 294
    return [p, enc, ite, n]
    
h = h + [his294]

def his295(p, enc, ite):
    n = 295
    return [p, enc, ite, n]
    
h = h + [his295]

def his296(p, enc, ite):
    n = 296
    return [p, enc, ite, n]
    
h = h + [his296]

def his297(p, enc, ite):
    n = 297
    return [p, enc, ite, n]
    
h = h + [his297]

def his298(p, enc, ite):
    n = 298
    return [p, enc, ite, n]
    
h = h + [his298]

def his299(p, enc, ite):
    n = 299
    return [p, enc, ite, n]
    
h = h + [his299]

def his300(p, enc, ite):
    n = 300
    return [p, enc, ite, n]
    
h = h + [his300]

def his301(p, enc, ite):
    n = 301
    return [p, enc, ite, n]
    
h = h + [his301]

def his302(p, enc, ite):
    n = 302
    return [p, enc, ite, n]
    
h = h + [his302]

def his303(p, enc, ite):
    n = 303
    return [p, enc, ite, n]
    
h = h + [his303]

def his304(p, enc, ite):
    n = 304
    return [p, enc, ite, n]
    
h = h + [his304]

def his305(p, enc, ite):
    n = 305
    return [p, enc, ite, n]
    
h = h + [his305]

def his306(p, enc, ite):
    n = 306
    return [p, enc, ite, n]
    
h = h + [his306]

def his307(p, enc, ite):
    n = 307
    return [p, enc, ite, n]
    
h = h + [his307]

def his308(p, enc, ite):
    n = 308
    return [p, enc, ite, n]
    
h = h + [his308]

def his309(p, enc, ite):
    n = 309
    return [p, enc, ite, n]
    
h = h + [his309]

def his310(p, enc, ite):
    n = 310
    return [p, enc, ite, n]
    
h = h + [his310]

def his311(p, enc, ite):
    n = 311
    return [p, enc, ite, n]
    
h = h + [his311]

def his312(p, enc, ite):
    n = 312
    return [p, enc, ite, n]
    
h = h + [his312]

def his313(p, enc, ite):
    n = 313
    return [p, enc, ite, n]
    
h = h + [his313]

def his314(p, enc, ite):
    n = 314
    return [p, enc, ite, n]
    
h = h + [his314]

def his315(p, enc, ite):
    n = 315
    return [p, enc, ite, n]
    
h = h + [his315]

def his316(p, enc, ite):
    n = 316
    return [p, enc, ite, n]
    
h = h + [his316]

def his317(p, enc, ite):
    n = 317
    return [p, enc, ite, n]
    
h = h + [his317]

def his318(p, enc, ite):
    n = 318
    return [p, enc, ite, n]
    
h = h + [his318]

def his319(p, enc, ite):
    n = 319
    return [p, enc, ite, n]
    
h = h + [his319]

def his320(p, enc, ite):
    n = 320
    return [p, enc, ite, n]
    
h = h + [his320]

def his321(p, enc, ite):
    n = 321
    return [p, enc, ite, n]
    
h = h + [his321]

def his322(p, enc, ite):
    n = 322
    return [p, enc, ite, n]
    
h = h + [his322]

def his323(p, enc, ite):
    n = 323
    return [p, enc, ite, n]
    
h = h + [his323]

def his324(p, enc, ite):
    n = 324
    return [p, enc, ite, n]
    
h = h + [his324]

def his325(p, enc, ite):
    n = 325
    return [p, enc, ite, n]
    
h = h + [his325]

def his326(p, enc, ite):
    n = 326
    return [p, enc, ite, n]
    
h = h + [his326]

def his327(p, enc, ite):
    n = 327
    return [p, enc, ite, n]
    
h = h + [his327]

def his328(p, enc, ite):
    n = 328
    return [p, enc, ite, n]
    
h = h + [his328]

def his329(p, enc, ite):
    n = 329
    return [p, enc, ite, n]
    
h = h + [his329]

def his330(p, enc, ite):
    n = 330
    return [p, enc, ite, n]
    
h = h + [his330]

def his331(p, enc, ite):
    n = 331
    return [p, enc, ite, n]
    
h = h + [his331]

def his332(p, enc, ite):
    n = 332
    return [p, enc, ite, n]
    
h = h + [his332]

def his333(p, enc, ite):
    n = 333
    return [p, enc, ite, n]
    
h = h + [his333]

def his334(p, enc, ite):
    n = 334
    return [p, enc, ite, n]
    
h = h + [his334]

def his335(p, enc, ite):
    n = 335
    return [p, enc, ite, n]
    
h = h + [his335]

def his336(p, enc, ite):
    n = 336
    return [p, enc, ite, n]
    
h = h + [his336]

def his337(p, enc, ite):
    n = 337
    return [p, enc, ite, n]
    
h = h + [his337]

def his338(p, enc, ite):
    n = 338
    return [p, enc, ite, n]
    
h = h + [his338]

def his339(p, enc, ite):
    n = 339
    return [p, enc, ite, n]
    
h = h + [his339]

def his340(p, enc, ite):
    n = 340
    return [p, enc, ite, n]
    
h = h + [his340]

def his341(p, enc, ite):
    n = 341
    return [p, enc, ite, n]
    
h = h + [his341]

def his342(p, enc, ite):
    n = 342
    return [p, enc, ite, n]
    
h = h + [his342]

def his343(p, enc, ite):
    n = 343
    return [p, enc, ite, n]
    
h = h + [his343]

def his344(p, enc, ite):
    n = 344
    return [p, enc, ite, n]
    
h = h + [his344]

def his345(p, enc, ite):
    n = 345
    return [p, enc, ite, n]
    
h = h + [his345]

def his346(p, enc, ite):
    n = 346
    return [p, enc, ite, n]
    
h = h + [his346]

def his347(p, enc, ite):
    n = 347
    return [p, enc, ite, n]
    
h = h + [his347]

def his348(p, enc, ite):
    n = 348
    return [p, enc, ite, n]
    
h = h + [his348]

def his349(p, enc, ite):
    n = 349
    return [p, enc, ite, n]
    
h = h + [his349]

def his350(p, enc, ite):
    n = 350
    return [p, enc, ite, n]
    
h = h + [his350]

def his351(p, enc, ite):
    n = 351
    return [p, enc, ite, n]
    
h = h + [his351]

def his352(p, enc, ite):
    n = 352
    return [p, enc, ite, n]
    
h = h + [his352]

def his353(p, enc, ite):
    n = 353
    return [p, enc, ite, n]
    
h = h + [his353]

def his354(p, enc, ite):
    n = 354
    return [p, enc, ite, n]
    
h = h + [his354]

def his355(p, enc, ite):
    n = 355
    return [p, enc, ite, n]
    
h = h + [his355]

def his356(p, enc, ite):
    n = 356
    return [p, enc, ite, n]
    
h = h + [his356]

def his357(p, enc, ite):
    n = 357
    return [p, enc, ite, n]
    
h = h + [his357]

def his358(p, enc, ite):
    n = 358
    return [p, enc, ite, n]
    
h = h + [his358]

def his359(p, enc, ite):
    n = 359
    return [p, enc, ite, n]
    
h = h + [his359]

def his360(p, enc, ite):
    n = 360
    return [p, enc, ite, n]
    
h = h + [his360]

def his361(p, enc, ite):
    n = 361
    return [p, enc, ite, n]
    
h = h + [his361]

def his362(p, enc, ite):
    n = 362
    return [p, enc, ite, n]
    
h = h + [his362]

def his363(p, enc, ite):
    n = 363
    return [p, enc, ite, n]
    
h = h + [his363]

def his364(p, enc, ite):
    n = 364
    return [p, enc, ite, n]
    
h = h + [his364]

def his365(p, enc, ite):
    n = 365
    return [p, enc, ite, n]
    
h = h + [his365]

def his366(p, enc, ite):
    n = 366
    return [p, enc, ite, n]
    
h = h + [his366]

def his367(p, enc, ite):
    n = 367
    return [p, enc, ite, n]
    
h = h + [his367]

def his368(p, enc, ite):
    n = 368
    return [p, enc, ite, n]
    
h = h + [his368]

def his369(p, enc, ite):
    n = 369
    return [p, enc, ite, n]
    
h = h + [his369]

def his370(p, enc, ite):
    n = 370
    return [p, enc, ite, n]
    
h = h + [his370]

def his371(p, enc, ite):
    n = 371
    return [p, enc, ite, n]
    
h = h + [his371]

def his372(p, enc, ite):
    n = 372
    return [p, enc, ite, n]
    
h = h + [his372]

def his373(p, enc, ite):
    n = 373
    return [p, enc, ite, n]
    
h = h + [his373]

def his374(p, enc, ite):
    n = 374
    return [p, enc, ite, n]
    
h = h + [his374]

def his375(p, enc, ite):
    n = 375
    return [p, enc, ite, n]
    
h = h + [his375]

def his376(p, enc, ite):
    n = 376
    return [p, enc, ite, n]
    
h = h + [his376]

def his377(p, enc, ite):
    n = 377
    return [p, enc, ite, n]
    
h = h + [his377]

def his378(p, enc, ite):
    n = 378
    return [p, enc, ite, n]
    
h = h + [his378]

def his379(p, enc, ite):
    n = 379
    return [p, enc, ite, n]
    
h = h + [his379]

def his380(p, enc, ite):
    n = 380
    return [p, enc, ite, n]
    
h = h + [his380]

def his381(p, enc, ite):
    n = 381
    return [p, enc, ite, n]
    
h = h + [his381]

def his382(p, enc, ite):
    n = 382
    return [p, enc, ite, n]
    
h = h + [his382]

def his383(p, enc, ite):
    n = 383
    return [p, enc, ite, n]
    
h = h + [his383]

def his384(p, enc, ite):
    n = 384
    return [p, enc, ite, n]
    
h = h + [his384]

def his385(p, enc, ite):
    n = 385
    return [p, enc, ite, n]
    
h = h + [his385]

def his386(p, enc, ite):
    n = 386
    return [p, enc, ite, n]
    
h = h + [his386]

def his387(p, enc, ite):
    n = 387
    return [p, enc, ite, n]
    
h = h + [his387]

def his388(p, enc, ite):
    n = 388
    return [p, enc, ite, n]
    
h = h + [his388]

def his389(p, enc, ite):
    n = 389
    return [p, enc, ite, n]
    
h = h + [his389]

def his390(p, enc, ite):
    n = 390
    return [p, enc, ite, n]
    
h = h + [his390]

def his391(p, enc, ite):
    n = 391
    return [p, enc, ite, n]
    
h = h + [his391]

def his392(p, enc, ite):
    n = 392
    return [p, enc, ite, n]
    
h = h + [his392]

def his393(p, enc, ite):
    n = 393
    return [p, enc, ite, n]
    
h = h + [his393]

def his394(p, enc, ite):
    n = 394
    return [p, enc, ite, n]
    
h = h + [his394]

def his395(p, enc, ite):
    n = 395
    return [p, enc, ite, n]
    
h = h + [his395]

def his396(p, enc, ite):
    n = 396
    return [p, enc, ite, n]
    
h = h + [his396]

def his397(p, enc, ite):
    n = 397
    return [p, enc, ite, n]
    
h = h + [his397]

def his398(p, enc, ite):
    n = 398
    return [p, enc, ite, n]
    
h = h + [his398]

def his399(p, enc, ite):
    n = 399
    return [p, enc, ite, n]
    
h = h + [his399]

def his400(p, enc, ite):
    n = 400
    return [p, enc, ite, n]
    
h = h + [his400]

n = 1
while perso[2] > 0:
    limpa()
    estado(perso)

#    if ENCANTOS[8] + ENCANTOS[9] + ENCANTOS[6] > 0: # Encanto Habilidade, Energia ou Sorte
#        sn = 'S'
#        while sn in ['S', 'SIM']:
#            sn = input('\nDesejar usar um encantamento agora? [s/n] ')
#            sn = sino(sn)
#            if sn in ['S', 'SIM']:
#                n = input('1. Encantos de habilidade = {}\n2. Encantos de energia = {}\n3. Encantos de sorte = {}\n4. Não usar encantoa\n\nDigite sua opção: '.format(ENCANTOS[8], ENCANTOS[9], ENCANTOS[6]))
#                n = numcerto(n,1,4)
#                enc = [ENCANTOS[8], ENCANTOS[9], ENCANTOS[6], 1]
#                while enc[n - 1] == 0:
#                    n = input('Você não posue esse encantamento, por favor escolha de novo: ')
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
    n = input('A cual capitulo vamos? ')
    n = numcerto(n,1,400)


    limpa()
    estado(perso)
    print('')
    [perso, ENCANTOS, ITEM, n] = h[n-1](perso,ENCANTOS,ITEM)
    if perso[2] < 1:
        sn = str(input('Quer jogar novamente? [s/n] '))
        sn = sino(sn)
        if sn == 'S' or sn == 'SIM':
            pers0 = criarpersonagem()
            perso = pers0.copy()
            ENCANTOS = criarmagia()
            ITEM = ITEM0
            n = 1
        else:
            break

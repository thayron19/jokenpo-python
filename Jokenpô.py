import tkinter
import random
import keyboard


# ---------------------------------------------------------------------------------------------------------------------
def escolha(ppt):

    if ppt == 1:
        var_escolha.set('Você escolheu pedra!        💎')
        resultado(1)
    elif ppt == 2:
        var_escolha.set('Você escolheu papel!        🧻')
        resultado(2)
    elif ppt == 3:
        var_escolha.set('Você escolheu tesoura!      ✀')
        resultado(3)


# ---------------------------------------------------------------------------------------------------------------------
def resultado(escolheu):

    acumulador = ''

    maquina = random.randint(1, 3)
    if maquina == 1:
        var_maquina.set('Eu escolhi pedra!               💎')
    elif maquina == 2:
        var_maquina.set('Eu escolhi papél!               🧻')
    elif maquina == 3:
        var_maquina.set('Eu escolhi tesoura!             ✀')

    if escolheu == maquina:
        var_resultado.set('Empate!')
        acumulador = 0
    elif escolheu == 1 and maquina == 2:
        var_resultado.set('Papél vence a pedra. Você perdeu!')
        acumulador = 1
    elif escolheu == 2 and maquina == 3:
        var_resultado.set('Tesoura corta papél. Você perdeu!')
        acumulador = 1
    elif escolheu == 3 and maquina == 1:
        var_resultado.set('Pedra quebra a tesoura. Você perdeu!')
        acumulador = 1
    elif escolheu == 1 and maquina == 3:
        var_resultado.set('Pedra quebra a tesoura. Você ganhou!')
        acumulador = 2
    elif escolheu == 2 and maquina == 1:
        var_resultado.set('Papél vence a pedra. Você ganhou!')
        acumulador = 2
    elif escolheu == 3 and maquina == 2:
        var_resultado.set('Tesoura corta papél. Você ganhou!')
        acumulador = 2

    acumula(acumulador)


# ---------------------------------------------------------------------------------------------------------------------
def acumula(resul):
    global soma_vitorias
    global soma_derrotas
    global soma_empates

    if resul == 2:
        soma_vitorias += 1
    elif resul == 1:
        soma_derrotas += 1
    else:
        soma_empates += 1

    diferenca = soma_vitorias - soma_derrotas
    if diferenca < 0:
        diferenca = diferenca*-1
        diferenca_txt = 'derrota(s)'
    else:
        diferenca_txt = 'vitoria(s)'

    total = soma_vitorias + soma_derrotas + soma_empates

    por_vitorias = soma_vitorias / total * 100
    por_derrotas = soma_derrotas / total * 100
    por_empates = soma_empates / total * 100

    var_vitoria.set(f'Vitórias: {soma_vitorias}          {por_vitorias:.2f}%')
    var_derrota.set(f'Derrotas: {soma_derrotas}        {por_derrotas:.2f}%')
    var_empate.set(f'Empates: {soma_empates}        {por_empates:.2f}%')
    var_diferenca.set(f'Diferença: {diferenca} {diferenca_txt}')
    var_jogos.set(f'Total de jogos: {total}')


# ---------------------------------------------------------------------------------------------------------------------
soma_vitorias = 0
soma_derrotas = 0
soma_empates = 0
# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Jokenpô')

largura_janela = 220
altura_janela = 220

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posl = float(largura_janela/2 - largura_tela/2)
posa = float(altura_janela/2 - altura_tela/2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posl, posa))
janela.resizable(width=False, height=False)
# ---------------------------------------------------------------------------------------------------------------------
var_escolha = tkinter.StringVar()
texto_escolha = tkinter.Label(janela, textvariable=var_escolha)
texto_escolha.place(x=10, y=40)

var_maquina = tkinter.StringVar()
texto_maquina = tkinter.Label(janela, textvariable=var_maquina)
texto_maquina.place(x=10, y=60)

var_resultado = tkinter.StringVar()
texto_resultado = tkinter.Label(janela, textvariable=var_resultado)
texto_resultado.place(x=10, y=85)

var_vitoria = tkinter.StringVar()
texto_vitoria = tkinter.Label(janela, textvariable=var_vitoria)
texto_vitoria.place(x=10, y=110)

var_derrota = tkinter.StringVar()
texto_derrota = tkinter.Label(janela, textvariable=var_derrota)
texto_derrota.place(x=10, y=130)

var_empate = tkinter.StringVar()
texto_empate = tkinter.Label(janela, textvariable=var_empate)
texto_empate.place(x=10, y=150)

var_diferenca = tkinter.StringVar()
texto_diferenca = tkinter.Label(janela, textvariable=var_diferenca)
texto_diferenca.place(x=10, y=170)

var_jogos = tkinter.StringVar()
texto_jogos = tkinter.Label(janela, textvariable=var_jogos)
texto_jogos.place(x=10, y=190)
# ---------------------------------------------------------------------------------------------------------------------
pedra = tkinter.Button(janela, text='Pedra 💎', command=lambda: escolha(1))
pedra.place(x=10, y=10)

papel = tkinter.Button(janela, text='Papél 🧻', command=lambda: escolha(2))
papel.place(x=70, y=10)

tesoura = tkinter.Button(janela, text='Tesoura ✀', command=lambda: escolha(3))
tesoura.place(x=130, y=10)
# ---------------------------------------------------------------------------------------------------------------------
keyboard.on_press_key('1', lambda _: escolha(1))
keyboard.on_press_key('2', lambda _: escolha(2))
keyboard.on_press_key('3', lambda _: escolha(3))

keyboard.on_press_key('q', lambda _: escolha(1))
keyboard.on_press_key('w', lambda _: escolha(2))
keyboard.on_press_key('e', lambda _: escolha(3))

keyboard.on_press_key('ESC', lambda _: janela.destroy())
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()

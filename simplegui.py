# Interface Gráfica com o Usuário

import PySimpleGUI as psg

import calcsimple
from calc import soma


layout = [

    [psg.Text('Informe n1: '),psg.InputText(key='num1')],
    [psg.Text('Informe n2: '),psg.InputText(key='num2')],
    [psg.Text(' ',key='Total')],
    [psg.Button('Calcular')],
         ]
janela = psg.Window('Calculadora Simples',layout)

while True:
        evento, valores = janela.read()
        if eventos== psg.WIN_CLOSED: break
        else:
            n1=int(valores['num1'])
            n2=int(valores['num2'])
            total=soma(n1,n2)
            janela['Total'].update(total)
janela.close()



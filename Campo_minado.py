import random
from tkinter import *
import time

minado = Tk()
minado.geometry("249x266+500+200")
minado.title("Campo Minado")

bombas = []
sort = []
camp_minas = []
savelista = []
x = 1
id_valor = 0

X1 = 80
X2 = 1
jogadas = []

infos = Frame(minado,width = 50,height = 40,bg='grey')
infos.pack(side = TOP, fill = X)

quant_pesas = Label(infos,text = X1,width = 6,bg='grey',font = ('ariel',10,'bold'),fg= 'white')
quant_pesas.place(x=100,y= 20)


pesas = Label(infos,text = "Peças",font = ('ariel',10,'bold'),bg='grey',fg= 'white')
pesas.place(x=100,y=1)

end_game = Frame(minado,width = 200,height = 150,relief = 'raised',bd = 5)

def sorteio():
    global sort
    global savelista
    
    for i in range(90):
        sort.append(i)
        savelista.append(0)

def sort_bombas():
    global bombas
    
    for i in range(10):
        bombas.append(random.choice(sort))
        sort.remove(bombas[-1])
        

def campo(x):
    global camp_minas
    
    for i in range(1,91):
        camp_minas.append(x)
        x +=1

        
def logica():
    global savelista
    
    for I in bombas:
        if I == 0 or 1<=I and I<9 or I == 9 or 80<I and I<89 or I == 89 or I==80:
            if I == 0:
                savelista[I+1] +=1
                savelista[I+10] +=1
                savelista[I+11] +=1

            elif I >= 1 and I < 9:
                savelista[I+1] +=1
                savelista[I+10] +=1
                savelista[I+11] +=1
                savelista[I-1] +=1
                savelista[I+9] +=1

            elif I == 9:
                savelista[I-1] +=1
                savelista[I+9] +=1
                savelista[I+10] +=1
                
            elif I > 80 and I < 89:
                savelista[I+1] +=1
                savelista[I-1] +=1
                savelista[I-11] +=1
                savelista[I-10] +=1
                savelista[I-9] +=1

            elif I == 80:
                savelista[I+1] +=1
                savelista[I-9] +=1
                savelista[I-10] +=1

            elif I == 89:
                savelista[I-1] +=1
                savelista[I-10] +=1
                savelista[I-11] +=1

        elif I != 10 and I != 20 and I != 30 and I != 40 and I != 50 and I != 60 and I != 70 and I != 19 and I != 29 and I != 39 and I != 49 and I != 59 and I != 69 and I != 79:
            
            savelista[I+1] +=1
            savelista[I-1] +=1
            savelista[I-11] +=1
            savelista[I+10] +=1
            savelista[I-10] +=1
            savelista[I+11] +=1
            savelista[I-9] +=1
            savelista[I+9] +=1

        else:
            
            for I1 in (10,20,30,40,50,60,70):
                if I == I1:
                    savelista[I+1] +=1
                    savelista[I+10] +=1
                    savelista[I+11] +=1
                    savelista[I-10] +=1
                    savelista[I-9] +=1

            for I2 in (19,29,39,49,59,69,79):
                if I == I2:
                    savelista[I-1] +=1
                    savelista[I+10] +=1
                    savelista[I+9] +=1
                    savelista[I-11] +=1
                    savelista[I-10] +=1
                




def placar(botoes,jogadas,end_game):
    global X2
    global X1

    X2 = 0
      
    for i in bombas:
        if id_valor != i:
            X2 += 1
    
    if X2 == 10:
        X1 = X1-1


    quant_pesas["text"] = X1
    
    if X1 == 0:
        end_game = Frame(minado,width = 250,height = 70,relief = 'raised',bd = 5)
        texto = Label(end_game,text = "Você Ganhou!",font = ('ariel',10,'bold'))
        
        bt_nv = Button(end_game,text= "Jogar Novamente!",command = lambda: novamente(end_game,botoes))   # Botão para jogar novamente
            
        end_game.place(x=0,y=0)
        texto.place(x = 75, y = 0)
        bt_nv.place(x= 70,y= 25)


    
    
def botoes(end_game):
    botao1 = Button(minado,width = 2, height = 1,command = lambda: frames(0,botoes,end_game))
    botao1.place(x=1,y=40)

    botao2 = Button(minado,width = 2, height = 1,command = lambda: frames(1,botoes,end_game))
    botao2.place(x=25,y=40)

    botao3 = Button(minado,width = 2, height = 1,command = lambda: frames(2,botoes,end_game))
    botao3.place(x=50,y=40)

    botao4 = Button(minado,width = 2, height = 1,command = lambda: frames(3,botoes,end_game))
    botao4.place(x=75,y=40)

    botao5 = Button(minado,width = 2, height = 1,command = lambda: frames(4,botoes,end_game))
    botao5.place(x=100,y=40)

    botao6 = Button(minado,width = 2, height = 1,command = lambda: frames(5,botoes,end_game))
    botao6.place(x=125,y=40)

    botao7 = Button(minado,width = 2, height = 1,command = lambda: frames(6,botoes,end_game))
    botao7.place(x=150,y=40)

    botao8 = Button(minado,width = 2, height = 1,command = lambda: frames(7,botoes,end_game))
    botao8.place(x=175,y=40)

    botao9 = Button(minado,width = 2, height = 1,command = lambda: frames(8,botoes,end_game))
    botao9.place(x=200,y=40)

    botao10 = Button(minado,width = 2, height = 1,command = lambda: frames(9,botoes,end_game))
    botao10.place(x=225,y=40)

    botao11 = Button(minado,width = 2, height = 1,command = lambda: frames(10,botoes,end_game))
    botao11.place(x=1,y=65)
    botao12 = Button(minado,width = 2, height = 1,command = lambda: frames(11,botoes,end_game))
    botao12.place(x=25,y=65)
    botao13 = Button(minado,width = 2, height = 1,command = lambda: frames(12,botoes,end_game))
    botao13.place(x=50,y=65)
    botao14 = Button(minado,width = 2, height = 1,command = lambda: frames(13,botoes,end_game))
    botao14.place(x=75,y=65)
    botao15 = Button(minado,width = 2, height = 1,command = lambda: frames(14,botoes,end_game))
    botao15.place(x=100,y=65)
    botao16 = Button(minado,width = 2, height = 1,command = lambda: frames(15,botoes,end_game))
    botao16.place(x=125,y=65)
    botao17 = Button(minado,width = 2, height = 1,command = lambda: frames(16,botoes,end_game))
    botao17.place(x=150,y=65)
    botao18 = Button(minado,width = 2, height = 1,command = lambda: frames(17,botoes,end_game))
    botao18.place(x=175,y=65)
    botao19 = Button(minado,width = 2, height = 1,command = lambda: frames(18,botoes,end_game))
    botao19.place(x=200,y=65)
    botao20 = Button(minado,width = 2, height = 1,command = lambda: frames(19,botoes,end_game))
    botao20.place(x=225,y=65)
    
    botao21 = Button(minado,width = 2, height = 1,command = lambda: frames(20,botoes,end_game))
    botao21.place(x=1,y=90)
    botao22 = Button(minado,width = 2, height = 1,command = lambda: frames(21,botoes,end_game))
    botao22.place(x=25,y=90)
    botao23 = Button(minado,width = 2, height = 1,command = lambda: frames(22,botoes,end_game))
    botao23.place(x=50,y=90)
    botao24 = Button(minado,width = 2, height = 1,command = lambda: frames(23,botoes,end_game))
    botao24.place(x=75,y=90)
    botao25 = Button(minado,width = 2, height = 1,command = lambda: frames(24,botoes,end_game))
    botao25.place(x=100,y=90)
    botao26 = Button(minado,width = 2, height = 1,command = lambda: frames(25,botoes,end_game))
    botao26.place(x=125,y=90)
    botao27 = Button(minado,width = 2, height = 1,command = lambda: frames(26,botoes,end_game))
    botao27.place(x=150,y=90)
    botao28 = Button(minado,width = 2, height = 1,command = lambda: frames(27,botoes,end_game))
    botao28.place(x=175,y=90)
    botao29 = Button(minado,width = 2, height = 1,command = lambda: frames(28,botoes,end_game))
    botao29.place(x=200,y=90)
    botao30 = Button(minado,width = 2, height = 1,command = lambda: frames(29,botoes,end_game))
    botao30.place(x=225,y=90)

    botao31 = Button(minado,width = 2, height = 1,command = lambda: frames(30,botoes,end_game))
    botao31.place(x=1,y=115)
    botao32 = Button(minado,width = 2, height = 1,command = lambda: frames(31,botoes,end_game))
    botao32.place(x=25,y=115)
    botao33 = Button(minado,width = 2, height = 1,command = lambda: frames(32,botoes,end_game))
    botao33.place(x=50,y=115)
    botao34 = Button(minado,width = 2, height = 1,command = lambda: frames(33,botoes,end_game))
    botao34.place(x=75,y=115)
    botao35 = Button(minado,width = 2, height = 1,command = lambda: frames(34,botoes,end_game))
    botao35.place(x=100,y=115)
    botao36 = Button(minado,width = 2, height = 1,command = lambda: frames(35,botoes,end_game))
    botao36.place(x=125,y=115)
    botao37 = Button(minado,width = 2, height = 1,command = lambda: frames(36,botoes,end_game))
    botao37.place(x=150,y=115)
    botao38 = Button(minado,width = 2, height = 1,command = lambda: frames(37,botoes,end_game))
    botao38.place(x=175,y=115)
    botao39 = Button(minado,width = 2, height = 1,command = lambda: frames(38,botoes,end_game))
    botao39.place(x=200,y=115)
    botao40 = Button(minado,width = 2, height = 1,command = lambda: frames(39,botoes,end_game))
    botao40.place(x=225,y=115)

    botao41 = Button(minado,width = 2, height = 1,command = lambda: frames(40,botoes,end_game))
    botao41.place(x=1,y=140)
    botao42 = Button(minado,width = 2, height = 1,command = lambda: frames(41,botoes,end_game))
    botao42.place(x=25,y=140)

    botao43 = Button(minado,width = 2, height = 1,command = lambda: frames(42,botoes,end_game))
    botao43.place(x=50,y=140)
    botao44 = Button(minado,width = 2, height = 1,command = lambda: frames(43,botoes,end_game))
    botao44.place(x=75,y=140)
    botao45 = Button(minado,width = 2, height = 1,command = lambda: frames(44,botoes,end_game))
    botao45.place(x=100,y=140)
    botao46 = Button(minado,width = 2, height = 1,command = lambda: frames(45,botoes,end_game))
    botao46.place(x=125,y=140)
    botao47 = Button(minado,width = 2, height = 1,command = lambda: frames(46,botoes,end_game))
    botao47.place(x=150,y=140)
    botao48 = Button(minado,width = 2, height = 1,command = lambda: frames(47,botoes,end_game))
    botao48.place(x=175,y=140)
    botao49 = Button(minado,width = 2, height = 1,command = lambda: frames(48,botoes,end_game))
    botao49.place(x=200,y=140)
    botao50 = Button(minado,width = 2, height = 1,command = lambda: frames(49,botoes,end_game))
    botao50.place(x=225,y=140)

    botao51 = Button(minado,width = 2, height = 1,command = lambda: frames(50,botoes,end_game))
    botao51.place(x=1,y=165)
    botao52 = Button(minado,width = 2, height = 1,command = lambda: frames(51,botoes,end_game))
    botao52.place(x=25,y=165)

    botao53 = Button(minado,width = 2, height = 1,command = lambda: frames(52,botoes,end_game))
    botao53.place(x=50,y=165)
    botao54 = Button(minado,width = 2, height = 1,command = lambda: frames(53,botoes,end_game))
    botao54.place(x=75,y=165)
    botao55 = Button(minado,width = 2, height = 1,command = lambda: frames(54,botoes,end_game))
    botao55.place(x=100,y=165)
    botao56 = Button(minado,width = 2, height = 1,command = lambda: frames(55,botoes,end_game))
    botao56.place(x=125,y=165)
    botao57 = Button(minado,width = 2, height = 1,command = lambda: frames(56,botoes,end_game))
    botao57.place(x=150,y=165)
    botao58 = Button(minado,width = 2, height = 1,command = lambda: frames(57,botoes,end_game))
    botao58.place(x=175,y=165)
    botao59 = Button(minado,width = 2, height = 1,command = lambda: frames(58,botoes,end_game))
    botao59.place(x=200,y=165)
    botao60 = Button(minado,width = 2, height = 1,command = lambda: frames(59,botoes,end_game))
    botao60.place(x=225,y=165)

    botao61 = Button(minado,width = 2, height = 1,command = lambda: frames(60,botoes,end_game))
    botao61.place(x=1,y=190)
    botao62 = Button(minado,width = 2, height = 1,command = lambda: frames(61,botoes,end_game))
    botao62.place(x=25,y=190)

    botao63 = Button(minado,width = 2, height = 1,command = lambda: frames(62,botoes,end_game))
    botao63.place(x=50,y=190)
    botao64 = Button(minado,width = 2, height = 1,command = lambda: frames(63,botoes,end_game))
    botao64.place(x=75,y=190)
    botao65 = Button(minado,width = 2, height = 1,command = lambda: frames(64,botoes,end_game))
    botao65.place(x=100,y=190)
    botao66 = Button(minado,width = 2, height = 1,command = lambda: frames(65,botoes,end_game))
    botao66.place(x=125,y=190)
    botao67 = Button(minado,width = 2, height = 1,command = lambda: frames(66,botoes,end_game))
    botao67.place(x=150,y=190)
    botao68 = Button(minado,width = 2, height = 1,command = lambda: frames(67,botoes,end_game))
    botao68.place(x=175,y=190)
    botao69 = Button(minado,width = 2, height = 1,command = lambda: frames(68,botoes,end_game))
    botao69.place(x=200,y=190)
    botao70 = Button(minado,width = 2, height = 1,command = lambda: frames(69,botoes,end_game))
    botao70.place(x=225,y=190)

    botao71 = Button(minado,width = 2, height = 1,command = lambda: frames(70,botoes,end_game))
    botao71.place(x=1,y=215)
    botao72 = Button(minado,width = 2, height = 1,command = lambda: frames(71,botoes,end_game))
    botao72.place(x=25,y=215)

    botao73 = Button(minado,width = 2, height = 1,command = lambda: frames(72,botoes,end_game))
    botao73.place(x=50,y=215)
    botao74 = Button(minado,width = 2, height = 1,command = lambda: frames(73,botoes,end_game))
    botao74.place(x=75,y=215)
    botao75 = Button(minado,width = 2, height = 1,command = lambda: frames(74,botoes,end_game))
    botao75.place(x=100,y=215)
    botao76 = Button(minado,width = 2, height = 1,command = lambda: frames(75,botoes,end_game))
    botao76.place(x=125,y=215)
    botao77 = Button(minado,width = 2, height = 1,command = lambda: frames(76,botoes,end_game))
    botao77.place(x=150,y=215)
    botao78 = Button(minado,width = 2, height = 1,command = lambda: frames(77,botoes,end_game))
    botao78.place(x=175,y=215)
    botao79 = Button(minado,width = 2, height = 1,command = lambda: frames(78,botoes,end_game))
    botao79.place(x=200,y=215)
    botao80 = Button(minado,width = 2, height = 1,command = lambda: frames(79,botoes,end_game))
    botao80.place(x=225,y=215)

    botao81 = Button(minado,width = 2, height = 1,command = lambda: frames(80,botoes,end_game))
    botao81.place(x=1,y=240)
    botao82 = Button(minado,width = 2, height = 1,command = lambda: frames(81,botoes,end_game))
    botao82.place(x=25,y=240)

    botao83 = Button(minado,width = 2, height = 1,command = lambda: frames(82,botoes,end_game))
    botao83.place(x=50,y=240)
    botao84 = Button(minado,width = 2, height = 1,command = lambda: frames(83,botoes,end_game))
    botao84.place(x=75,y=240)
    botao85 = Button(minado,width = 2, height = 1,command = lambda: frames(84,botoes,end_game))
    botao85.place(x=100,y=240)
    botao86 = Button(minado,width = 2, height = 1,command = lambda: frames(85,botoes,end_game))
    botao86.place(x=125,y=240)
    botao87 = Button(minado,width = 2, height = 1,command = lambda: frames(86,botoes,end_game))
    botao87.place(x=150,y=240)
    botao88 = Button(minado,width = 2, height = 1,command = lambda: frames(87,botoes,end_game))
    botao88.place(x=175,y=240)
    botao89 = Button(minado,width = 2, height = 1,command = lambda: frames(88,botoes,end_game))
    botao89.place(x=200,y=240)
    botao90 = Button(minado,width = 2, height = 1,command = lambda: frames(89,botoes,end_game))
    botao90.place(x=225,y=240)

    botoes = [botao1,botao2,botao3,botao4,botao5,botao6,botao7,botao8,botao9,botao10,
              botao11,botao12,botao13,botao14,botao15,botao16,botao17,botao18,botao19,botao20,
              botao21,botao22,botao23,botao24,botao25,botao26,botao27,botao28,botao29,botao30,
              botao31,botao32,botao33,botao34,botao35,botao36,botao37,botao38,botao39,botao40,
              botao41,botao42,botao43,botao44,botao45,botao46,botao47,botao48,botao49,botao50,
              botao51,botao52,botao53,botao54,botao55,botao56,botao57,botao58,botao59,botao60,
              botao61,botao62,botao63,botao64,botao65,botao66,botao67,botao68,botao69,botao70,
              botao71,botao72,botao73,botao74,botao75,botao76,botao77,botao78,botao79,botao80,
              botao81,botao82,botao83,botao84,botao85,botao86,botao87,botao88,botao89,botao90]




def frames(id_valor,botoes,end_game):
    global jogadas
    
    for i in bombas:
        if i == id_valor:
            imagembomba = PhotoImage(file = 'bomba.png')
            imagembomba = imagembomba.subsample(15,15)

            img_bombas = Label(minado,width = 20,height = 20,image = imagembomba, bg = "grey")
            img_bombas.image = imagembomba
            
            save = 0
            L = 25
            save = id_valor%10
            L = L*save
            A = 25
            save = id_valor//10
            A = A*save

            if A == 0:
                A = 40
            else:
                A = A+40
        
            img_bombas.place(x = L,y = A)
            jogadas.append(img_bombas)

            end_game = Frame(minado,width = 250,height = 70,relief = 'raised',bd = 5)
            texto = Label(end_game,text = "Você Perdeu!",font = ('ariel',10,'bold'))
            bt_nv = Button(end_game,text= "Jogar Novamente!",command = lambda: novamente(end_game,botoes))   # Botão para jogar novamente
            
            end_game.place(x=0,y=0)
            texto.place(x = 75, y = 0)
            bt_nv.place(x= 70,y= 25)

            break
        
        elif i == bombas[-1]:
            jogada = Label(minado,width = 2,height = 1,text = savelista[id_valor],font = ('ariel',12,'bold'),bg = "grey")
            jogadas.append(jogada)
            
            save = 0
            L = 25
            save = id_valor%10
            L = L*save
            A = 25
            save = id_valor//10
            A = A*save

            if A == 0:
                A = 40
            else:
                A = A+40
        
            jogada.place(x = L,y = A)
            placar(botoes,jogadas,end_game)

            

def novamente(end_game,botoes):
    global bombas,sort,camp_minas,savelista,x,id_valor,X1,X2,jogadas,quant_pesas
    bombas = []
    sort = []
    camp_minas = []
    savelista = []
    x = 1
    id_valor = 0

    X1 = 80
    X2 = 1
    quant_pesas["text"] = X1

    end_game.destroy()
    
    for jgs in jogadas:
        jgs.destroy()
        
    for bt in botoes:
        bt.destroy()
        
    jogadas = []

    main(end_game)
    

def main(end_game):

    x1 = -1
    sorteio()
    sort_bombas()
    campo(x)
    logica()
        
    botoes(end_game)

main(end_game)
    
minado.mainloop()

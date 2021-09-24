"Programação POWER UP no celular"
from tkinter import*

class Perna(Toplevel):

    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela9()
        self.widgets9()

    def tela9(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame29 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame29.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame31 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame31.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame25 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame25.place(relx=0.001,  # onde começa da esquerda
                          rely=0.077,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.05)  # altura
        self.frame007 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame007.place(relx=0.121,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.5,  # largura
                          relheight=0.28)  # altura
        self.frame27 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame27.place(relx=0.1981,  # onde começa da esquerda
                          rely=0.454,  # onde começa da direita
                          relwidth=0.6,  # largura
                          relheight=0.36)  # altura
        self.btn = Button(self,
                          command=self.voltar1,  # comando que ele executa
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=0.9,  # largura
                       relheight=0.10)

    def widgets9(self):
        self.text_power = Label(self.frame31,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_aluno = Label(self.frame25,  # onde irá aparecer o texto
                                text=" Leg Press",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_aluno.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.fundo = PhotoImage(file="atencao_p.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame27,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="white")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=1.0)

    def hide(self):  # esconde o root
        self.withdraw()

    def voltar1(self):
        print("ok")  
        self.hide()
        self.subframe = Exercicio(self)  # chamar a janela

class Braco(Toplevel):

    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela8()
        self.widgets9()

    def tela8(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame29 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame29.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame31 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame31.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame25 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame25.place(relx=0.001,  # onde começa da esquerda
                          rely=0.077,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.05)  # altura
        self.frame008 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame008.place(relx=0.121,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.50,  # largura
                          relheight=0.28)  # altura
        self.frame27 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame27.place(relx=0.191,  # onde começa da esquerda
                          rely=0.454,  # onde começa da direita
                          relwidth=0.6,  # largura
                          relheight=0.4)  # altura
        self.btn = Button(self,
                          command=self.voltar2,  # comando que ele executa
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=0.9,  # largura
                       relheight=0.10)

    def widgets9(self):
        self.text_power = Label(self.frame31,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_aluno = Label(self.frame25,  # onde irá aparecer o texto
                                text=" Barbell Bench Press",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_aluno.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.fundo = PhotoImage(file="atencao_b.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame27,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="white")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=1.0)

    def hide(self):  # esconde o root
        self.withdraw()

    def voltar2(self):
        print("ok")  
        self.hide()
        self.subframe = Exercicio(self)  # chamar a janela
        
class Exercicio(Toplevel):

    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela7()
        self.widgets8()

    def tela7(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame29 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame29.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame31 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame31.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame25 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame25.place(relx=0.001,  # onde começa da esquerda
                          rely=0.077,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.05)  # altura
        self.frame26 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame26.place(relx=0.121,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.35,  # largura
                          relheight=0.35)  # altura

        self.frame27 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame27.place(relx=0.551,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.35,  # largura
                          relheight=0.35)  # altura
        self.btn = Button(self,
                          command=self.voltar,  # comando que ele executa
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=0.9,  # largura
                       relheight=0.10)

    def widgets8(self):
        self.text_power = Label(self.frame31,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_aluno = Label(self.frame25,  # onde irá aparecer o texto
                                text=" Exercícios ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_aluno.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.btn = Button(self.frame26,
                          command=self.braco,  # comando que ele executa
                          text="Braço",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",11),
                          bg="gray",  # cor do botão
                          activebackground="gray",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=1.0,  # largura
                       relheight=0.2) # altura
        self.fundo = PhotoImage(file="braco.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame26,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="#ED7D31")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=0.79)
        
        self.btn = Button(self.frame27,
                          command=self.perna,  # comando que ele executa
                          text="Perna",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",11),
                          bg="gray",  # cor do botão
                          activebackground="gray",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=1.0,  # largura
                       relheight=0.2) # altura
        self.fundo1 = PhotoImage(file="perna.png")  # nome do arquivo escolhido
        self.img2 = Label(self.frame27,  # local onde vai aparecer o arquivo
                          image=self.fundo1,
                          bg="#ED7D31")
        self.img2.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=0.79)
        
        

    def hide(self):  # esconde o root
        self.withdraw()

    def braco(self):
        print("ok")  
        self.hide()
        self.subframe = Braco(self)  # chamar a janela

    def perna(self):
        print("ok")  
        self.hide()
        self.subframe = Perna(self)  # chamar a janela

    def voltar(self):
        print("ok")  
        self.hide()
        self.subframe = Entrar_tela(self)  # chamar a janela

    


class Ficha(Toplevel):
    
    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela6()
        self.widgets7()

    


    def tela6(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame29 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame29.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame31 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame31.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame32 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame32.place(relx=0.001,  # onde começa da esquerda
                          rely=0.077,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.05)  # altura
        self.frame33 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame33.place(relx=0.121,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.8,  # largura
                          relheight=0.6)  # altura
        self.btn = Button(self,
                          command=self.volta,  # comando que ele executa
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=0.9,  # largura
                       relheight=0.10)
        

    def widgets7(self):
        self.text_power = Label(self.frame31,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_aluno = Label(self.frame32,  # onde irá aparecer o texto
                                text=" Minha ficha",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_aluno.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.fundo = PhotoImage(file="minhaficha.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame33,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="white")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=1.0)

    def hide(self):  # esconde o root
        self.withdraw()

    def volta(self):
        print("ok")  
        self.hide()
        self.subframe = Entrar_tela(self)  # chamar a janela



class Entrar_tela(Toplevel):

    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela4()
        self.widgets6()
    
    def onClose(self):
        self.destroy()
        self.frame_original.show()

    def tela4(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame13 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame13.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame24 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame24.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame25 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame25.place(relx=0.001,  # onde começa da esquerda
                          rely=0.077,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.05)  # altura

        self.frame26 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame26.place(relx=0.121,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.35,  # largura
                          relheight=0.35)  # altura

        self.frame27 = Frame(self,
                            bg="#ED7D31")  # cor do frame 
        self.frame27.place(relx=0.551,  # onde começa da esquerda
                          rely=0.164,  # onde começa da direita
                          relwidth=0.35,  # largura
                          relheight=0.35)  # altura
    

    def widgets6(self):
        self.text_power = Label(self.frame24,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        
        self.text_aluno = Label(self.frame25,  # onde irá aparecer o texto
                                text=" Olá, aluno da acadêmia SESI ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_aluno.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        
        self.btn = Button(self.frame13,
                          command=self.onClose,  # comando que ele executa
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=0.9,  # largura
                       relheight=0.10)
        self.btn = Button(self.frame26,
                          command=self.ficha,  # comando que ele executa
                          text="Ficha",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",11),
                          bg="gray",  # cor do botão
                          activebackground="gray",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=1.0,  # largura
                       relheight=0.2) # altura
        self.fundo = PhotoImage(file="ficha.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame26,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="#ED7D31")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=0.79)
        
        self.btn = Button(self.frame27,
                          command=self.exercicio,  # comando que ele executa
                          text="Exercícios",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",11),
                          bg="gray",  # cor do botão
                          activebackground="gray",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                       rely=0.825,  # onde começa da direita
                       relwidth=1.0,  # largura
                       relheight=0.2) # altura
        self.fundo1 = PhotoImage(file="pesos.png")  # nome do arquivo escolhido
        self.img2 = Label(self.frame27,  # local onde vai aparecer o arquivo
                          image=self.fundo1,
                          bg="#ED7D31")
        self.img2.place(relx=0,  # onde começa da esquerda
                        rely=0,
                        relwidth=1.0,
                        relheight=0.79)

    def hide(self):  # esconde o root
        self.withdraw()
        
    def ficha(self):
        print("ok")  
        self.hide()
        self.subframe = Ficha(self)  # chamar a janela

    def exercicio(self):
        print("ok")  
        self.hide()
        self.subframe = Exercicio(self)  # chamar a janela
        
        


class Cadastrar_tela(Toplevel):

    def onClose(self):
        self.destroy()
        self.frame_original.show()

    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela5()
        self.widgets4()

    def tela5(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame14 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame14.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.text_power = Label(self.frame14,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.frame19 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame19.place(relx=0.014,  # onde começa da esquerda
                          rely=0.067,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.04)  # altura

        self.frame20 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame20.place(relx=0.0109,  # onde começa da esquerda
                          rely=0.17,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.035)  # altura
        self.frame21 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame21.place(relx=0.0119,  # onde começa da esquerda
                          rely=0.27,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.035)  # altura
        self.frame22 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame22.place(relx=0.0129,  # onde começa da esquerda
                          rely=0.37,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.035)  # altura
        self.frame23 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame23.place(relx=0.0139,  # onde começa da esquerda
                          rely=0.47,  # onde começa da direita
                          relwidth=0.7,  # largura
                          relheight=0.055)  # altura

        self.btn = Button(self.frame14,
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          command=self.onClose,  # comando que ele executa
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                          rely=0.825,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.10)
        self.btn = Button(self.frame23,
                          text="Cadastre-se",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          command=self.cadastra,  # comando que ele executa
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                       rely=0.0,  # onde começa da direita
                       relwidth=1.0,  # largura
                       relheight=1.0)
    def widgets4(self):
        self.text_e = Label(self.frame19,  # onde irá aparecer o texto
                                text="Nome ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_e.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_n = Label(self.frame20,  # onde irá aparecer o texto
                                text="E-mail  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_n.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_senha = Label(self.frame21,  # onde irá aparecer o texto
                                text="Senha  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_senha.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_csenha = Label(self.frame22,  # onde irá aparecer o texto
                                text="Comfirma senha  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_csenha.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        
        self.entra_e1= Entry(self,
                             font=("Arial",11),  # fonte e numero da letra
                             bg="white",  # cor de fundo
                             fg="black")  # cor da fonte)
        self.entra_e1.place(relx=0.095,  # onde começa da esquerda
                            rely=0.11,  # onde começa da direita
                            relwidth=0.8,  # largura
                            relheight=0.04)  # altura

        self.entra_n1 = Entry(self,
                               font=("Arial",11),  # fonte e numero da letra
                               bg="white",  # cor de fundo
                               fg="black")  # cor da fonte
        self.entra_n1.place(relx=0.105,  # onde começa da esquerda
                            rely=0.21,  # onde começa da direita
                            relwidth=0.8,  # largura
                            relheight=0.04)  # altura
        self.entra_senha1 = Entry(self,
                                  show="*",
                                  font=("Arial",11),  # fonte e numero da letra
                                  bg="white",  # cor de fundo
                                  fg="black")  # cor da fonte
        self.entra_senha1.place(relx=0.105,  # onde começa da esquerda
                                rely=0.31,  # onde começa da direita
                                relwidth=0.8,  # largura
                                relheight=0.04)  # altura
        self.entra_csenha1 = Entry(self,
                                   show="*",
                                   font=("Arial",11),  # fonte e numero da letra
                                   fg="black")  # cor da fonte
        self.entra_csenha1.place(relx=0.105,  # onde começa da esquerda
                                rely=0.41,  # onde começa da direita
                                relwidth=0.8,  # largura
                                relheight=0.04)  # altura

    def hide(self):  # esconde o root
        self.withdraw()
        
    def cadastra(self):
        print("ok")  
        self.hide()
        self.subframe = Entrar_tela(self)  # chamar a janela
        
    
    
class Esquece_senha(Toplevel):
    
    def __init__(self, original):  # o que vai rodar na terceira tela
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela3()
        self.widgets3()

    def onClose(self):
        self.destroy()
        self.frame_original.show()

    def tela3(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame10 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame10.place(relwidth=1,  # largura
                          relheight=1)  # altura
        self.frame15 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame15.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        self.frame16 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame16.place(relx=0.014,  # onde começa da esquerda
                          rely=0.067,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.04)  # altura

        self.frame17 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame17.place(relx=0.0109,  # onde começa da esquerda
                          rely=0.17,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.035)  # altura
        self.frame18 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame18.place(relx=0.0119,  # onde começa da esquerda
                          rely=0.27,  # onde começa da direita
                          relwidth=0.7,  # largura
                          relheight=0.075)  # altura
    def widgets3(self):
        self.text_power = Label(self.frame15,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        self.text_s = Label(self.frame16,  # onde irá aparecer o texto
                                text="Nova senha: ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_s.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_ns = Label(self.frame17,  # onde irá aparecer o texto
                                text="Confirmar senha:  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_ns.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita
        
        self.entra_s1= Entry(self,
                                  show="*",
                                 font=("Arial",11),  # fonte e numero da letra
                                 bg="white",  # cor de fundo
                                 fg="black")  # cor da fonte)
        self.entra_s1.place(relx=0.095,  # onde começa da esquerda
                          rely=0.11,  # onde começa da direita
                          relwidth=0.8,  # largura
                          relheight=0.04)  # altura

        self.entra_ns1 = Entry(self,
                                  show="*",
                                  font=("Arial",11),  # fonte e numero da letra
                                  bg="white",  # cor de fundo
                                  fg="black")  # cor da fonte)
        self.entra_ns1.place(relx=0.105,  # onde começa da esquerda
                          rely=0.21,  # onde começa da direita
                          relwidth=0.8,  # largura
                          relheight=0.04)  # altura

        self.btn = Button(self.frame10,
                          text="Voltar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          command=self.onClose,  # comando que ele executa
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.05,  # onde começa da esquerda
                          rely=0.825,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.10)
        self.btn = Button(self.frame18,
                          text="Confirmar",  # texto do primeiro botão da segunda tela
                          font=("Britannic Bold",20),
                          command=self.comfirma,  # comando que ele executa
                          bg="#f35b04",  # cor do botão
                          activebackground="#f35b04",  # utilizado para o botão não mudar de cor ao se acionado
                          fg="black",  # cor do texto do botão
                          activeforeground="black") # marter cor do texto do botão
        self.btn.place(relx=0.0,  # onde começa da esquerda
                          rely=0.0,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=1.0)

        

    def hide(self):  # esconde o root
        self.withdraw()
        
    def comfirma(self):
        print("ok")  
        self.hide()
        self.subframe = Tela_cadastro(self)  # chamar a janela

class Tela_cadastro(Toplevel):  

    def __init__(self, original):  # o que vai rodar na segunda tela
        self.frame_original = original
        Toplevel.__init__(self)  # importante metodo construtor
        self.tela2()
        self.widgets2()

    def tela2(self):
        self.title("POWER UP")  # Título da tela
        self.geometry("375x667+978+15")  # Tamanho e posição da tela
        self.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.resizable(False, False)  # comando para não mudar de tamanho
        self.frame5 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame5.place(relwidth=1,  # largura
                          relheight=1)  # altura
        
        self.frame4 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame4.place(relx=0.01,  # onde começa da esquerda
                          rely=0.01,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.07)  # altura
        
        self.frame6 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame6.place(relx=0.014,  # onde começa da esquerda
                          rely=0.067,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.04)  # altura

        self.frame7 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame7.place(relx=0.0109,  # onde começa da esquerda
                          rely=0.17,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.035)  # altura
        self.frame8 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame8.place(relx=0.0119,  # onde começa da esquerda
                          rely=0.27,  # onde começa da direita
                          relwidth=0.4,  # largura
                          relheight=0.045)  # altura
        self.frame9 = Frame(self,
                            bg="#f35b04")  # cor do frame 
        self.frame9.place(relx=0.0119,  # onde começa da esquerda
                          rely=0.35,  # onde começa da direita
                          relwidth=0.4,  # largura
                          relheight=0.045)  # altura
        self.frame11 = Frame(self,
                            bg="white")  # cor do frame 
        self.frame11.place(relx=0.0129,  # onde começa da esquerda
                          rely=0.45,  # onde começa da direita
                          relwidth=1.0,  # largura
                          relheight=0.10)  # altura
        self.frame12 = Frame(self,
                            bg="#f35b04") #cor do frame
        self.frame12.place(relx=0.0185,   #onde começa da esquerda
                           rely=0.55,     #onde começa da diteita
                           relwidth=0.5,  #largura
                           relheight=0.08) #altura

        

    def widgets2(self):
        self.text_power = Label(self.frame4,  # onde irá aparecer o texto
                                text="         POWER UP  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",24),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_power.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_entrar = Label(self.frame6,  # onde irá aparecer o texto
                                text="Login  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_entrar.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_senha = Label(self.frame7,  # onde irá aparecer o texto
                                text="Senha  ",  # o que aparecera para o usuario
                                font=("Britannic Bold",15),  # fonte e numero da letra
                                bg="#f35b04",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_senha.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.text_cadas = Label(self.frame11,  # onde irá aparecer o texto
                                text="Caso não possua conta, \nclique aqui para cria-la ",  # o que aparecera para o usuario
                                font=("Britannic Bold",20),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_cadas.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

        self.entra_login = Entry(self,
                                 font=("Arial",11),  # fonte e numero da letra
                                 bg="white",  # cor de fundo
                                 fg="black")  # cor da fonte)
        self.entra_login.place(relx=0.095,  # onde começa da esquerda
                          rely=0.11,  # onde começa da direita
                          relwidth=0.8,  # largura
                          relheight=0.04)  # altura

        self.entra_senha1 = Entry(self,
                                  show="*",
                                  font=("Arial",11),  # fonte e numero da letra
                                  bg="white",  # cor de fundo
                                  fg="black")  # cor da fonte)
        self.entra_senha1.place(relx=0.105,  # onde começa da esquerda
                          rely=0.21,  # onde começa da direita
                          relwidth=0.8,  # largura
                          relheight=0.04)  # altura
        self.btn_esquece = Button(self.frame8,  # em que frame esta o botão
                                  text="Esqueceu a senha?",  # o texto que aparece no botão
                                  bg="#f35b04",  # a cor do botão
                                  command=self.senha,  # comando que será executado
                                  activebackground="#f35b04",  # utiliza para quando clicar no botão
                                  font=("Arial",11),  # fonte e tamanho do texto
                                  fg="black",  # cor do texto
                                  activeforeground="black") # para continuar com a cor do texto
        self.btn_esquece.place(relx=0, # onde começa da esquerda
                               rely=0, # onde começa da direita
                               relwidth=1.00, # largura
                               relheig=1.00) # altura
        self.btn_comeca = Button(self.frame9,  # em que frame esta o botão
                                  text="Entrar",  # o texto que aparece no botão
                                  bg="#f35b04",  # a cor do botão
                                  command=self.entrar_,  # comando que será executado
                                  activebackground="#f35b04",  # utiliza para quando clicar no botão
                                  font=("Arial",15),  # fonte e tamanho do texto
                                  fg="black",  # cor do texto
                                  activeforeground="black") # para continuar com a cor do texto
        self.btn_comeca.place(relx=0, # onde começa da esquerda
                               rely=0, # onde começa da direita
                               relwidth=1.00, # largura
                               relheig=1.00) # altura
        self.btn_cadast = Button(self.frame12,  # em que frame esta o botão
                                  text="Cadastrar-se",  # o texto que aparece no botão
                                  bg="#f35b04",  # a cor do botão
                                  command=self.cadastro,  # comando que será executado
                                  activebackground="#f35b04",  # utiliza para quando clicar no botão
                                  font=("Arial",15),  # fonte e tamanho do texto
                                  fg="black",  # cor do texto
                                  activeforeground="black") # para continuar com a cor do texto
        self.btn_cadast.place(relx=0, # onde começa da esquerda
                               rely=0, # onde começa da direita
                               relwidth=1.00, # largura
                               relheig=1.00) # altura
        
        

    def hide(self):  # esconde o root
        self.withdraw()

    def senha(self):
        print("ok1")  # texto que aparecera se rodar
        self.hide()
        self.subframe = Esquece_senha(self)  # chamar a janela

    def entrar_(self):
        print("ok1")  # texto que aparecera se rodar
        self.hide()
        self.subframe = Entrar_tela(self)  # chamar a janela

    def cadastro(self):
        print("ok1")  # texto que aparecera se rodar
        self.hide()
        self.subframe = Cadastrar_tela(self)  # chamar a janela 

    def show(self):  # mostra outra janela
        self.update()
        self.deiconify()

        
        
class Tela1:
    def __init__(self):  # O que irá aparecer para o úsuario
        self.root = root
        self.tela()
        self.frame()
        self.widgets()
        root.mainloop()
        
    def tela(self):
        self.root.title("POWER UP")  # Título da tela
        self.root.geometry("375x667+978+15")  # Tamanho e posição da tela
        # Largura x Altura + Posição Horizontal + posição Vertical
        root.iconbitmap("logo-POWER-UP.ico")  # Icone
        self.root.resizable(False, False)  # comando para não mudar de tamanho
        
    def frame(self):  # Configurações do frame
        self.frame1 = Frame(root, # primeiro frame
                            bg = "white") # Cor do primeiro frame
        self.frame1.place(x=0,
                          y=0,
                          relwidth=1,
                          relheig=0.95)

        self.frame2 = Frame(self.root,
                            bg="#f35b04")  # cor do segundo frame da primera tela
        self.frame2.place(relx=0.05,  # onde começa da esquerda
                          rely=0.825,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.15)  # altura

        self.frame3 = Frame(self.root,
                            bg="white")  # cor do segundo frame da primera tela
        self.frame3.place(relx=0.05,  # onde começa da esquerda
                          rely=0.05,  # onde começa da direita
                          relwidth=0.9,  # largura
                          relheight=0.17)  # altura
        
    def widgets(self):
        self.btn_iniciar = Button(self.frame2,  # em que frame esta o botão
                                  text="Iniciar",  # o texto que aparece no botão
                                  bg="#f35b04",  # a cor do botão
                                  command=self.clicar_iniciar,  # comando que será executado
                                  activebackground="#f35b04",  # utiliza para quando clicar no botão
                                  font=("Britannic Bold",20),  # fonte e tamanho do texto
                                  fg="black",  # cor do texto
                                  activeforeground="black") # para continuar com a cor do texto
        self.btn_iniciar.place(relx=0, # onde começa da esquerda
                               rely=0, # onde começa da direita
                               relwidth=1.00, # largura
                               relheig=1.00) # altura
        self.fundo = PhotoImage(file="powerup1.png")  # nome do arquivo escolhido
        self.img1 = Label(self.frame1,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bg="white")
        self.img1.place(relx=0,  # onde começa da esquerda
                        rely=0.3,
                        relwidth=0.98,
                        relheight=0.68)

        self.text_login = Label(self.frame3,  # onde irá aparecer o texto
                                text="POWER UP",  # o que aparecera para o usuario
                                font=("Britannic Bold",52),  # fonte e numero da letra
                                bg="white",  # cor de fundo
                                fg="black")  # cor da fonte
        self.text_login.place(relx=0,  # onde começa da esquerda
                              rely=0 ) # onde começa da direita

    def hide(self):  # esconde o root
        self.root.withdraw()
        
    def clicar_iniciar(self):
        print("ok")  
        self.hide()
        self.subframe = Tela_cadastro(self)  # chamar a janela 
        
root = Tk()
Tela1()

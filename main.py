import backend as core
import customtkinter
from PIL import Image

#bojetivo - criar a secao de seu objetivo, criar a secao de seu objetivo para treinos e dietas, criar a area (meu perfil)


current_usuario = None
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def criar_tela_logado():
    #Tela principal logado
    global current_usuario
    main_logado = customtkinter.CTkToplevel(main_deslogado)
    main_logado.geometry("850x800")
    main_logado.resizable(width=False,height=False)



    frame_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame_logado.grid(row=0,column=0)
    minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
    lbl_nome_logado = customtkinter.CTkLabel(frame_logado,text="M-saude",width=630,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
    lbl_nome_logado.grid(row=0,column=0,padx=10,pady=10)

    frame2_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame2_logado.grid(row=0,column=1)
    btn_entrar_logado = customtkinter.CTkButton(frame2_logado,text="meu perfil",width=180,height=40,font=("Helvetica",20,"bold")).grid(row=0,column=2,padx=10,pady=6)

    frame4_logado = customtkinter.CTkFrame(main_logado,height=50,fg_color=["gray92", "gray14"])
    frame4_logado.grid(row=1,column=0,padx=0,pady=50)
    frame4_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.3)
    lbl_texto_logado = customtkinter.CTkLabel(frame4_logado,text="-"*120,font=("Helvetica",20,"bold"),width=200,text_color=["#2CC985", "#2FA572"]).grid(row=0,column=0,)




    frame3_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame3_logado.grid(row=2,column=0,padx=100,pady=50)
    frame3_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.4)
    lbl_principal_logado = customtkinter.CTkLabel(frame3_logado,text="Selecione a opcao desejada",font=("Helvetica",50,"bold"),width=200).grid(row=0,column=0,)


    frame5_logado = customtkinter.CTkFrame(main_logado,fg_color=["gray92", "gray14"])
    frame5_logado.grid(row=3,column=0,padx=200,pady=50)
    frame5_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.7)
    btn1_logado = customtkinter.CTkButton(frame5_logado,text="calcular imc",width=250,height=170,command=tela_calc_imc).grid(row=0,column=0,padx=60,pady=20)
    btn2_logado = customtkinter.CTkButton(frame5_logado,text="calcular basal",width=250,height=170,command=tela_calc_basal).grid(row=0,column=1,padx=60,pady=20)
    btn3_logado = customtkinter.CTkButton(frame5_logado,text="dieta personalizada",width=250,height=170,command=lambda:(tela_dieta_personalizada(),main_logado.withdraw())).grid(row=1,column=0,padx=60,pady=20)
    btn4_logado = customtkinter.CTkButton(frame5_logado,text="teste",width=250,height=170).grid(row=1,column=1,padx=60,pady=20)



#tela de log-in:
def tela_login():
    global main_logado
    global current_usuario
    global core
    tela_login = customtkinter.CTk()
    tela_login.geometry("300x250")
    tela_login.title("M-saude")
    tela_login.resizable(width=False,height=False)
    lbllogin = customtkinter.CTkLabel(tela_login,text="Faça seu login",font=('Arial',20,"bold"),text_color="white")
    lbllogin.pack(padx=5, pady=5)
    entrada_email = customtkinter.CTkEntry(tela_login,placeholder_text="Email:",width=250,font=("Arial",15,"bold"),placeholder_text_color="white")
    entrada_email.pack(padx=5,pady=5)
    entrada_senha_login = customtkinter.CTkEntry(tela_login,placeholder_text="Senha:",width=250,font=("Arial",15,"bold"),placeholder_text_color="white",show="*")
    entrada_senha_login.pack(padx=5,pady=5)
    def verificar():
        global current_usuario
        reusltado,current_usuario = core.login(entrada_email.get(),entrada_senha_login.get())
        if reusltado:
            print("achei",current_usuario)
            main_deslogado.withdraw()
            criar_tela_logado()
            
        else:
            print("nao achei")
            lbllogin_erro.configure(text="E-mail ou senha Inválidos")
    btn_login2 = customtkinter.CTkButton(tela_login,text="Entrar",font=("Arial",18,"bold"),fg_color=["#2CC985", "#2FA572"],hover_color="green",width=230,corner_radius=20,text_color="#DEEFE7",command=verificar)
    btn_login2.pack(padx=10,pady=10)
    btn_voltar = customtkinter.CTkButton(tela_login,text="Voltar",font=("Arial",18,"bold"),fg_color=["#2CC985", "#2FA572"],hover_color="green",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_voltar.pack()
    lbllogin_erro = customtkinter.CTkLabel(tela_login,text='',font=("Arial",15,"bold"),text_color="red")
    lbllogin_erro.pack(padx=10,pady=10)
    tela_login.mainloop()

#tela de cadastro:
def tela_cadastro():
    tela_cadastro = customtkinter.CTk()
    tela_cadastro.geometry("500x500")
    entrada_nome = customtkinter.CTkEntry(tela_cadastro,placeholder_text="nome")
    entrada_nome.pack()
    entrada_email = customtkinter.CTkEntry(tela_cadastro,placeholder_text="email")
    entrada_email.pack()
    entrada_senha = customtkinter.CTkEntry(tela_cadastro,placeholder_text="senha")
    entrada_senha.pack()
    generos = ['M','F']
    genero = customtkinter.CTkOptionMenu(tela_cadastro,values=generos)
    genero.pack()
    entrada_idade = customtkinter.CTkEntry(tela_cadastro,placeholder_text="idade")
    entrada_idade.pack()
    def verificar():
        resultado = core.verificar_se_ja_adicionado(entrada_nome.get(),entrada_email.get(),entrada_senha.get(),entrada_idade.get(),genero.get())
        if resultado:
            print("ja adicionado")
        else:
            core.cadastrar_usuario(entrada_nome.get(),entrada_email.get(),entrada_senha.get(),entrada_idade.get(),genero.get())
            print("adicionado")
    botao = customtkinter.CTkButton(tela_cadastro,text="cadastrar",command=verificar)
    botao.pack()
    tela_cadastro.mainloop()

#tela calculadora imc
def tela_calc_imc():
    tela_imc = customtkinter.CTk()
    tela_imc.geometry("500x500")
    lbl_altura = customtkinter.CTkLabel(tela_imc,text="altura")
    lbl_altura.pack()
    entrada_altura = customtkinter.CTkEntry(tela_imc,placeholder_text="altura em cm")
    entrada_altura.pack()
    lbl_peso = customtkinter.CTkLabel(tela_imc,text="peso")
    lbl_peso.pack()
    entrada_peso = customtkinter.CTkEntry(tela_imc,placeholder_text="peso em kg")
    entrada_peso.pack()
    def verificar():
        try:
            resultado = core.calcular_IMC(int(entrada_peso.get()),int(entrada_altura.get()))
            if resultado != None:
                lbl_imc.configure(text="O seu imc eh de {:.2f}".format(resultado[0]))
                lbl_classificacao.configure(text="sua classificacao eh de {}".format(resultado[1]))
            else:
                print("erro")
        except:
            lbl_classificacao.configure(text="digite valores validos")
    btn_calc = customtkinter.CTkButton(tela_imc,text="calacular",command=verificar)
    btn_calc.pack()
    lbl_imc = customtkinter.CTkLabel(tela_imc,text='')
    lbl_imc.pack()
    lbl_classificacao = customtkinter.CTkLabel(tela_imc,text='')
    lbl_classificacao.pack()
    tela_imc.mainloop()

#tela calculadora basal
def tela_calc_basal():
    tela_basal = customtkinter.CTkToplevel(main_deslogado)
    tela_basal.geometry("500x550")
    tela_basal.resizable(width=False,height=False)
    minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
    lbl_nome_app = customtkinter.CTkLabel(tela_basal,text="M-saude",width=450,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
    lbl_nome_app.pack(padx=10,pady=10)
    lbl_peso = customtkinter.CTkLabel(tela_basal,text="Peso",font=("Arial",30,"bold"))
    lbl_peso.pack(padx=5,pady=5)
    entrada_peso = customtkinter.CTkEntry(tela_basal,placeholder_text="Peso em kg:", placeholder_text_color="gray",font=("Arial",15),width=250)
    entrada_peso.pack(padx=5,pady=5)

    lbl_altura = customtkinter.CTkLabel(tela_basal,text="Altura",font=("Arial",30,"bold"))
    lbl_altura.pack(padx=5,pady=5)
    
    entrada_altura = customtkinter.CTkEntry(tela_basal,placeholder_text="Altura em cm:", placeholder_text_color="gray",font=("Arial",15),width=250)
    entrada_altura.pack(padx=5,pady=5)

    lbl_idade = customtkinter.CTkLabel(tela_basal,text="Idade",font=("Arial",30,"bold"))
    lbl_idade.pack(padx=5,pady=5)

    entrada_idade = customtkinter.CTkEntry(tela_basal,placeholder_text="Idade:", placeholder_text_color="gray",font=("Arial",15))
    entrada_idade.pack(padx=5,pady=5)

    lbl_genero = customtkinter.CTkLabel(tela_basal,text="Gênero",font=("Arial",23,"bold"))
    lbl_genero.pack(padx=5,pady=5)
    
    entrada_genero = customtkinter.CTkOptionMenu(tela_basal,values=['M','F'],font=("Arial",23,"bold"))
    entrada_genero.pack(padx=5,pady=5)

    def verificar():
        try:
            resultado = core.calcular__basal(entrada_genero.get(),int(entrada_peso.get()),int(entrada_altura.get()),int(entrada_idade.get()))
            if resultado != None:
                lbl_resultado.configure(text="A sua taxa basal é de\n{:.2f}Kcal".format(resultado),font=("Arial",45,"bold"),text_color="#7cfc00")
                tela_basal.geometry("500x650")
            else:
                print("erro")
        except:
            lbl_resultado.configure(text="Digite valores validos",text_color="red",font=("Arial",20,"bold"))
    btn_calc = customtkinter.CTkButton(tela_basal,text="Calcular",font=("Arial",23,"bold"),width=200,command=verificar)
    btn_calc.pack(padx=5,pady=8)
    lbl_resultado = customtkinter.CTkLabel(tela_basal,text='')
    lbl_resultado.pack()
    #tela_basal. mainloop()
#tela_dieta_personalizada
def tela_dieta_personalizada():
    if current_usuario != None:
        tela_objetivo()
        
    else:
        print("faca login")
        popup = customtkinter.CTkToplevel(main_deslogado)
        popup.geometry("200x200")
        lbl = customtkinter.CTkLabel(popup,text="faca login")
        lbl.pack()
        popup.bind("<Destroy>", lambda event: print('just closed'))

def tela_objetivo():
    tela_seu_objetivo = customtkinter.CTkToplevel(main_deslogado)
    tela_seu_objetivo.geometry("500x500")
    lbl_principal_objetivo = customtkinter.CTkLabel(tela_seu_objetivo,text="escolha seu objetivo")
    lbl_principal_objetivo.pack()

#Tela principal deslogado
main_deslogado = customtkinter.CTk()
main_deslogado.geometry("850x800")
main_deslogado.resizable(width=False,height=False)



frame = customtkinter.CTkFrame(main_deslogado,height=100,fg_color=["gray92", "gray14"])
frame.grid(row=0,column=0)
minha_imagem = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
lbl_nome = customtkinter.CTkLabel(frame,text="M-saude",width=630,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem)
lbl_nome.grid(row=0,column=0,padx=10,pady=10)

frame2 = customtkinter.CTkFrame(main_deslogado,height=100,fg_color=["gray92", "gray14"])
frame2.grid(row=0,column=1)
btn_entrar = customtkinter.CTkButton(frame2,text="Entrar",width=180,height=40,font=("Helvetica",20,"bold"),command=tela_login).grid(row=0,column=2,padx=10,pady=6)
btn_cadastrar = customtkinter.CTkButton(frame2,text="Cadastre-se",width=180,height=40,font=("Helvetica",20,"bold"),command=tela_cadastro).grid(row=1,column=2,padx=10,pady=6)

frame4 = customtkinter.CTkFrame(main_deslogado,height=50,fg_color=["gray92", "gray14"])
frame4.grid(row=1,column=0,padx=0,pady=50)
frame4.place(in_=main_deslogado, anchor="c", relx=.5, rely=.3)
lbl_texto = customtkinter.CTkLabel(frame4,text="-"*120,font=("Helvetica",20,"bold"),width=200,text_color=["#2CC985", "#2FA572"]).grid(row=0,column=0,)




frame3 = customtkinter.CTkFrame(main_deslogado,height=100,fg_color=["gray92", "gray14"])
frame3.grid(row=2,column=0,padx=100,pady=50)
frame3.place(in_=main_deslogado, anchor="c", relx=.5, rely=.4)
lbl_principal = customtkinter.CTkLabel(frame3,text="Selecione a opcão desejada",font=("Helvetica",50,"bold"),width=200).grid(row=0,column=0,)


frame5 = customtkinter.CTkFrame(main_deslogado,fg_color=["gray92", "gray14"])
frame5.grid(row=3,column=0,padx=200,pady=50)
frame5.place(in_=main_deslogado, anchor="c", relx=.5, rely=.7)
imagem_basal = customtkinter.CTkImage(Image.open("imagens/basal.ico"), size=(200, 165))
imagem_imc = customtkinter.CTkImage(Image.open("imagens/imc.ico"), size=(200, 165))
imagem_dieta = customtkinter.CTkImage(Image.open("imagens/Dieta.ico"), size=(200, 165))
imagem_treio = customtkinter.CTkImage(Image.open("imagens/treino.ico"), size=(200, 165))
btn1 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_imc,command=tela_calc_imc).grid(row=0,column=0,padx=60,pady=20)
btn2 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_basal,command=tela_calc_basal).grid(row=0,column=1,padx=60,pady=20)
btn3 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_dieta,command=tela_dieta_personalizada).grid(row=1,column=0,padx=60,pady=20)
btn4 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_treio).grid(row=1,column=1,padx=60,pady=20)
lbl_faca_login = customtkinter.CTkLabel(main_deslogado,text="").grid(row=2,column=1,padx=60,pady=20)


main_deslogado.mainloop()






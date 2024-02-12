import backend as core
import customtkinter
from PIL import Image
from time import sleep

#objetivo - funcao de apagar dietas e treinos, front end tela de listagem de meus treinos e minhas dietas


current_usuario = None
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


    


def criar_tela_logado():
    global current_usuario
    def abrir_tela_meu_perfil():
        tela_meu_perfil = customtkinter.CTkToplevel(main_deslogado)
        tela_meu_perfil.geometry("300x300")
        minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
        lbl_nome_app = customtkinter.CTkLabel(tela_meu_perfil,text="M-saude",width=450,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
        lbl_nome_app.pack(padx=10,pady=10)
        btn_minhas_dietas = customtkinter.CTkButton(tela_meu_perfil,text="Minhas dietas",font=("Arial",20,"bold"),width=270,command=tela_minhas_dietas)
        btn_minhas_dietas.pack(padx=5,pady=5)
        btn_meus_treinos = customtkinter.CTkButton(tela_meu_perfil,text="Meus treinos",font=("Arial",20,"bold"),width=270,command=tela_meus_treinos)
        btn_meus_treinos.pack(padx=5,pady=5)
        btn_sair = customtkinter.CTkButton(tela_meu_perfil,text="Sair",font=("Arial",20,"bold"),width=270,fg_color="red",command=lambda:(log_off(),tela_meu_perfil.withdraw()))
        btn_sair.pack(padx=5,pady=5)
        btn_voltar = customtkinter.CTkButton(tela_meu_perfil,text="Voltar",font=("Arial",20,"bold"),width=270,fg_color="gray",command=lambda:(main_logado.deiconify(),tela_meu_perfil.withdraw()))
        btn_voltar.pack(padx=5,pady=5)
        main_logado.withdraw()
        

    #Tela principal logado
    main_logado = customtkinter.CTkToplevel(main_deslogado)
    main_logado.geometry("850x800")
    main_logado.resizable(width=False,height=False)



    frame_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame_logado.grid(row=0,column=0)
    minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
    lbl_nome_logado = customtkinter.CTkLabel(frame_logado,text="M-saude",width=690,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
    lbl_nome_logado.grid(row=0,column=0,padx=10,pady=10)

    frame2_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame2_logado.grid(row=0,column=1)
    minha_imagem_menu = customtkinter.CTkImage(Image.open("imagens/icone_menu.ico"),size=(50,50))
    btn_entrar_logado = customtkinter.CTkButton(frame2_logado,text="",width=100,height=40,font=("Helvetica",20,"bold"),image=minha_imagem_menu,corner_radius=100,command=abrir_tela_meu_perfil).grid(row=0,column=2,padx=10,pady=6)

    frame4_logado = customtkinter.CTkFrame(main_logado,height=50,fg_color=["gray92", "gray14"])
    frame4_logado.grid(row=1,column=0,padx=0,pady=50)
    frame4_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.3)
    lbl_texto_logado = customtkinter.CTkLabel(frame4_logado,text="-"*120,font=("Helvetica",20,"bold"),width=200,text_color=["#2CC985", "#2FA572"]).grid(row=0,column=0,)




    frame3_logado = customtkinter.CTkFrame(main_logado,height=100,fg_color=["gray92", "gray14"])
    frame3_logado.grid(row=2,column=0,padx=100,pady=50)
    frame3_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.4)
    lbl_principal_logado = customtkinter.CTkLabel(frame3_logado,text="Selecione a opção desejada",font=("Helvetica",50,"bold"),width=200).grid(row=0,column=0,)


    frame5_logado = customtkinter.CTkFrame(main_logado,fg_color=["gray92", "gray14"])
    frame5_logado.grid(row=3,column=0,padx=200,pady=50)
    frame5_logado.place(in_=main_logado, anchor="c", relx=.5, rely=.7)
    imagem_basal = customtkinter.CTkImage(Image.open("imagens/basal.ico"), size=(200, 165))
    imagem_imc = customtkinter.CTkImage(Image.open("imagens/imc.ico"), size=(200, 165))
    imagem_dieta = customtkinter.CTkImage(Image.open("imagens/Dieta.ico"), size=(200, 165))
    imagem_treio = customtkinter.CTkImage(Image.open("imagens/treino.ico"), size=(200, 165))
    btn1_logado = customtkinter.CTkButton(frame5_logado,text="",width=250,height=165,image=imagem_imc,command=tela_calc_imc).grid(row=0,column=0,padx=60,pady=20)
    btn2_logado = customtkinter.CTkButton(frame5_logado,text="",width=250,height=165,image=imagem_basal,command=tela_calc_basal).grid(row=0,column=1,padx=60,pady=20)
    btn3_logado = customtkinter.CTkButton(frame5_logado,text="",width=250,height=165,image=imagem_dieta,command=lambda:(tela_dieta_personalizada(),main_logado.withdraw())).grid(row=1,column=0,padx=60,pady=20)
    btn4_logado = customtkinter.CTkButton(frame5_logado,text="",width=250,height=165,image=imagem_treio,command=lambda:(tela_treinos_personalizados(),main_logado.withdraw())).grid(row=1,column=1,padx=60,pady=20)
    
    #funcoes da tela meu perfil
    def tela_minhas_dietas():
        tela = customtkinter.CTkToplevel(main_deslogado)
        tela.geometry("1000x500")
        dietas = core.listar_dietas(current_usuario)
        def abrir_link(link):
            core.abrir_link(link)
        for elementos in dietas:
            print(elementos)
            lbl = customtkinter.CTkLabel(tela,text=elementos)
            lbl.pack()
           
            btn = customtkinter.CTkButton(tela,text="abrir",command=lambda l=elementos:abrir_link(l))
            btn.pack()
        
        print(dietas)
    def tela_meus_treinos():
        tela = customtkinter.CTkToplevel(main_deslogado)
        tela.geometry("1000x500")
        treinos = core.listar_treinos(current_usuario)
        def abrir_link(link):
            core.abrir_link(link)
        for elementos in treinos:
            print(elementos)
            lbl = customtkinter.CTkLabel(tela,text=elementos)
            lbl.pack()
           
            btn = customtkinter.CTkButton(tela,text="abrir",command=lambda l=elementos:abrir_link(l))
            btn.pack()
    def log_off():
        global current_usuario
        current_usuario = None
        main_deslogado.deiconify()
        main_logado.withdraw()
    def tela_dieta_personalizada():
        if current_usuario != None:
            tela_seu_objetivo = customtkinter.CTkToplevel(main_deslogado)
            tela_seu_objetivo.geometry("400x300")
            minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
            lbl_nome_app = customtkinter.CTkLabel(tela_seu_objetivo,text="M-saude",width=350,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
            lbl_nome_app.pack(padx=10,pady=10)
            lbl_principal_objetivo = customtkinter.CTkLabel(tela_seu_objetivo,text="escolha seu objetivo",font=("Arial",25,"bold"))
            lbl_principal_objetivo.pack(padx=5,pady=5)
            #funcoes da tela
            def perder_peso():
                tela_dietas = customtkinter.CTkToplevel(main_deslogado)
                tela_dietas.geometry("400x450")
                minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
                lbl_nome_app = customtkinter.CTkLabel(tela_dietas,text="M-saude",width=300,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
                lbl_nome_app.pack(padx = 10, pady =10)
                btn_dieta1 = customtkinter.CTkButton(tela_dietas,text="Dieta de 1800kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta1800calorias.pdf"),print("abriu")))
                btn_dieta1.pack(padx=5,pady=5)
                btn_add_dieta1 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta1800calorias.pdf",current_usuario),print("adicionou")))
                btn_add_dieta1.pack(padx=5,pady=5)
                btn_dieta2 = customtkinter.CTkButton(tela_dietas,text="Dieta de 1500kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta1500calorias.pdf"),print("abriu")))
                btn_dieta2.pack(padx=5,pady=5)
                btn_add_dieta2 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta1500calorias.pdf",current_usuario),print("adicionou")))
                btn_add_dieta2.pack(padx=5,pady=5)
                btn_dieta3 = customtkinter.CTkButton(tela_dietas,text="Dieta de 2000kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta2000calorias.pdf"),print("abriu")))
                btn_dieta3.pack(padx=5,pady=5)
                btn_add_dieta3 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta2000calorias.pdf",current_usuario),print("adicionou")))
                btn_add_dieta3.pack(padx=5,pady=5)
                btn_voltar = customtkinter.CTkButton(tela_dietas,text="voltar",command=lambda:(tela_seu_objetivo.deiconify(),tela_dietas.withdraw()),fg_color="red",font=("Arial",20,"bold"))
                btn_voltar.pack(padx=5,pady=5)
            def hipertrofia():
                tela_dietas = customtkinter.CTkToplevel(main_deslogado)
                tela_dietas.geometry("400x450")
                minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
                lbl_nome_app = customtkinter.CTkLabel(tela_dietas,text="M-saude",width=300,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
                lbl_nome_app.pack(padx = 10, pady =10)
                btn_dieta1 = customtkinter.CTkButton(tela_dietas,text="Dieta de 2500kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta2500calorias.pdf"),print("abriu")))
                btn_dieta1.pack(padx=5,pady=5)
                btn_add_dieta1 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta2500calorias.pdf",current_usuario),print("adicionou")))
                btn_add_dieta1.pack(padx=5,pady=5)
                btn_dieta2 = customtkinter.CTkButton(tela_dietas,text="Dieta de 2800kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://pt.scribd.com/document/453088515/2800kcal-1"),print("abriu")))
                btn_dieta2.pack(padx=5,pady=5)
                btn_add_dieta2 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://pt.scribd.com/document/453088515/2800kcal-1",current_usuario),print("adicionou")))
                btn_add_dieta2.pack(padx=5,pady=5)
                btn_dieta3 = customtkinter.CTkButton(tela_dietas,text="Dieta de 3000kcal",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta3000calorias.pdf"),print("abriu")))
                btn_dieta3.pack(padx=5,pady=5)
                btn_add_dieta3 = customtkinter.CTkButton(tela_dietas,text="Adicionar dieta",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_dieta("https://www.endocrinologiausp.com.br/wp-content/uploads/2010/04/dieta3000calorias.pdf",current_usuario),print("adicionou")))
                btn_add_dieta3.pack(padx=5,pady=5)
                btn_voltar = customtkinter.CTkButton(tela_dietas,text="voltar",command=lambda:(tela_seu_objetivo.deiconify(),tela_dietas.withdraw()),fg_color="red",font=("Arial",20,"bold"))
                btn_voltar.pack(padx=5,pady=5)
            btn_perder_peso = customtkinter.CTkButton(tela_seu_objetivo,text="Peca de peso",width=350, font=("Arial",20,"bold"),command=perder_peso)
            btn_perder_peso.pack(padx=5,pady=5)
            btn_hipertrofia = customtkinter.CTkButton(tela_seu_objetivo,text="Hipertrofia",width=350, font=("Arial",20,"bold"),command=hipertrofia)
            btn_hipertrofia.pack(padx=5,pady=5)
            btn_voltar = customtkinter.CTkButton(tela_seu_objetivo,text="Voltar",width=350, font=("Arial",20,"bold"),fg_color="gray",command=lambda:(main_logado.deiconify(),tela_seu_objetivo.withdraw()))
            btn_voltar.pack(padx=5,pady=5)
            
        else:
            if x == 1:
                print("faca login")
                popup = customtkinter.CTkToplevel(main_deslogado)
                popup.geometry("200x200")
                lbl = customtkinter.CTkLabel(popup,text="faca login")
                lbl.pack()  

    def tela_treinos_personalizados():
        if current_usuario != None:
            tela_seu_objetivo = customtkinter.CTkToplevel(main_deslogado)
            tela_seu_objetivo.geometry("400x300")
            minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
            lbl_nome_app = customtkinter.CTkLabel(tela_seu_objetivo,text="M-saude",width=350,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
            lbl_nome_app.pack(padx=10,pady=10)
            lbl_principal_objetivo = customtkinter.CTkLabel(tela_seu_objetivo,text="escolha seu objetivo",font=("Arial",25,"bold"))
            lbl_principal_objetivo.pack(padx=5,pady=5)
            #funcoes da tela
            def perder_peso():
                tela_treinos = customtkinter.CTkToplevel(main_deslogado)
                tela_treinos.geometry("400x450")
                minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
                lbl_nome_app = customtkinter.CTkLabel(tela_treinos,text="M-saude",width=300,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
                lbl_nome_app.pack(padx = 10, pady =10)
                btn_treino1 = customtkinter.CTkButton(tela_treinos,text="Treino de cardio intenso",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://teses.usp.br/teses/disponiveis/39/39133/tde-14022013-085048/publico/Versao_para_impressao_Material_didatico_do_programa_de_intervencao_Anexo_4_corrigido.pdf"),print("abriu")))
                btn_treino1.pack(padx=5,pady=5)
                btn_add_treino1 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://teses.usp.br/teses/disponiveis/39/39133/tde-14022013-085048/publico/Versao_para_impressao_Material_didatico_do_programa_de_intervencao_Anexo_4_corrigido.pdf",current_usuario),print("adicionou")))
                btn_add_treino1.pack(padx=5,pady=5)
                btn_treino2 = customtkinter.CTkButton(tela_treinos,text="treino de costas",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://pt.scribd.com/document/628056676/costas"),print("abriu")))
                btn_treino2.pack(padx=5,pady=5)
                btn_add_treino2 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://pt.scribd.com/document/628056676/costas",current_usuario),print("adicionou")))
                btn_add_treino2.pack(padx=5,pady=5)
                btn_treino3 = customtkinter.CTkButton(tela_treinos,text="Treino de perna",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://cepe.usp.br/wp-content/uploads/TREINO-4-Muscula%C3%A7%C3%A3o.pdf"),print("abriu")))
                btn_treino3.pack(padx=5,pady=5)
                btn_add_treino3 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://cepe.usp.br/wp-content/uploads/TREINO-4-Muscula%C3%A7%C3%A3o.pdf",current_usuario),print("adicionou")))
                btn_add_treino3.pack(padx=5,pady=5)
                btn_voltar = customtkinter.CTkButton(tela_treinos,text="voltar",command=lambda:(tela_seu_objetivo.deiconify(),tela_treinos.withdraw()),fg_color="red",font=("Arial",20,"bold"))
                btn_voltar.pack(padx=5,pady=5)
            def hipertrofia():
                tela_treinos = customtkinter.CTkToplevel(main_deslogado)
                tela_treinos.geometry("400x450")
                minha_imagem_logado = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
                lbl_nome_app = customtkinter.CTkLabel(tela_treinos,text="M-saude",width=300,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",75,"bold"),corner_radius=10,image=minha_imagem_logado)
                lbl_nome_app.pack(padx = 10, pady =10)
                btn_treino1 = customtkinter.CTkButton(tela_treinos,text="Treino de superiores completo",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://www.crefsp.gov.br/storage/app/arquivos/4d57a525a306535a4162d2c7bafd1b95.pdf"),print("abriu")))
                btn_treino1.pack(padx=5,pady=5)
                btn_add_treino1 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://www.crefsp.gov.br/storage/app/arquivos/4d57a525a306535a4162d2c7bafd1b95.pdf",current_usuario),print("adicionou")))
                btn_add_treino1.pack(padx=5,pady=5)
                btn_treino2 = customtkinter.CTkButton(tela_treinos,text="treino de costas",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://pt.scribd.com/document/628056676/costas"),print("abriu")))
                btn_treino2.pack(padx=5,pady=5)
                btn_add_treino2 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://pt.scribd.com/document/628056676/costas",current_usuario),print("adicionou")))
                btn_add_treino2.pack(padx=5,pady=5)
                btn_treino3 = customtkinter.CTkButton(tela_treinos,text="Treino de perna",font=("Arial",25,"bold"),fg_color="gray",command=lambda:(core.abrir_link("https://cepe.usp.br/wp-content/uploads/TREINO-4-Muscula%C3%A7%C3%A3o.pdf"),print("abriu")))
                btn_treino3.pack(padx=5,pady=5)
                btn_add_treino3 = customtkinter.CTkButton(tela_treinos,text="Adicionar treino",font=("Arial",20,"bold"),command=lambda:(core.cadastrar_treino("https://cepe.usp.br/wp-content/uploads/TREINO-4-Muscula%C3%A7%C3%A3o.pdf",current_usuario),print("adicionou")))
                btn_add_treino3.pack(padx=5,pady=5)
                btn_voltar = customtkinter.CTkButton(tela_treinos,text="voltar",command=lambda:(tela_seu_objetivo.deiconify(),tela_treinos.withdraw()),fg_color="red",font=("Arial",20,"bold"))
                btn_voltar.pack(padx=5,pady=5)
            btn_perder_peso = customtkinter.CTkButton(tela_seu_objetivo,text="Perca de peso",width=350, font=("Arial",20,"bold"),command=perder_peso)
            btn_perder_peso.pack(padx=5,pady=5)
            btn_hipertrofia = customtkinter.CTkButton(tela_seu_objetivo,text="Hipertrofia",width=350, font=("Arial",20,"bold"),command=hipertrofia)
            btn_hipertrofia.pack(padx=5,pady=5)
            btn_voltar = customtkinter.CTkButton(tela_seu_objetivo,text="Voltar",width=350, font=("Arial",20,"bold"),fg_color="gray",command=lambda:(main_logado.deiconify(),tela_seu_objetivo.withdraw()))
            btn_voltar.pack(padx=5,pady=5)    
        else:
            if x == 1:
                print("faca login")
                popup = customtkinter.CTkToplevel(main_deslogado)
                popup.geometry("200x200")
                lbl = customtkinter.CTkLabel(popup,text="faca login")
                lbl.pack()   

#tela de log-in:
def criar_tela_login():
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
            tela_login.withdraw()
            
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
    tela_cadastro = customtkinter.CTkToplevel(main_deslogado)
    tela_cadastro.geometry("500x520")
    minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
    lbl_nome_app = customtkinter.CTkLabel(tela_cadastro,text="M-saude",width=400,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
    lbl_nome_app.pack(padx=10, pady=10)
    lbl_nome_cadastro = customtkinter.CTkLabel(tela_cadastro,text="Nome",font=("Arial",20,"bold"))
    lbl_nome_cadastro.pack(padx=5,pady=5)
    entrada_nome = customtkinter.CTkEntry(tela_cadastro,placeholder_text="Digite seu nome:",width=300)
    entrada_nome.pack()
    lbl_email_cadastro = customtkinter.CTkLabel(tela_cadastro,text="Email",font=("Arial",20,"bold"))
    lbl_email_cadastro.pack(padx=5,pady=5)
    entrada_email = customtkinter.CTkEntry(tela_cadastro,placeholder_text="Digite seu e-mail:",width=300)
    entrada_email.pack()
    lbl_senha_cadastro = customtkinter.CTkLabel(tela_cadastro,text="Senha",font=("Arial",20,"bold"))
    lbl_senha_cadastro.pack(padx=5,pady=5)
    entrada_senha = customtkinter.CTkEntry(tela_cadastro,placeholder_text="Digite sua senha:",width=200)
    entrada_senha.pack()
    generos = ['M','F']
    lbl_genero_cadastro = customtkinter.CTkLabel(tela_cadastro,text="Gênero",font=("Arial",20,"bold"))
    lbl_genero_cadastro.pack(padx=5,pady=5)
    genero = customtkinter.CTkOptionMenu(tela_cadastro,values=generos)
    genero.pack(padx=5,pady=5)
    lbl_idade_cadastro = customtkinter.CTkLabel(tela_cadastro,text="Idade",font=("Arial",20,"bold"))
    lbl_idade_cadastro.pack(padx=5,pady=5)
    entrada_idade = customtkinter.CTkEntry(tela_cadastro,placeholder_text="Digite sua idade")
    entrada_idade.pack(padx=5,pady=5)
    def verificar():
        resultado = core.verificar_se_ja_adicionado(entrada_nome.get(),entrada_email.get(),entrada_senha.get(),entrada_idade.get(),genero.get())
        if resultado:
            tela_cadastro.geometry("500x600")
            lbl_resultado.configure(text="Informações inválidas \nou \nusuário já adicionado",font=("Arial",20,"bold"),text_color="red")
        else:
            core.cadastrar_usuario(entrada_nome.get(),entrada_email.get(),entrada_senha.get(),entrada_idade.get(),genero.get())
            tela_cadastro.geometry("500x600")
            lbl_resultado.configure(text="Usuário adicionado com sucesso!",font=("Arial",20,"bold"),text_color="green")
    botao = customtkinter.CTkButton(tela_cadastro,text="Cadastrar",font=("Arial",20,"bold"),command=verificar)
    botao.pack(padx=5,pady=5)
    lbl_resultado = customtkinter.CTkLabel(tela_cadastro,text="")
    lbl_resultado.pack()
    tela_cadastro.mainloop()

#tela calculadora imc
def tela_calc_imc():
    tela_imc = customtkinter.CTkToplevel(main_deslogado)
    tela_imc.geometry("500x350")
    minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
    lbl_nome_app = customtkinter.CTkLabel(tela_imc,text="M-saude",width=450,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
    lbl_nome_app.pack(padx=10,pady=10)
    lbl_altura = customtkinter.CTkLabel(tela_imc,text="Altura",font=("Arial",30,"bold"))
    lbl_altura.pack(padx=5,pady=5)
    entrada_altura = customtkinter.CTkEntry(tela_imc,placeholder_text="Altura em cm:",placeholder_text_color="gray",font=("Arial",15),width=250)
    entrada_altura.pack(padx=5,pady=5)
    lbl_peso = customtkinter.CTkLabel(tela_imc,text="Peso",font=("Arial",30,"bold"))
    lbl_peso.pack(padx=5,pady=5)
    entrada_peso = customtkinter.CTkEntry(tela_imc,placeholder_text="Peso em kg:",placeholder_text_color="gray",font=("Arial",15),width=250)
    entrada_peso.pack(padx=5,pady=5)
    def verificar():
        try:
            resultado = core.calcular_IMC(int(entrada_peso.get()),int(entrada_altura.get()))
            if resultado != None:
                tela_imc.geometry("500x430")
                lbl_imc.configure(text="O seu imc é de {:.2f}".format(resultado[0]),font=("Arial",25,"bold"),text_color="green")
                lbl_classificacao.configure(text="Sua classificacao é de: {}".format(resultado[1]),font=("Arial",25,"bold"),text_color="green")
            else:
                print("erro")
        except:
            tela_imc.geometry("500x400")
            lbl_imc.configure(text="")
            lbl_classificacao.configure(text="Digite valores validos",font=("Arial",25,"bold"),text_color="red")
    btn_calc = customtkinter.CTkButton(tela_imc,text="Calcular",font=("Arial",23,"bold"),width=200,command=verificar)
    btn_calc.pack(padx=5,pady=5)
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
    
x = 0
#tela dieta personalizada
def tela_dieta_personalizada():
    if current_usuario != None:
        tela_seu_objetivo = customtkinter.CTkToplevel(main_deslogado)
        tela_seu_objetivo.geometry("400x300")
        minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
        lbl_nome_app = customtkinter.CTkLabel(tela_seu_objetivo,text="M-saude",width=350,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
        lbl_nome_app.pack(padx=10,pady=10)
        lbl_principal_objetivo = customtkinter.CTkLabel(tela_seu_objetivo,text="escolha seu objetivo",font=("Arial",25,"bold"))
        lbl_principal_objetivo.pack(padx=5,pady=5)
        btn_perder_peso = customtkinter.CTkButton(tela_seu_objetivo,text="Peca de peso",width=350, font=("Arial",20,"bold"))
        btn_perder_peso.pack(padx=5,pady=5)
        btn_hipertrofia = customtkinter.CTkButton(tela_seu_objetivo,text="Hipertrofia",width=350, font=("Arial",20,"bold"))
        btn_hipertrofia.pack(padx=5,pady=5)
        btn_voltar = customtkinter.CTkButton(tela_seu_objetivo,text="Voltar",width=350, font=("Arial",20,"bold"),fg_color="gray",command=lambda:(main_logado.deiconify(),tela_seu_objetivo.withdraw()))
        btn_voltar.pack(padx=5,pady=5)
        
    else:
        if x == 1:
            print("faca login")
            popup = customtkinter.CTkToplevel(main_deslogado)
            popup.geometry("200x100")
            lbl = customtkinter.CTkLabel(popup,text="Faça log-in ou cadastre-se para ter acesso à função",wraplength=180,font=("Arial",20,"bold"),text_color="red")
            lbl.pack()
            

def tela_treinos_personalizados():
    if current_usuario != None:
        tela_seu_objetivo = customtkinter.CTkToplevel(main_deslogado)
        tela_seu_objetivo.geometry("400x300")
        minha_imagem2 = customtkinter.CTkImage(Image.open("imagens/icone_saude.ico"), size=(100, 100))
        lbl_nome_app = customtkinter.CTkLabel(tela_seu_objetivo,text="M-saude",width=350,height=100,fg_color=["#2CC985", "#2FA572"],font=("Helvetica",50,"bold"),corner_radius=10,image=minha_imagem2)
        lbl_nome_app.pack(padx=10,pady=10)
        lbl_principal_objetivo = customtkinter.CTkLabel(tela_seu_objetivo,text="escolha seu objetivo",font=("Arial",25,"bold"))
        lbl_principal_objetivo.pack(padx=5,pady=5)
        btn_perder_peso = customtkinter.CTkButton(tela_seu_objetivo,text="Perca de peso",width=350, font=("Arial",20,"bold"))
        btn_perder_peso.pack(padx=5,pady=5)
        btn_hipertrofia = customtkinter.CTkButton(tela_seu_objetivo,text="Hipertrofia",width=350, font=("Arial",20,"bold"))
        btn_hipertrofia.pack(padx=5,pady=5)
        btn_voltar = customtkinter.CTkButton(tela_seu_objetivo,text="Voltar",width=350, font=("Arial",20,"bold"),fg_color="gray",command=lambda:(main_logado.deiconify(),tela_seu_objetivo.withdraw()))
        btn_voltar.pack(padx=5,pady=5)
        
    else:
        if x == 1:
            print("faca login")
            popup = customtkinter.CTkToplevel(main_deslogado)
            popup.geometry("200x100")
            lbl = customtkinter.CTkLabel(popup,text="Faça log-in ou cadastre-se para ter acesso à função",wraplength=180,font=("Arial",20,"bold"),text_color="red")
            lbl.pack()
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
btn_entrar = customtkinter.CTkButton(frame2,text="Entrar",width=180,height=40,font=("Helvetica",20,"bold"),command=criar_tela_login).grid(row=0,column=2,padx=10,pady=6)
btn_cadastrar = customtkinter.CTkButton(frame2,text="Cadastre-se",width=180,height=40,font=("Helvetica",20,"bold"),command=tela_cadastro).grid(row=1,column=2,padx=10,pady=6)

frame4 = customtkinter.CTkFrame(main_deslogado,height=50,fg_color=["gray92", "gray14"])
frame4.grid(row=1,column=0,padx=0,pady=50)
frame4.place(in_=main_deslogado, anchor="c", relx=.5, rely=.3)
lbl_texto = customtkinter.CTkLabel(frame4,text="-"*120,font=("Helvetica",20,"bold"),width=200,text_color=["#2CC985", "#2FA572"]).grid(row=0,column=0,)




frame3 = customtkinter.CTkFrame(main_deslogado,height=100,fg_color=["gray92", "gray14"])
frame3.grid(row=2,column=0,padx=100,pady=50)
frame3.place(in_=main_deslogado, anchor="c", relx=.5, rely=.4)
lbl_principal = customtkinter.CTkLabel(frame3,text="Selecione a opção desejada",font=("Helvetica",50,"bold"),width=200).grid(row=0,column=0,)

def atribuicao():
    global x
    x+=1
    print(x)
frame5 = customtkinter.CTkFrame(main_deslogado,fg_color=["gray92", "gray14"])
frame5.grid(row=3,column=0,padx=200,pady=50)
frame5.place(in_=main_deslogado, anchor="c", relx=.5, rely=.7)
imagem_basal = customtkinter.CTkImage(Image.open("imagens/basal.ico"), size=(200, 165))
imagem_imc = customtkinter.CTkImage(Image.open("imagens/imc.ico"), size=(200, 165))
imagem_dieta = customtkinter.CTkImage(Image.open("imagens/Dieta.ico"), size=(200, 165))
imagem_treio = customtkinter.CTkImage(Image.open("imagens/treino.ico"), size=(200, 165))
btn1 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_imc,command=tela_calc_imc).grid(row=0,column=0,padx=60,pady=20)
btn2 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_basal,command=tela_calc_basal).grid(row=0,column=1,padx=60,pady=20)
btn3 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_dieta,command=lambda:(atribuicao(),tela_dieta_personalizada())).grid(row=1,column=0,padx=60,pady=20)
btn4 = customtkinter.CTkButton(frame5,text="",width=250,height=165,image=imagem_treio,command=lambda:(atribuicao(),tela_treinos_personalizados())).grid(row=1,column=1,padx=60,pady=20)
lbl_faca_login = customtkinter.CTkLabel(main_deslogado,text="").grid(row=2,column=1,padx=60,pady=20)


main_deslogado.mainloop()






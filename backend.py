import json
import webbrowser

class Usuario():
    def __init__(self,nome, email,senha,idade,genero):
        self.Nome = nome
        self.Email = email
        self.Senha = senha
        self.Idade = idade
        self.Genero = genero
        self.Dietas = []
        self.Treinos = []


def calcular_IMC(peso,altura):
    altura_formatada = altura /100
    imc = peso / (altura_formatada*altura_formatada)
    if imc <18.5:
        classificacao = "baixo peso"
    elif imc >=18.5 and imc <=24.9:
        classificacao = "peso ideal"
    elif imc >=25 and imc <=29.9:
        classificacao = "sobrepeso"
    elif imc >=30 and imc <=34.9:
        classificacao = "obesidade grau 1"
    elif imc >=35 and imc <=39.9:
        classificacao = "obesidade grau 2"
    elif imc > 39.9:
        classificacao = "obesidade extrema"
    return imc,classificacao

def calcular__basal(genero, peso, altura,idade):

    if genero == 'M':
        basal = 66 + (13.8 * peso) + (5*altura) - (6.8 * idade)
    elif genero == 'F':
        basal = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    else:
        basal = 0
    
    return basal

def verificar_se_ja_adicionado(nome, email,senha,idade,genero):
    user = Usuario(nome,email,senha,idade,genero)
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    dados_atualizados = carregar_dados('bd.json')
    adiconado = False
    for elemetos in dados_atualizados:
        if elemetos['email'].lower() == user.Email.lower() or nome == '' or senha == '' or email == '':
            adiconado = True
            break
                
        else:
            adiconado = False
    return adiconado
    
def cadastrar_usuario(nome, email,senha,idade,genero):
    user = Usuario(nome,email,senha,idade,genero)
    user.Dietas = []
    user.Treinos = []
    
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    
        

    def salvar_dados(nome_arquivo, novos_dados):
        dados_existentes = carregar_dados('bd.json')
        dados_existentes.append(novos_dados)

        with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados_existentes, arquivo, indent=2)
    dados_atualizados = carregar_dados('bd.json')
    adiconado = False
    for elemetos in dados_atualizados:
        if elemetos['nome'].lower() == user.Nome.lower() or nome == '' or senha == '' or email == '':
            adiconado = True
            break
                
        else:
            adiconado = False
           

    if adiconado == True:
        return adiconado
        
    
    else:

        salvar_dados('bd.json',{
            "nome":user.Nome,
            "email":user.Email,
            "senha":user.Senha,
            "idade":user.Idade,
            "genero":user.Genero,
            "dietas": user.Dietas,
            "treinos": user.Treinos
        })
        return adiconado
    
def login(email,senha):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    dados_atualizados = carregar_dados("bd.json")
    achei = False
    current_usuario = None
    for elemetos in dados_atualizados:
        if elemetos['email'] == email and elemetos['senha'] == senha:
            achei = True
            current_usuario = elemetos['nome']
            break
        else:
            achei = False
            current_usuario = None
    return achei,current_usuario
             
def cadastrar_treino(treino,usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    def salvar_dados(nome_arquivo,dados_atualizados):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=2)
    dados_atualizados = carregar_dados('bd.json')
    for elemetos in dados_atualizados:
        
        if elemetos['nome'] == usuario:
            elemetos['treinos'].append(treino)
            break
    salvar_dados('bd.json',dados_atualizados)
   
def cadastrar_dieta(dieta,usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    def salvar_dados(nome_arquivo,dados_atualizados):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=2)
    dados_atualizados = carregar_dados('bd.json')
    for elemetos in dados_atualizados:
        
        if elemetos['nome'] == usuario:
            elemetos['dietas'].append(dieta)
            break
    salvar_dados('bd.json',dados_atualizados)

def listar_treinos(usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    dados_atualziados = carregar_dados('bd.json')
    for elemetos in dados_atualziados:
        if elemetos['nome'] == usuario:
            treinos = elemetos['treinos']
            break
        else:
            treinos = "nada encontrado"
    return treinos

def listar_dietas(usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    dados_atualziados = carregar_dados('bd.json')
    for elemetos in dados_atualziados:
        if elemetos['nome'] == usuario:
            dietas = elemetos['dietas']
            break
        else:
            dietas =  "nehum usuario encontrado"
        
    return dietas

def deletar_dietas(dieta, usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    def salvar_dados(nome_arquivo,dados_atualizados):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=2)
    dados_atualizados = carregar_dados('bd.json')
    for elementos in dados_atualizados:
        dietas=elementos['dietas']
        if elementos['nome'] == usuario:
            dietas.remove(dieta)
            break
    
    salvar_dados('bd.json',dados_atualizados)

def deletar_treinos(treino,usuario):
    def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
    def salvar_dados(nome_arquivo,dados_atualizados):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=2)
    dados_atualizados = carregar_dados('bd.json')
    for elementos in dados_atualizados:
        if elementos['nome'] == usuario:
            elementos['treinos'].remove(treino)
            break
    salvar_dados('bd.json',dados_atualizados)

def abrir_link(link):
    new = 2
    url = link
    webbrowser.open(url,new=new)
        

       
    

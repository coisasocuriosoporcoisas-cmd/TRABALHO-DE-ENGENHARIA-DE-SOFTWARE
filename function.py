#pensei em fazer um sistema de cadastro de perdidos de uma loja qualquer 
#cliente, terá como atributo -id, cpf, nome,email, perdido
import json
import os
import customtkinter as ctk
from Constants import DATA_PATH

def bancoCarregado():
    print("carregando banco de dados...")
    if not os.path.exists(DATA_PATH):
        print(f"Arquivo {DATA_PATH} não encontrado. Criando um novo arquivo.")
        with open(DATA_PATH, 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo)  # Cria um arquivo JSON vazio
    try:
        with open(DATA_PATH, 'r', encoding ='utf-8') as arquivo:
            return  json.load(arquivo)
           
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Retornando lista vazia.")
        return []




def ValidarEmail(email: str):
    if '@' in email and '.' in email:
        return True
    else:
        return False
    
def criarAlerta(texto,titulo, master=None):
    alerta = ctk.CTkToplevel(master)
    alerta.title(titulo)
    alerta.geometry("400x200")
    #faz o alerta aparece na frente 
    alerta.lift()
    alerta.attributes("-topmost",True)

    textoAlerta = ctk.CTkLabel(alerta, text=texto, font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"),corner_radius=8)
    textoAlerta.pack(pady=30, padx=30)

    btnOk = ctk.CTkButton(alerta,text="OK",fg_color="#D32F2F",command=alerta.destroy)
    btnOk.pack(pady=20,padx=20)
    



def CadastraCliente( cpf, nome,telefone, email, perdido, master=None):
    if ValidarEmail(email) == True:
        bancoAtual = bancoCarregado()
        if len(bancoAtual )== 0:
            id =1
        else:
            id = bancoAtual[-1]['id']+1

        novoUsuario= {
                "id": id,
                "cpf": cpf,
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "perdido": perdido
            }    
        bancoAtual.append(novoUsuario) 

        with open(DATA_PATH,'w', encoding="utf-8") as arquivo:
            json.dump(bancoAtual,arquivo, indent=4,ensure_ascii=False)
    else:
        criarAlerta("Alerta, email invalído!","email aviso", master=None)




def ExcluirUsuario(cpf):
    banco_atual = bancoCarregado()
    CpfUser = cpf.strip()
    Cpf_achado = None
    for cpfbuscado in banco_atual:
        if str(cpfbuscado.get('cpf')).strip()  == CpfUser:
            Cpf_achado = cpfbuscado
            break

    if  Cpf_achado is not None:
        banco_atual.remove(Cpf_achado)

        with open(DATA_PATH,'w',encoding="utf-8") as arquivo:
            json.dump(banco_atual,arquivo, ensure_ascii=False, indent=4)
        return True
    return False
#está pegando tentando pegar um dicionario e não um json. conserta isso


def PesquisarUser(TermoDigitado):
    banco_atual = bancoCarregado()
    termoBusc = str(TermoDigitado).strip().lower()

    userEncontrados = []

    for user in banco_atual:
        cpf = str(user.get('cpf','')).strip().lower()
        nome = str(user.get('nome','')).strip().lower()

        if termoBusc in cpf or termoBusc in nome:
            userEncontrados.append(user)

    return userEncontrados
    




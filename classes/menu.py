
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import customtkinter as ctk
from formulario import  FormularioCadastra
from cardUser import Card
#menu


class MenuLateral(ctk.CTk):
    def __init__(self, controller=None):
        super().__init__()#essa herança é passada atráves das classes, no caso as telas de acordo com o toque do usuario, por isso controller é none, já que ele nunca mudar, mas o seu contéudo(janelas(ctkframes))
        
        self.controller = controller#controle é a interface principal
        self.title("Sistema de cadastro")

       
        #fundo menu lateral
        self.side_menu = ctk.CTkFrame(self, width=932, height=700)
        self.side_menu.pack(side='left', fill ='y',padx=10, pady=10)
        #botões
        self.btn_home = ctk.CTkButton(self.side_menu,text="incio",command = self.show_home)
        self.btn_home.pack(pady =20, padx=20)
        self.btnCadastra = ctk.CTkButton(self.side_menu, text="cadastra", command= self.tela2Cadastra)
        self.btnCadastra.pack(pady=20, padx=20)
        self.btnDeletarUser = ctk.CTkButton(self.side_menu, text="Deleta Usuário", command= self.DeletaUsuario)
        self.btnDeletarUser.pack(pady=20, padx=20)
        #frames de conteudo home page
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side='left', fill = 'both', expand =True, padx=10, pady=10)
        self.show_home()
    #função de limpa o contéudo
    def Limpartela(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
   
    
    #funçãoes de mostra contéudo da tela
    def show_home(self):#tela inicial
        self.Limpartela()
        self.carduser = Card(self.content_frame)#classe cardPessoa, mostra o card e consequêtemente suas informações
        
        

    def tela2Cadastra(self):#cadatra pessoa
        self.Limpartela()
        self.formulario = FormularioCadastra(self.content_frame)#declaração da classe FormularioCadastro, que servira como função principal para isso
        self.formulario.pack(pady=20)

    def DeletaUsuario(self):
        self.Limpartela()
        welcame_label = ctk.CTkLabel(self.content_frame, text ="tá funcionando (tela3)", font=("Arial bold", 20))
        welcame_label.pack(pady=20)
   

if __name__ == "__main__":
    app = MenuLateral()
    app.geometry("932x700")
    app.mainloop()
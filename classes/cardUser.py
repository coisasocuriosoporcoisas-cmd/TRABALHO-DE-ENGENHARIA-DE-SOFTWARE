import sys 
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import customtkinter as ctk

import function as fc
class Card(ctk.CTkFrame):
    def __init__(self, telaPrincipal):
        super().__init__(telaPrincipal)
        self.telaPrincipal =telaPrincipal
        self.textoCard = ctk.CTkLabel(self, text="usuários")
        self.textoCard.pack()

        scroll_frame = ctk.CTkScrollableFrame(self.telaPrincipal, width=450, height=350)
        scroll_frame.pack(fill="both", expand=True, padx=15, pady=15)

        dadosUsuarios = fc.bancoCarregado(fc.ArquivoJson)
        if not dadosUsuarios:
            self.Labelvazio = ctk.CTkLabel(self,text="não há cadatros")
            self.Labelvazio.pack()

        for dadoUser in dadosUsuarios:
            self.card = ctk.CTkFrame(scroll_frame, fg_color="blue",border_width=3, border_color="#3cc765", corner_radius=10)
            self.card.pack(fill="x", padx=10, pady=8)

            self.lblUser = ctk.CTkLabel(self.card, text=f"Nome: {dadoUser.get('nome')} | Cpf: {dadoUser.get("cpf")}",anchor="w")
            self.lblUser.pack(fill="x", padx=15, pady=(10, 2))



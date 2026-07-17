import customtkinter as ctk

class PessoaCard(ctk.CTkFrame):
    """Componente visual para exibir as informações de uma pessoa."""
    def __init__(self, master, pessoa, **kwargs):
        super().__init__(master, fg_color="#242424", **kwargs)
        
        self.pessoa = pessoa
        self._criar_widgets()

    def _criar_widgets(self):
        # Checkbox (posicionado à direita)
        self.check_input = ctk.CTkCheckBox(self, text="")
        self.check_input.pack(side="right", padx=10)

        # Informações de texto (alinhadas à esquerda)
        self.name_label = ctk.CTkLabel(self, text=f"Nome: {self.pessoa.get('name')}")
        self.name_label.pack(side="top", anchor="w", padx=10, pady=(2, 0))
        
        self.cpf_label = ctk.CTkLabel(self, text=f"CPF: {self.pessoa.get('cpf')}")
        self.cpf_label.pack(side="top", anchor="w", padx=10, pady=(0, 2))
        
        self.number_label = ctk.CTkLabel(self, text=f"Número: {self.pessoa.get('number')}")
        self.number_label.pack(side="top", anchor="w", padx=10, pady=(0, 2))

        self.email_label = ctk.CTkLabel(self, text=f"Email: {self.pessoa.get('email')}")
        self.email_label.pack(side="top", anchor="w", padx=10, pady=(0, 2))
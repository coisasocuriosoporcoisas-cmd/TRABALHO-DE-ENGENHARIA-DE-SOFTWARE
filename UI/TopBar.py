import customtkinter as ctk
from function import PesquisarUser, bancoCarregado

class TopBar(ctk.CTkFrame):
    # recebe master (janela principal)
    # recebe comando_excluir (função que será chamada ao clicar no botão "Excluir")
    # recebe ao_adicionar (função que será chamada ao clicar no botão "Adicionar")
    # recebe atualizar_interface (função que será chamada para atualizar a interface)
    # recebe kwargs (argumentos adicionais, que servem para customizar o frame, como cor de fundo, altura, etc.)
    def __init__(self, master, comando_excluir, ao_adicionar=None, atualizar_interface=None, **kwargs):
        super().__init__(master, fg_color="#3b3b3b", height=50, corner_radius=0, **kwargs)
        self.pack_propagate(False)
        
        # O argumento 'ao_adicionar' recebe a função que será executada ao clicar
        # como assim? 
        # ele vai receber a função 'novo_registro' da classe App, que é passada como argumento na criação do TopBar no App.py
        self.comando_excluir = comando_excluir
        self.ao_adicionar = ao_adicionar
        self.atualizar_interface = atualizar_interface
        self.texto_pesquisa = ctk.StringVar()
        self._criar_widgets()
        self.texto_pesquisa.trace_add("write", self.ao_digitar)  # Chama ao_digitar sempre que o texto mudar

    def _criar_widgets(self):
        # Barra de pesquisa
        self.search_input = ctk.CTkEntry(self, placeholder_text="Buscar...", height=25, textvariable=self.texto_pesquisa)
        self.search_input.pack(side="left", fill="x", expand=True, padx=10)
        
        # Botão Adicionar
        self.add_button = ctk.CTkButton(
            self, text="Adicionar", height=30, width=50, 
            command=self.ao_adicionar if self.ao_adicionar else None  # Chama a função passada como argumento
        )
        self.add_button.pack(side="left", padx=10)
        
        # Botão Deletar
        self.delete_button = ctk.CTkButton(self, text="Deletar", height=30, width=50, command=self.comando_excluir)  # Placeholder command
        self.delete_button.pack(side="left", padx=10)


    def ao_digitar(self, *args):
        termo = self.texto_pesquisa.get()
        
        # Se o campo estiver vazio, você pode optar por mostrar todos ou nenhum
        if not termo.strip():
            # Exemplo: limpa a tela se não tiver nada digitado
            self.atualizar_interface(lista_usuarios=bancoCarregado())
            return

        # Chama a SUA função passando o que o usuário digitou
        usuarios_filtrados = PesquisarUser(termo)
        
        # Atualiza a interface com os usuários que sua função encontrou
        self.atualizar_interface(lista_usuarios=usuarios_filtrados)
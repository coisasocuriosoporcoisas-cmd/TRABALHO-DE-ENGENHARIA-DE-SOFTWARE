import customtkinter as ctk
from UI.TopBar import TopBar
from UI.Card import PessoaCard
from function import bancoCarregado, CadastraCliente, ExcluirUsuario, criarAlerta

# Configuração global de aparência
ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    #Janela principal da aplicação.
    def __init__(self):
        super().__init__()
        
        # Configurações da Janela
        self.title("Cadastro de Pessoas")
        self.largura = 1080
        self.altura = 720
        self._centralizar_janela()

        # Criar os componentes da interface
        self._inicializar_ui()
        self._carregar_dados(bancoCarregado())  # Carrega os dados do arquivo JSON

    def _centralizar_janela(self):
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        
        posicao_x = int((largura_tela / 2) - (self.largura / 2))
        posicao_y = int((altura_tela / 2) - (self.altura / 2))
        
        self.geometry(f"{self.largura}x{self.altura}+{posicao_x}+{posicao_y}")

    def _inicializar_ui(self):
        # 1. Barra Superior (passando o método de criar registro como callback)
        self.top_bar = TopBar(self, comando_excluir=self.excluir_usuario, ao_adicionar=self.novo_registro, atualizar_interface=self.atualizar_interface)
        self.top_bar.pack(fill="x", side="top", padx=0, pady=0)
        
        # 2. Container de dados rolável
        self.content_container = ctk.CTkScrollableFrame(self)
        self.content_container.pack(fill="both", expand=True)

    def novo_registro(self):
        # Cria uma camada (overlay) simulando um modal.
        # Usando a cor hexadecimal correta para transparência no CTk (#RRGGBBAA)
        frame_overlay = ctk.CTkFrame(self, fg_color="#1a1a1a")
        frame_overlay.lift()
        frame_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        Modal = ctk.CTkFrame(frame_overlay, fg_color="#242424", corner_radius=10)
        Modal.place(relx=0.5, rely=0.5, anchor="center")

        #campo de nome
        label_name = ctk.CTkLabel(Modal, text="Nome:")
        label_name.pack(pady=(20, 5), padx=20)
        entry_name = ctk.CTkEntry(Modal)
        entry_name.pack(pady=(0, 20), padx=20)

        #campo de cpf
        label_cpf = ctk.CTkLabel(Modal, text="CPF:")
        label_cpf.pack(pady=(0, 5), padx=20)
        entry_cpf = ctk.CTkEntry(Modal)
        entry_cpf.pack(pady=(0, 20), padx=20)

        #campo de número
        label_number = ctk.CTkLabel(Modal, text="Número:")
        label_number.pack(pady=(0, 5), padx=20)
        entry_number = ctk.CTkEntry(Modal)
        entry_number.pack(pady=(0, 20), padx=20)

        #campo email
        label_email = ctk.CTkLabel(Modal, text="Email:")
        label_email.pack(pady=(0, 5), padx=20)
        entry_email = ctk.CTkEntry(Modal)
        entry_email.pack(pady=(0, 20), padx=20)

        # Botão de salvar
        save_button = ctk.CTkButton(Modal, text="Salvar", command=lambda: self.get_dado(entry_cpf, entry_name, entry_number, entry_email, frame_overlay))
        save_button.pack(side="right", pady=20, padx=20)

        # Botão de cancelar
        cancel_button = ctk.CTkButton(Modal, text="Cancelar", command=frame_overlay.destroy)
        cancel_button.pack(side="right", pady=20, padx=20)

    #bagulhete
    def get_dado(self, entry_cpf, entry_name, entry_number, entry_email, frame_overlay):
        CadastraCliente(
            entry_cpf.get(),
            entry_name.get(),
            entry_number.get(),
            entry_email.get(),
            "False",  # Valor padrão para 'perdido'
            master=self
            )
        frame_overlay.destroy()  # Fecha o modal após salvar
        self.atualizar_interface()  # Atualiza a interface para mostrar o novo registro

    def verficar_checkbox(self):
        # Lista para armazenar os CPFs dos usuários selecionados
        cpfs_selecionados = []
        
        # Itera sobre todos os widgets filhos do content_container
        for widget in self.content_container.winfo_children():
            # Verifica se o widget é uma instância de PessoaCard
            if isinstance(widget, PessoaCard):
                # Se o checkbox estiver marcado, adiciona o CPF à lista
                if widget.check_input.get() == 1:  # 1 significa marcado
                    cpfs_selecionados.append(widget.pessoa.get("cpf"))
        
        if not cpfs_selecionados:
            criarAlerta("Nenhum usuário selecionado para exclusão.", "Aviso", master=self)

        print(f"CPFs selecionados para exclusão: {cpfs_selecionados}")  # Para depuração
        return cpfs_selecionados  # Retorna a lista de CPFs selecionados

    def excluir_usuario(self):
        cpfs = self.verficar_checkbox()
        print(f"Excluindo usuários")
        if cpfs:
            for cpf in cpfs:
                ExcluirUsuario(cpf)
            self.atualizar_interface()  # Atualiza a interface após a exclusão
            print(f"Usuários com CPFs {cpfs} foram excluídos com sucesso.")
        else:
            criarAlerta("Nenhum usuário selecionado para exclusão.", "Aviso", master=self)

    def atualizar_interface(self, lista_usuarios=None):
        # Limpa o container de dados
        print("Atualizando interface...")
        for widget in self.content_container.winfo_children():
            widget.destroy()
        # Recarrega os dados do arquivo JSON
        if lista_usuarios is None:
            self._carregar_dados(bancoCarregado())
        else:
            self._carregar_dados(lista_usuarios)

    def _carregar_dados(self, dados):
        for i, dado in enumerate(dados):
            dado = {
                "cpf": dado.get("cpf"),
                "name": dado.get("nome"),
                "number": dado.get("telefone"),
                "email": dado.get("email"),
                "perdido": dado.get("perdido")
            }
            # Instancia o card passando o container e os dados
            card = PessoaCard(self.content_container, dado)
            card.pack(fill="x", side="top", padx=50, pady=(0, 5))


if __name__ == "__main__":
    app = App()
    app.mainloop()
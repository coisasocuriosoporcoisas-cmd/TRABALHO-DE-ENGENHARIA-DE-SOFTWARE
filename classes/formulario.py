import customtkinter as   ctk
import  function  as fc

class FormularioCadastra(ctk.CTkFrame):
    def __init__(self, telaPrincipal):
        super().__init__(telaPrincipal)
        # ENTRADAS E TEXTOS
        self.TextoCpf = ctk.CTkLabel(self, text="Informe seu CPF ABAIXO")
        self.TextoCpf.pack(pady=20,padx=20)
        self.entraCpf = ctk.CTkEntry(self,placeholder_text="Insira o seu Cpf ")
        self.entraCpf.pack(pady=20, padx=20)

        self.TextoNome = ctk.CTkLabel(self, text="Informe seu Nome")
        self.TextoNome.pack(pady=20,padx=20)
        self.entradaNome = ctk.CTkEntry(self, placeholder_text="Insira o seu Nome")
        self.entradaNome.pack(pady=20, padx=20)

        self.TextoTelefone = ctk.CTkLabel(self,text="informe o número de telefone")
        self.TextoTelefone.pack(pady=20,padx=20)
        self.EntradaTelefone = ctk.CTkEntry(self, placeholder_text="telefone")
        self.EntradaTelefone.pack(pady=20,padx=20)
        
        self.TextoEmail = ctk.CTkLabel(self, text="Abaixo adicione o email da pessoa")
        self.TextoEmail.pack(pady=20, padx=20)
        self.Entradaemail = ctk.CTkEntry(self, placeholder_text="email")
        self.Entradaemail.pack(pady=20, padx=20)

        self.OpcaoPedido = ctk.CTkOptionMenu(self, values=["True","False"])
        self.OpcaoPedido.pack()
        self.OpcaoPedido.set("Situação, o cliente pediou algo ?")

        self.Enviar = ctk.CTkButton(self,text="enviar", command=self.PegarCampos)
        self.Enviar.pack(pady=20,padx=20)
    def PegarCampos(self):
        cpf_digitado = self.entraCpf.get()
        nomeUser = self.entradaNome.get()
        telefone = self.EntradaTelefone.get()
        email = self.Entradaemail.get()
        pedido = self.OpcaoPedido.get()
        #pega a janela principal que está rederizando o frame.
        master = self.winfo_toplevel()

        fc.CadastraCliente(cpf_digitado,nomeUser,telefone,email,pedido,fc.ArquivoJson,master)



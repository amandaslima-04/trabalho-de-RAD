import tkinter as tk
from tkinter import messagebox
from funcoes_bd import LoginFunctions


class NovoUsuario:
    def __init__(self, root) -> None:
        """Inicializa a janela para cadastrar um novo usuário.

        Args:
            root (tk.Tk): A janela principal da aplicação.
        """
        self.root = root
        self.root.title('Cadastrar Novo Usuário')
        self.root.geometry('400x200')
        self.root.resizable(False, False)
        self.root.grab_set()

        tk.Label(self.root, text="Insira os dados para cadastrar o novo usuário").pack(pady=10)

        tk.Label(self.root, text="Usuário:").pack(pady=5)
        self.entry_usuario = tk.Entry(self.root, width=30)
        self.entry_usuario.pack()

        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show="*", width=30)
        self.entry_senha.pack()

        tk.Button(self.root, text="Cadastrar", bg="#77cff2", command=self.tentar_cadastrar_usuario).pack(pady=20)
            

    def cadastrar_usuario(self) -> None:
        """Função para cadastrar o novo usuário."""
        nome = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if LoginFunctions.novo_usuario(nome, senha):
            self.root.destroy()  


    def tentar_cadastrar_usuario(self) -> None:
        """Valida se a entrada para registrar um novo usuário é valida."""
        login_user = self.entry_usuario.get()
        senha_user = self.entry_senha.get()

        if not login_user or not senha_user:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        if len(login_user) < 3:
            messagebox.showerror("Erro", "Nome deve conter ao menos três caracteres!")
            return
        if len(senha_user) < 3:
            messagebox.showerror("Erro", "Senha deve conter ao menos três caracteres!")
            return
        else:
            self.cadastrar_usuario()


class TelaLogin:
    def __init__(self, root) -> None:
        """Inicializa a janela de login.

        Args:
            root (tk.Tk): A janela principal da aplicação.
        """
        self.root = root
        self.root.title('Login')
        self.root.geometry('400x200')
        self.root.resizable(False, False)

        tk.Label(self.root, text="Usuário:").pack(pady=10)
        self.entry_usuario = tk.Entry(self.root, width=30)
        self.entry_usuario.pack()

        tk.Label(self.root, text="Senha:").pack(pady=10)
        self.entry_senha = tk.Entry(self.root, show="*", width=30)
        self.entry_senha.pack()

        botao_frame = tk.Frame(self.root)
        botao_frame.pack(pady=20)

        tk.Button(botao_frame, text="Login", command=self.fazer_login, bg="lightgreen").pack(side="left", padx=(0, 10))
        tk.Button(botao_frame, text="Cadastrar novo usuário", command=self.abrir_cadastro, bg="yellow").pack(side="left")


    def abrir_cadastro(self) -> None:
        """Abre a tela de cadastro de novo usuário."""
        NovoUsuario(tk.Toplevel(self.root))  


    def fazer_login(self) -> None:
        """Função para verificar as credenciais do login no banco de dados."""
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if LoginFunctions.verificacao_login(usuario, senha):
            self.root.destroy()
            from main import TelaPrincipal
            TelaPrincipal()
        
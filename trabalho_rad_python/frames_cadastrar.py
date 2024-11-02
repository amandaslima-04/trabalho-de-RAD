import tkinter as tk
from tkinter import messagebox
from funcoes_bd import MainFunctions
from validador_entry import ValidadoresEntrada
from widgets import CriarCampos


class FormularioCadastro:
    """Classe responsável pelo formulário de cadastro de pessoas."""
    def __init__(self, root) -> None:
        """Inicializa o formulário de cadastro.

        Args:
            root (tk.Tk): 
        """
        self.root = root
        self.frame_principal = tk.Frame(root, width=845)
        self.frame_principal.pack(side="right", fill="both", expand=True)
        self.frame_campos = tk.Frame(self.frame_principal, width=845)
        self.frame_campos.grid(row=2, column=0, pady=10)  
        self.criar_campos = CriarCampos(self)

        self.criar_campos.criar_label(self.frame_campos, "Cadastrar Pessoa", column=2, columnspan=6)
        self.entry_nome = self.criar_campos.criar_nome(self.frame_campos)
        self.entry_numero = self.criar_campos.criar_numero(self.frame_campos)
        self.entry_cpf = self.criar_campos.criar_cpf(self.frame_campos)
        self.entry_email = self.criar_campos.criar_email(self.frame_campos)
        self.entry_dia, self.entry_mes, self.entry_ano = self.criar_campos.criar_data_nascimento(self.frame_campos)
        self.criar_campos.criar_botao(self.frame_campos, "Salvar", self.salvar_cadastro, column=2, columnspan=6) 
    

    def tentar_validar_data(self) -> bool:
        """Valida a data de nascimento informada pelo usuário.

        Returns:
            bool: True se a data for válida, False caso contrário.
        """
        dia = self.entry_dia.get()
        mes = self.entry_mes.get()
        ano = self.entry_ano.get()
        data_nascimento = f"{dia.zfill(2)}/{mes.zfill(2)}/{ano}"

        return ValidadoresEntrada.data_valida(data_nascimento)


    def salvar_cadastro(self) -> None:
        """Salva o cadastro com os dados informados e verifica se todos os campos estão preenchidos corretamente."""
        nome = self.entry_nome.get()
        numero = self.entry_numero.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        dia = self.entry_dia.get()
        mes = self.entry_mes.get()
        ano = self.entry_ano.get()

        if not nome or not numero or not cpf or not email:
            messagebox.showerror("Erro", "Por favor preencha todos os campos!")
            return
        if len(numero) < 11:
            messagebox.showerror("Erro", "O número deve ter pelo menos 11 caracteres.")
            return
        if len(cpf) < 11:
            messagebox.showerror("Erro", "O CPF deve ter exatamente 11 dígitos.")
            return
        if "@" not in email or "." not in email:
            messagebox.showerror("Erro", "Email inválido!")
            return
        if not self.tentar_validar_data():  
            messagebox.showerror("Erro", "Data de nascimento inválida!")
            return

        MainFunctions.salvar_cadastro(nome, numero, cpf, email, f"{dia.zfill(2)}/{mes.zfill(2)}/{ano}")

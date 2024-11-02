import tkinter as tk
from tkinter import messagebox
from funcoes_bd import MainFunctions
from widgets import CriarCampos
from validador_entry import ValidadoresEntrada


class FormularioEdicao:
    """Classe que representa o formulário de edição de cadastros."""
    def __init__(self, root) -> None:
        """Inicializa o formulário de edição de cadastro.

        Args:
            root (tk.Tk): 
        """
        self.frame = tk.Frame(root, width=845)
        self.frame.pack(side="right", fill="both", expand=True)
        self.frame_campos = tk.Frame(self.frame)
        self.frame_campos.grid(pady=20)
        self.criar_campos = CriarCampos(self)

        self.criar_campos.criar_label(self.frame_campos, "Editar Cadastro", column=2, columnspan=6)
        self.combobox = self.criar_campos.criar_combobox(self.frame_campos)
        self.combobox.bind("<<ComboboxSelected>>", self.carregar_dados_para_edicao)
        self.entry_nome = self.criar_campos.criar_nome(self.frame_campos)
        self.entry_numero = self.criar_campos.criar_numero(self.frame_campos)
        self.entry_cpf = self.criar_campos.criar_cpf(self.frame_campos)
        self.entry_email = self.criar_campos.criar_email(self.frame_campos)
        self.entry_dia, self.entry_mes, self.entry_ano = self.criar_campos.criar_data_nascimento(self.frame_campos)
        self.criar_campos.criar_botao(self.frame_campos, "Salvar Edição", self.salvar_edicao, column=2, columnspan=6) 
    
        self.carregar_cpfs()


    def carregar_cpfs(self) -> None:
        """Carrega os CPFs dos usuários cadastrados e os exibe na caixa de seleção."""
        registros = MainFunctions.ler_pessoas()
        cpfs_nomes = [f"{registro[1]} - {registro[3]}" for registro in registros]  
        self.combobox['values'] = cpfs_nomes


    def carregar_dados_para_edicao(self, event) -> None:
        """Carrega os dados do cadastro selecionado na caixa de seleção.

        Args:
            event: O evento de seleção do Combobox.
        """
        selecionado = self.combobox.get()
        cpf_selecionado = selecionado.split(" - ")[1]

        registros = MainFunctions.ler_pessoas()
        for registro in registros:
            if registro[3] == cpf_selecionado:
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, registro[1])
                self.entry_numero.delete(0, tk.END)
                self.entry_numero.insert(0, registro[2])
                self.entry_cpf.delete(0, tk.END)
                self.entry_cpf.insert(0, registro[3])
                self.entry_email.delete(0, tk.END)
                self.entry_email.insert(0, registro[4])
                data_nascimento = registro[5]  
                dia, mes, ano = data_nascimento.split('/')  
                self.entry_dia.delete(0, tk.END)  
                self.entry_dia.insert(0, dia)
                self.entry_mes.delete(0, tk.END)  
                self.entry_mes.insert(0, mes)
                self.entry_ano.delete(0, tk.END)  
                self.entry_ano.insert(0, ano)
                return

        messagebox.showerror("Erro", "Cadastro não encontrado.")


    def tentar_validar_data(self) -> bool:
        """Valida a data de nascimento.

        Returns:
            bool: True se a data for válida, False caso contrário.
        """        
        novo_dia = self.entry_dia.get()
        novo_mes = self.entry_mes.get()
        novo_ano = self.entry_ano.get()
        nova_data_nascimento = f"{novo_dia.zfill(2)}/{novo_mes.zfill(2)}/{novo_ano}"

        return ValidadoresEntrada.data_valida(nova_data_nascimento)


    def salvar_edicao(self):
        """Salva as edições no cadastro com validação de todos os campos."""
        novo_nome = self.entry_nome.get()
        novo_numero = self.entry_numero.get()
        novo_cpf = self.entry_cpf.get()
        novo_email = self.entry_email.get()
        novo_dia = self.entry_dia.get()
        novo_mes = self.entry_mes.get()
        novo_ano = self.entry_ano.get()
        
        if not novo_nome or not novo_numero or not novo_cpf or not novo_email:
            messagebox.showerror("Erro", "Por favor preencha todos os campos!")
            return
        if len(novo_numero) < 11:
            messagebox.showerror("Erro", "O número deve ter pelo menos 11 caracteres.")
            return
        if len(novo_cpf) < 11:
            messagebox.showerror("Erro", "O CPF deve ter exatamente 11 dígitos.")
            return
        if "@" not in novo_email or "." not in novo_email:
            messagebox.showerror("Erro", "Email inválido!")
            return
        if not self.tentar_validar_data():  
            messagebox.showerror("Erro", "Data de nascimento inválida!")
            return

        cpf_selecionado = self.combobox.get().split(" - ")[1]
        MainFunctions.editar_pessoa(cpf_selecionado, novo_nome, novo_numero, novo_email, f"{novo_dia.zfill(2)}/{novo_mes.zfill(2)}/{novo_ano}")
        messagebox.showinfo("Edição", "Cadastro atualizado com sucesso!")
        self.frame.destroy()
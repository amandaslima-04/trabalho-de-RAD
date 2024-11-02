import tkinter as tk
from tkinter import messagebox, ttk
from funcoes_bd import MainFunctions

class ExcluirFormulario:
    """Classe que representa o formulário para exclusão de cadastros."""
    def __init__(self, root) -> None:
        """Inicializa o formulário de exclusão de cadastro.

        Args:
            root (tk.Tk): 
        """
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Excluir Cadastro").pack(pady=30)

        tk.Label(self.frame, text="Selecionar Usuário:").pack(pady=5)
        self.combobox = ttk.Combobox(self.frame, state="readonly")
        self.combobox.pack(pady=5)
        self.combobox.bind("<<ComboboxSelected>>", self._carregar_dados)


        tk.Button(self.frame, text="Excluir", command=self.tentar_excluir_pessoa).pack(pady=20)

        self._carregar_cpfs_nomes()  


    def _carregar_cpfs_nomes(self):
        """Carrega os CPFs e Nomes dos usuários cadastrados para o Combobox."""
        registros = MainFunctions.ler_pessoas() 
        cpfs_nomes = [f"{registro[1]} - {registro[3]}" for registro in registros] 
        self.combobox['values'] = cpfs_nomes


    def _carregar_dados(self, event):
        """Carrega os dados do cadastro selecionado no Combobox.

        Args:
            event: O evento de seleção do Combobox.
        """
        selecionado = self.combobox.get()
        if selecionado:
            nome_selecionado = selecionado.split(" - ")[0]
            print(f"Usuário selecionado: {nome_selecionado}")  


    def tentar_excluir_pessoa(self):
        """Tenta excluir a pessoa selecionada no Combobox."""
        selecionado = self.combobox.get()
        if not selecionado:
            messagebox.showwarning("Atenção", "Por favor, selecione um usuário.")
            return

        nome_selecionado = selecionado.split(" - ")[0]
        cpf_selecionado = selecionado.split(" - ")[1]

        confirmacao = messagebox.askyesno("Confirmação", f"Deseja realmente excluir {nome_selecionado}?")
        if confirmacao:
            MainFunctions.excluir_pessoa(cpf_selecionado)  

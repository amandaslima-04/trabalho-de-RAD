import tkinter as tk
from tkinter import ttk
from validador_entry import ValidadoresEntrada


class CriarCampos:
    """Cria os campos de entrada do formulário com validação."""
    def __init__(self, formulario) -> None:
        self.validadores = ValidadoresEntrada()
        self.formulario = formulario   
            
        formulario.frame_campos.grid_columnconfigure(0, minsize=100)
            

    def criar_nome(self, frame) -> tk.Entry:
        """Cria um campo de entrada para o nome.

        Args:
            frame (tk.Frame): O frame onde o campo será inserido.
        """        
        tk.Label(frame, text="Nome:").grid(row=2, column=1, padx=10, pady=10, sticky="e")
        self.formulario.entry_nome = tk.Entry(frame, width=10, validate="key",
            validatecommand=(frame.register(self.validadores.validar_nome), "%P"))
        self.formulario.entry_nome.grid(row=2, column=2, columnspan=6, padx=10, pady=10, sticky="nsew")
        return self.formulario.entry_nome


    def criar_numero(self, frame) -> tk.Entry:
        """Cria um campo de entrada para o número.

        Args:
            frame (tk.Frame): O frame onde o campo será inserido.
        """        
        tk.Label(frame, text="Número:").grid(row=3, column=1, padx=10, pady=10, sticky="e")
        self.formulario.entry_numero = tk.Entry(frame, width=5, validate="key",
            validatecommand=(frame.register(self.validadores.validar_numero), "%P"))
        self.formulario.entry_numero.grid(row=3, column=2, columnspan=6, padx=10, pady=10, sticky="nsew")
        return self.formulario.entry_numero


    def criar_cpf(self, frame) -> tk.Entry:
        """Cria um campo de entrada para o CPF.

        Args:
            frame (tk.Frame): O frame onde o campo será inserido.
        """ 
        tk.Label(frame, text="CPF:").grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.formulario.entry_cpf = tk.Entry(frame, width=10, validate="key",
            validatecommand=(frame.register(self.validadores.validar_cpf), "%P"))
        self.formulario.entry_cpf.grid(row=4, column=2, columnspan=6, padx=10, pady=10, sticky="nsew")
        return self.formulario.entry_cpf


    def criar_email(self, frame) -> tk.Entry:
        """Cria um campo de entrada para o email.

        Args:
            frame (tk.Frame): O frame onde o campo será inserido.
        """        
        tk.Label(frame, text="Email:").grid(row=5, column=1, padx=10, pady=10, sticky="e")
        self.formulario.entry_email = tk.Entry(frame, width=10)
        self.formulario.entry_email.grid(row=5, column=2, columnspan=6,  padx=10, pady=10, sticky="nsew")
        return self.formulario.entry_email


    def criar_data_nascimento(self, frame) -> tuple:
        """Cria campos de entrada para a data de nascimento.

        Args:
            frame (tk.Frame): O frame onde os campos serão inseridos.
        """        
        tk.Label(frame, text="Data de Nascimento\n(DD/MM/AAAA)").grid(row=6, column=1, sticky="s")
        self.formulario.entry_dia = tk.Entry(frame, width=5, validate="key",
            validatecommand=(frame.register(self.validadores.validar_dia), "%P"))
        self.formulario.entry_dia.grid(row=6, column=2, padx=(10,0), pady=10, sticky="nsew")

        tk.Label(frame, text="/").grid(row=6, column=3, sticky="nsew")
        self.formulario.entry_mes = tk.Entry(frame, width=5, validate="key",
            validatecommand=(frame.register(self.validadores.validar_mes), "%P"))
        self.formulario.entry_mes.grid(row=6, column=4, padx=(0,0), pady=10, sticky="nsew")

        tk.Label(frame, text="/").grid(row=6, column=5, sticky="nsew")
        self.formulario.entry_ano = tk.Entry(frame, width=10, validate="key",
            validatecommand=(frame.register(self.validadores.validar_ano), "%P"))
        self.formulario.entry_ano.grid(row=6, column=6, padx=(0,0), pady=10, sticky="nsew")

        return self.formulario.entry_dia, self.formulario.entry_mes, self.formulario.entry_ano


    def criar_combobox(self, frame) -> ttk.Combobox:
        """Cria uma combobox para selecionar CPF.

        Args:
            frame (tk.Frame): O frame onde a combobox será inserida.
        """        
        tk.Label(frame, text="Selecionar CPF:").grid(row=1, column=1, padx=10, pady=10, sticky="e")  
        self.formulario.combobox = ttk.Combobox(frame)
        self.formulario.combobox.grid(row=1, column=2, columnspan=6, padx=10, pady=10, sticky="nsew")
        return self.formulario.combobox


    def criar_botao(self, frame, text, command, column, columnspan, **kwargs) -> tk.Button:
        """Cria um botão com texto e comando personalizados.

        Args:
            frame (tk.Frame): O frame onde o botão será inserido.
            text (str): O texto do botão.
            command (callable): A função que será chamada ao clicar no botão.
            column (int): A coluna onde o botão será inserido.
            columnspan (int): O número de colunas que o botão deve ocupar.
            **kwargs: Outros argumentos para o botão.
        """        
        botao = tk.Button(frame, text=text, command=command, **kwargs)
        botao.grid(row=8, column=column, columnspan=columnspan, pady=10, sticky="nsew")  
        return botao
    

    def criar_label(self, frame, text, columnspan, column, **kwargs) -> tk.Label:
        """Cria um label com texto personalizado.

        Args:
            frame (tk.Frame): O frame onde o label será inserido.
            text (str): O texto do label.
            columnspan (int): O número de colunas que o label deve ocupar.
            column (int): A coluna onde o label será inserido.
            **kwargs: Outros argumentos para o label.
        """        
        label = tk.Label(frame, text=text, **kwargs)
        label.grid(row=0, column=column, columnspan=columnspan, padx=10, pady=30, sticky="nsew")
        return label
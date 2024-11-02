import tkinter as tk
from frames_cadastrar import FormularioCadastro
from frame_editar import FormularioEdicao
from frame_excluir import ExcluirFormulario
from tela_login import TelaLogin
from frame_historico import FrameHistorico


class TelaPrincipal:
    """classe que gerencia tela principal e a navegação
    entre diferentes frames, como cadastro, edição e exclusão.
    """
    def __init__(self) -> None:
        """Inicializa a tela principal da aplicação.

        Cria a janela principal e a barra lateral de navegação.
        """
        self.root = tk.Tk()
        self.root.title('Tela de Cadastro')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        self.criar_sidebar()
        self.root.mainloop()

    def criar_sidebar(self) -> None:
        """Cria a barra lateral com os botões de navegação."""
        sidebar_frame = tk.Frame(self.root, width=200, bg="#3b1c21", name='sidebar_frame')
        sidebar_frame.pack(side="left", fill="y")
        sidebar_frame.pack_propagate(False)

        botao_novo_cadastro = tk.Button(sidebar_frame, text='Novo Cadastro', command=self.abrir_novo_cadastro, width=25)
        botao_novo_cadastro.pack(pady=25)

        botao_editar_dados = tk.Button(sidebar_frame, text='Editar Cadastro', command=self.abrir_editar_dados, width=25)
        botao_editar_dados.pack(pady=25)

        botao_excluir_dados = tk.Button(sidebar_frame, text='Excluir Cadastro', command=self.abrir_excluir_cadastro, width=25)
        botao_excluir_dados.pack(pady=25)

        botao_historico = tk.Button(sidebar_frame, text='Histórico', command=self.abrir_historico, width=25)
        botao_historico.pack(pady=25)

    def abrir_historico(self) -> None:
        """Limpa a tela e exibe o frame de histórico."""
        self.limpar_tela()
        FrameHistorico(self.root)


    def limpar_tela(self) -> None:
        """Remove todos os widgets da tela exceto a sidebar."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_name() != 'sidebar_frame':
                widget.destroy()


    def abrir_novo_cadastro(self) -> None:
        """Limpa a tela e exibe o formulário de novo cadastro."""
        self.limpar_tela()
        FormularioCadastro(self.root)


    def abrir_editar_dados(self) -> None:
        """Limpa a tela e exibe o formulário de edição de dados."""
        self.limpar_tela()
        FormularioEdicao(self.root)


    def abrir_excluir_cadastro(self) -> None:
        """Limpa a tela e exibe o formulário de exclusão de usuário."""
        self.limpar_tela()
        ExcluirFormulario(self.root)  

    
    def abrir_historico(self) -> None:
        """Limpa a tela e exibe o frame de histórico."""
        self.limpar_tela()
        FrameHistorico(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    TelaLogin(root)
    root.mainloop()
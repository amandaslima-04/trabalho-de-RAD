import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class FrameHistorico:
    """Classe que representa o frame para exibição do histórico de alterações."""
    def __init__(self, root) -> None:
        """Inicializa o frame de histórico.

        Args:
            root (tk.Tk): 
        """
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill='both', expand=True)

        tk.Label(self.frame, text="Histórico de Alterações").pack(pady=30)

        
        self.text_area = scrolledtext.ScrolledText(self.frame, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)

        
        tk.Button(self.frame, text="Atualizar Pagina", command=self.carregar_historico).pack(pady=5)

       
        self.carregar_historico()


    def carregar_historico(self) -> None:
        """Carrega e exibe o histórico de alterações a partir do arquivo .txt."""
        try:
            with open('historico.txt', 'r') as file:
                self.text_area.delete(1.0, tk.END)  
                self.text_area.insert(tk.END, file.read())  
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "Arquivo de histórico não encontrado.")
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "Nenhum histórico encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o histórico: {e}")
from tkinter import messagebox
import sqlite3


class LoginFunctions:
    """Classe responsavel pelas funções relacionadas ao processo de login"""    
    def verificacao_login(usuario: str, senha: str) -> bool:
        """Verifica se o login existe no banco de dados."""
        try:
            conexao = sqlite3.connect('lista_usuarios.db')
            cursor = conexao.cursor()
            cursor.execute('SELECT senha FROM usuario WHERE nome = ?', (usuario,))
            resultado = cursor.fetchone()  

            if resultado:  
                senha_armazenada = resultado[0]  
                return senha_armazenada == senha  
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorreto.\nTente novamente!")
                return False
        except sqlite3.OperationalError as e:
            if "no such table: usuario" in str(e):
                messagebox.showerror("Erro", "Usuário não cadastrado!")
        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            return False  
        finally:
            conexao.close()


    def novo_usuario(nome: str, senha: str) -> bool:
        """Cadastra um novo usuário no banco de dados.

        Args:
            nome (str): Nome do usuário a ser cadastrado.
            senha (str): Senha do usuário a ser cadastrada.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            conexao = sqlite3.connect('lista_usuarios.db')
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,  -- Adicionado UNIQUE para evitar duplicatas
                    senha TEXT NOT NULL
                )
                ''')
            cursor.execute('INSERT INTO usuario (nome, senha) VALUES (?, ?)', (nome, senha))
            conexao.commit()
            messagebox.showinfo("Usuário", "Usuário salvo com sucesso!")
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Usuário já cadastrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar cadastro: {e}")
        finally:
            conexao.close()


class MainFunctions:
    def salvar_cadastro(nome: str, numero: str, cpf: str, email: str, data_nascimento: str) -> None:
        """Salva os dados do cadastro no banco de dados.

        Args:
            nome (str): Nome da pessoa a ser cadastrada.
            numero (str): Número de telefone da pessoa.
            cpf (str): CPF da pessoa, que deve ser único.
            email (str): Email da pessoa.
            data_nascimento (str): Data de nascimento da pessoa no formato 'DD/MM/AAAA'.
        """
        try:
            conexao = sqlite3.connect("ficha_pessoa.db")
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    numero TEXT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL,
                    data_nascimento DATE NOT NULL
                );
                """)
            cursor.execute("INSERT INTO pessoa (nome, numero, cpf, email, data_nascimento) VALUES (?, ?, ?, ?, ?)",
                           (nome, numero, cpf, email, data_nascimento))
            conexao.commit()
            messagebox.showinfo("Cadastro", "Cadastro salvo com sucesso!")

            MainFunctions.registrar_historico(f"Cadastro: {nome}, CPF: {cpf}, Data: {data_nascimento}")

        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "CPF já cadastrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar cadastro: {e}")
        finally:
            conexao.close()


    def ler_pessoas() -> list:
        """Lê todas as pessoas cadastradas no banco de dados."""
        conexao = sqlite3.connect("ficha_pessoa.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pessoa")
        registros = cursor.fetchall()
        conexao.close()
        return registros


    def editar_pessoa(cpf: str, novo_nome: str, novo_numero: str, novo_email: str, nova_data_nascimento: str) -> None:
        """Edita os dados de uma pessoa no banco de dados.

        Args:
            cpf (str): CPF da pessoa a ser editada.
            novo_nome (str): Novo nome da pessoa.
            novo_numero (str): Novo número de telefone da pessoa.
            novo_email (str): Novo email da pessoa.
            nova_data_nascimento (str): Nova data de nascimento da pessoa no formato 'DD/MM/AAAA'.
        """
        try:
            conexao = sqlite3.connect("ficha_pessoa.db")
            cursor = conexao.cursor()
            cursor.execute(""" 
                UPDATE pessoa
                SET nome = ?, numero = ?, email = ?, data_nascimento = ?
                WHERE cpf = ?
            """, (novo_nome, novo_numero, novo_email, nova_data_nascimento, cpf))
            conexao.commit()

            MainFunctions.registrar_historico(f"Edição: {novo_nome}, CPF: {cpf}")

        except Exception as e:
            messagebox.showerror("Erro", "Cadastro não encontrado.")
        finally:
            conexao.close()


    def excluir_pessoa(cpf: str) -> None:
        """Exclui uma pessoa da tabela 'pessoa' com base no CPF.

        Args:
            cpf (str): CPF da pessoa a ser excluída.
        """
        try:
            conexao = sqlite3.connect('ficha_pessoa.db')
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM pessoa WHERE cpf = ?", (cpf,)) 
            if cursor.rowcount > 0:
                conexao.commit()
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                MainFunctions.registrar_historico(f"Exclusão: CPF: {cpf}")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado.")  
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir usuário: {e}")
        finally:
            conexao.close()

    
    def registrar_historico(mensagem: str) -> None:
        """Registra uma mensagem no arquivo de histórico.

        Args:
            mensagem (str): Mensagem a ser registrada no histórico.
        """
        with open('historico.txt', 'a') as file:
            file.write(mensagem + '\n')

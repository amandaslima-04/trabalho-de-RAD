from datetime import datetime


class ValidadoresEntrada:  
    """Classe que sera usada sempre que um frame precisar de validação em sua entradas"""  
    def validar_nome(self, nome) -> bool:
        """Valida o nome para permitir apenas letras e espaço, com no máximo 32 caracteres.

        Args:
            nome (str): O nome a ser validado.
        """
        return (all(c.isalpha() or c.isspace() for c in nome) and len(nome) <= 32) or nome == ""


    def validar_numero(self, numero) -> bool:
        """Valida o número para permitir apenas dígitos e no máximo 11 caracteres.

        Args:
            numero (str): O número a ser validado.
        """
        return (numero.isdigit() and len(numero) <= 11) or numero == ""


    def validar_cpf(self, cpf) -> bool:
        """Valida o CPF para permitir apenas dígitos e no máximo 11 caracteres.

        Args:
            cpf (str): O CPF a ser validado.
        """
        return (cpf.isdigit() and len(cpf) <= 11) or cpf == ""


    def validar_dia(self, dia) -> bool:
        """Valida o dia para permitir apenas dígitos e no máximo 2 caracteres.

        Args:
            dia (str): O dia a ser validado.
        """
        return (dia.isdigit() and len(dia) <= 2) or dia == ""


    def validar_mes(self, mes) -> bool:
        """Valida o mês para permitir apenas dígitos e no máximo 2 caracteres.

        Args:
            mes (str): O mês a ser validado.
        """
        return (mes.isdigit() and len(mes) <= 2) or mes == ""


    def validar_ano(self, ano) -> bool:
        """Valida o ano para permitir apenas dígitos e no máximo 4 caracteres.

        Args:
            ano (str): O ano a ser validado.
        """
        return (ano.isdigit() and len(ano) <= 4) or ano == ""
    
    
    def data_valida(data_nascimento) -> bool:
        """Verifica se a data de nascimento é válida.

        Args:
            data_nascimento (str): A data de nascimento a ser verificada no formato 'DD/MM/AAAA'.
        """
        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            ano_atual = datetime.now().year
            return 1900 <= data.year <= ano_atual
        except ValueError:
            return False
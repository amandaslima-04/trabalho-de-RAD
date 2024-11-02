#Sistema de Cadastro no Tkinter

Este é um protótipo de um sistema de cadastro de pessoas, usando Tkinter para a interface gráfica e SQLite como banco de dados.
=====================

Descrição:
-------------------------------------
A aplicação permite as seguintes funcionalidades:

Criar um novo cadastro de pessoa
Editar cadastros realizados
Deletar cadastros por um sistema de busca de CPF
Visualizar o histórico de atividades feitas pelo programa


Como rodar a aplicação:
-------------------------------------
Baixe a pasta com os arquivos .py (todos são necessários) e execute o arquivo main na IDE de sua escolha.

Requisitos:
-------------------------------------
Ter o Python 3.11.9 ou superior instalado

Estrutura do Projeto:
-------------------------------------
O projeto é composto por 8 arquivos:

main: é responsável pela criação da janela principal, onde todo o programa se estrutura.
tela_login: cria uma janela onde é feita a entrada de usuário e senha para gerenciamento de acesso.
Os arquivos frames_: são responsáveis pelas janelas onde o usuário pode interagir com as funcionalidades do programa.
funcoes_db: contém o backend para executar as interações com o banco de dados.
validador_entry: armazena todas as validações de entrada de usuário, facilitando a reutilização por outros módulos.
widgets: armazena botões, labels, entry e combobox, alguns com estilos variáveis para serem reutilizados ao longo do programa.

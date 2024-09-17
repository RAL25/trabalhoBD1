import cx_Oracle
import pandas as pd
import streamlit as st
import asyncio

# finally:
#     # Fechar a conexão
#     # if cursor:
#     #     cursor.close()
#     if connection:
#         connection.close()
 
# teste query simples
# query = """SELECT * FROM PESSOA"""
# pessoa = pd.read_sql(query, conexao)
# print(pessoa)

#------ teste para a funcionalidade do projeto ------#

async def main():
    # Informações da conexão 
    string_conexao = "ral25704/ral25704@200.131.242.43:1521/IFNMGPDB"

    # Estabelecer conexão 
    connection = cx_Oracle.Connection(string_conexao)

    try:
        conexao = cx_Oracle.Connection(string_conexao)
        print('conexão realizada com sucesso')
    except cx_Oracle.DatabaseError as e:
        print(e)
        
    # query = """SELECT * FROM PESSOA"""
    # pessoa = pd.read_sql(query, conexao)
    # print(pessoa)
        
    st.title("Bem vindo ao AvatarSucks")
    
    st.header("Funcionalidades do projeto")
    st.write("Para aplicar a primeira funcionalidade foi selecionado a tabela Espectador")
    
    # st.write(pessoa)
    
    # funcionalidades = ["INSERT", "UPDATE", "SELECT", "DELETE"]
    
    selected_option = st.selectbox("escolha o tipo de manipulção de dados: ", ["Inserir", "atualizar", "listar", "remover"])
    
    if selected_option == "listar":
        input2 = st.text_input("Informe o código")
        espec = pd.read_sql(f"SELECT * FROM ESPECTADOR WHERE CODIGO = {input2}", conexao)
        st.write(espec)

asyncio.run(main())
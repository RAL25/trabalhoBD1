import cx_Oracle
import pandas as pd
import streamlit as st

import func1, func2

# Estabelecer conexão com Oracle
string_conexao = "ral25704/ral25704@200.131.242.43:1521/IFNMGPDB"
connection = cx_Oracle.Connection(string_conexao)
mycursor = connection.cursor()
print("Conectado com sucesso ao banco de dados Oracle!")

class MultiApp:
    def run():
        with st.sidebar:
            func = st.selectbox("Escolha a funcionalidade",("Relação simples","Generalização/Especialização"))
        if func == "Relação simples":
            func1.app(mycursor, connection, pd)
        if func == "Generalização/Especialização":
            func2.main(mycursor, connection, pd)
        

    run()
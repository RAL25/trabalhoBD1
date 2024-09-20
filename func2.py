import streamlit as st
import buscarP

def main(mycursor, connection, pd):
    st.title("Bem vindo ao AvatarSucks")
    
    st.header("Generalização e Especialização")    
    st.subheader("Tabela escolhida: Pessoa")
    option=st.selectbox("Selecione uma operação",("Inserir", "Listar", "Atualizar", "Remover"))
    
    st.header("")
    if option == "Inserir":
        st.subheader("Cadastrar nova pessoa")
        
        nome=st.text_input("Insira um nome")
        ender=st.text_input("Insira um endereço")
        exp=st.radio("Escolha uma especialização:", ["Aluno", "Professor"])
        if exp=="Aluno":
            matricula=st.text_input("Insira o número de matrícula")
            if st.button("Inserir"):
                sql1=f"INSERT INTO APESSOA(NOME,ENDERECO) VALUES('{nome}','{ender}')"
                sql2=f"INSERT INTO ALUNO(NOME_ALUNO,MATRICULA) VALUES('{nome}','{matricula}')"
                mycursor.execute(sql1)
                connection.commit()
                mycursor.execute(sql2)
                connection.commit()
                st.success("Novo aluno cadastrado com sucesso!")
        elif exp=="Professor":
            salario_str=st.text_input("Digite o salário")
            if salario_str:
                salario = float(salario_str)
            else :
                salario = 0
                
            if st.button("Inserir"):
                sql1=f"INSERT INTO APESSOA(NOME,ENDERECO) VALUES('{nome}','{ender}')"
                sql2=f"INSERT INTO APROFESSOR(NOME_PROFESSOR,SALARIO) VALUES('{nome}',{salario})"
                mycursor.execute(sql1)
                connection.commit()
                mycursor.execute(sql2)
                connection.commit()
                st.success("Novo professor cadastrado com sucesso!")
                
                
    elif option == "Listar":
        st.subheader("Listando pessoas")
        
        selec_pessoa = st.selectbox("Selecione qual tipo de pessoa", ("Aluno", "Professor"))
        if selec_pessoa=="Aluno":
            st.subheader("Listando os alunos")
            query = "SELECT * FROM ALUNO"
            aluno = pd.read_sql(query, connection)
            st.write(aluno)
        elif selec_pessoa=="Professor":
            st.subheader("Listando os professores")
            query = "SELECT * FROM APROFESSOR"
            professor = pd.read_sql(query, connection)
            st.write(professor)
            
            
    elif option == "Atualizar":
        st.subheader("Atualizar uma pessoa")
        
        nome=st.text_input("Insira um nome")
        if st.button("Buscar"):
            nome_id = buscarP.buscar_pessoa(nome)
            
            if nome_id == "Aluno":
                endereco = st.text_input("Endereço")
                matricula = st.text_input("Matricula")
                
                if st.button("Atualizar"):
                    buscarP.update_professor_data(nome_id,endereco, matricula)
        
        
        ender=st.text_input("Insira um endereço")
        exp=st.radio("Escolha uma especialização:", ["Aluno", "Professor"])
        if exp=="Aluno":
            matricula=st.text_input("Insira o número de matrícula")
            if st.button("Inserir"):
                sql1=f"INSERT INTO APESSOA(NOME,ENDERECO) VALUES('{nome}','{ender}')"
                sql2=f"INSERT INTO ALUNO(NOME_ALUNO,MATRICULA) VALUES('{nome}','{matricula}')"
                mycursor.execute(sql1)
                connection.commit()
                mycursor.execute(sql2)
                connection.commit()
                st.success("Novo aluno cadastrado com sucesso!")
        elif exp=="Professor":
            salario_str=st.text_input("Digite o salário")
            if salario_str:
                salario = float(salario_str)
            else :
                salario = 0
                
            if st.button("Atualizar"):
                sql1=f"INSERT INTO APESSOA(NOME,ENDERECO) VALUES('{nome}','{ender}')"
                sql2=f"INSERT INTO APROFESSOR(NOME_PROFESSOR,SALARIO) VALUES('{nome}',{salario})"
                mycursor.execute(sql1)
                connection.commit()
                mycursor.execute(sql2)
                connection.commit()
                st.success("Novo professor cadastrado com sucesso!")
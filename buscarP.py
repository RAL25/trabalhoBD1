import streamlit as st

def buscar_pessoa(nome, mycursor):
    # Buscar o pessoa_id pelo nome
    query_pessoa = f"SELECT pessoa_id FROM Pessoa WHERE nome = '{nome}'"
    mycursor.execute(query_pessoa)
    pessoa = mycursor.fetchone()

    if pessoa:
        pessoa_id = pessoa[0]

        # Verificar se é Professor
        query_professor = f"SELECT professor_id FROM Professor WHERE professor_id = '{pessoa_id}'"
        mycursor.execute(query_professor)
        professor = mycursor.fetchone()

        if professor:
            return pessoa_id, 'Professor'
        else:
            # Verificar se é Aluno
            query_aluno = f"SELECT professor_id FROM Professor WHERE professor_id = '{pessoa_id}'"
            mycursor.execute(query_professor)
            aluno = mycursor.fetchone()

            if aluno:
                return pessoa_id, 'Aluno'
            else:
                return pessoa_id, 'Não encontrado'

    else:
        return None, 'Pessoa não encontrada'

# Função para atualizar os dados de Professor
def update_professor_data(pessoa_id, nome, endereco, salario, mycursor, connection):
    
            # Iniciar uma transação
            mycursor.execute("BEGIN")

            # Atualizar os dados genéricos na tabela Pessoa
            update_pessoa_query = """
            UPDATE Pessoa
            SET nome = :nome, endereco = :endereco
            WHERE pessoa_id = :pessoa_id
            """
            mycursor.execute(update_pessoa_query, {'nome': nome, 'endereco': endereco, 'pessoa_id': pessoa_id})

            # Atualizar os dados específicos na tabela Professor
            update_professor_query = """
            UPDATE Professor
            SET salario = :salario
            WHERE professor_id = :pessoa_id
            """
            mycursor.execute(update_professor_query, {'salario': salario, 'pessoa_id': pessoa_id})

            # Commitar as alterações
            connection.commit()

            st.success("Dados do Professor atualizados com sucesso!")
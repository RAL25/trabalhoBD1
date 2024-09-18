import streamlit as st

    #função para buscar o nome e o id 
def buscar_cliente(mycursor):
    mycursor.execute("SELECT ID, NOME FROM CLIENTE")
    clientes = mycursor.fetchall()
    return clientes

def buscar_pedido(mycursor):
    mycursor.execute("SELECT ID, DESCRICAO FROM PEDIDO")
    pedidos = mycursor.fetchall()
    return pedidos

def app(mycursor, connection, pd):
    st.title("Bem vindo ao AvatarSucks")
    
    st.header("Primeira funcionalidade do projeto")    
    st.subheader("Tabela escolhida: Pedido")
    option=st.selectbox("Selecione uma operação",("Inserir", "Listar", "Atualizar", "Remover"))
    
    st.header("")
    if option == "Inserir":
        st.subheader("Inserir um novo pedido")
        
        id=st.text_input("Insira uma nova ID")
        desc=st.text_input("Insira uma descrição")
        valor_str=st.text_input("Insira um valor")
        if valor_str:
            valor = float(valor_str)
        else :
            valor = 0  
        clientes = buscar_cliente(mycursor)
        clientes_dict = {nome: id for id, nome in clientes}
        selec_cliente = st.selectbox("Selecione um cliente associado", list(clientes_dict.keys()))
        id_selecionado = clientes_dict[selec_cliente]
        
        if st.button("Inserir"):
            sql=f"INSERT INTO PEDIDO(ID,DESCRICAO,VALOR,ID_CLIENTE) VALUES('{id}','{desc}',{valor},'{id_selecionado}')"
            mycursor.execute(sql)
            connection.commit()
            st.success("Novo pedido inserido com sucesso!")
            
    
    elif option=="Listar":
        st.subheader("Listando os pedidos")
        query = "SELECT * FROM PEDIDO"
        cliente = pd.read_sql(query, connection)
        st.write(cliente)
    
    
    elif option=="Atualizar":
        st.subheader("Atualizar um pedido")
        
        id=st.number_input("Insira um ID",min_value=1)
        desc=st.text_input("Insira uma descrição")
        valor_str=st.text_input("Insira um valor")
        if valor_str:
            valor = float(valor_str)
        else :
            valor = 0 
        clientes = buscar_cliente(mycursor)
        clientes_dict = {nome: id for id, nome in clientes}
        selec_cliente = st.selectbox("Selecione um cliente associado", list(clientes_dict.keys()))
        id_selecionado = clientes_dict[selec_cliente]
        
        if st.button("Atualizar"):
            sql=f"UPDATE PEDIDO SET DESCRICAO = '{desc}', VALOR = {valor}, ID_CLIENTE = '{id_selecionado}' WHERE ID = '{id}'"
            mycursor.execute(sql)
            connection.commit()
            st.success("Registro atualizado com sucesso!")
            
            
    elif option=="Remover":
        st.subheader("Remover um pedido")
        pedidos = buscar_pedido(mycursor)
        pedidos_dict = {desc: id for id, desc in pedidos}
        selec_pedido = st.selectbox("Selecione um pedido", list(pedidos_dict.keys()))
        id = pedidos_dict[selec_pedido]
        if st.button("Remover"):
            sql=f"DELETE FROM PEDIDO WHERE ID ='{id}'"
            mycursor.execute(sql)
            connection.commit()
            st.success("Pedido removido com sucesso!")
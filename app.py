import streamlit as st
import contrato

def main():
    st.title('SISTEMA DE CRM INICIAL')
    email = st.text_input('inserir email')
    data = st.date_input('inserir data')
    hora = st.time_input('inserir a hora')
    produto = st.selectbox('Escolha o produto',['abacaxi','banana','caqui','damasco'])
    qtt = st.number_input('inserir a quantidade vendida', min_value=0)
    valor = st.number_input('inserir o valor unitário', min_value=0.0)
    
    if st.button('Salvar'):
        st.write('*** Dados da venda ***')
        st.write(f'email do vendedor: {email}')
        st.write(f'Data e Hora da Compra: {data} - {hora}')
        st.write(f'Pedido: {qtt} de {produto} a BRL {valor:.2f} | Total de BRL {qtt*valor:.2f}')


if __name__ == "__main__":
    main()
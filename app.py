import streamlit as st
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    st.title('SISTEMA DE CRM INICIAL')
    email = st.text_input('inserir email')
    dia = st.date_input('inserir data')
    hora = st.time_input('inserir a hora')
    produto = st.selectbox('Escolha o produto',['abacaxi','banana','caqui','damasco'])
    qtt = st.number_input('inserir a quantidade vendida', min_value=0)
    valor = st.number_input('inserir o valor unitário', min_value=0.0)
    
    if st.button('Salvar'):
        try:
            venda = Vendas(
                email = email, 
                dia = dia, 
                hora = hora, 
                produto = produto, 
                qtt = qtt, 
                valor = valor)
            st.write('*** Dados da venda ***')
            st.write(f'email do vendedor: {email}')
            st.write(f'Data e Hora da Compra: {dia} - {hora}')
            st.write(f'Pedido: {qtt} de {produto} a BRL {valor:.2f} | Total de BRL {qtt*valor:.2f}')
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(f'DEU ERRO! {e}')       



if __name__ == "__main__":
    main()
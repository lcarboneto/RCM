import streamlit as st
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
            venda = (email, dia, hora, produto, qtt, valor)
            st.write('*** Dados da venda ***')
            st.write(venda)            
            salvar_no_postgres(venda)
            
        except ValidationError as e:
            st.error(f'DEU ERRO! {e}')    
         



if __name__ == "__main__":
    main()
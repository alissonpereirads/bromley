import streamlit as st
from chain.chain_question import chain_q


st.title("Bromley - Classificador de Solicitações")

# Entrada de texto do usuário
user_input = st.text_area(
    "Digite sua reclamação, solicitação ou comentário:",
    placeholder="Exemplo: 'Meu celular não está carregando. O que fazer?'",
)

if st.button("Classificar"):
    if user_input:
        # Inicializa a cadeia de processamento
        chain = chain_q()
        resultado = chain.invoke(user_input)

        # Exibe o resultado
        st.write("### Resultado da Classificação")
        st.json(resultado.model_dump())

        categoria = resultado.categoria
        st.write(f"**Categoria:** {categoria}")
    else:
        st.write(
            "Por favor, insira uma reclamação, solicitação ou comentário para classificar."
        )

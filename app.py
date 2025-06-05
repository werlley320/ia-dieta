import streamlit as st import openai

--- Chave da OpenAI ---

openai.api_key = "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"

st.set_page_config(page_title="IA Dieta", page_icon="🥗") st.title("🥗 IA Dieta Personalizada")

--- Formulário de entrada do usuário ---

st.header("📋 Informe seus dados") with st.form("form_dados"): nome = st.text_input("Nome") idade = st.number_input("Idade", min_value=0, max_value=120, step=1) peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1) altura = st.number_input("Altura (cm)", min_value=0.0, step=0.1) objetivo = st.selectbox("Objetivo", ["Perder peso", "Ganhar massa", "Manter peso"]) enviado = st.form_submit_button("Gerar dieta")

--- Geração de dieta personalizada ---

if enviado: with st.spinner("Gerando sua dieta personalizada..."): prompt = f""" Crie um plano alimentar personalizado para o seguinte perfil:

Nome: {nome}
    Idade: {idade} anos
    Peso: {peso} kg
    Altura: {altura} cm
    Objetivo: {objetivo.lower()}

    O plano deve incluir:
    - Café da manhã
    - Almoço
    - Lanche da tarde
    - Jantar
    - Dicas nutricionais
    """

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um nutricionista profissional."},
                {"role": "user", "content": prompt}
            ]
        )
        dieta = resposta.choices[0].message.content
        st.success("Plano alimentar gerado com sucesso!")
        st.markdown("### 🥗 Sua dieta personalizada")
        st.markdown(dieta)

    except Exception as e:
        st.error("Erro ao gerar dieta. Verifique a chave da API ou tente novamente mais tarde.")
        st.exception(e)

Rodapé

st.markdown("---") st.markdown("Desenvolvido com ❤️ por Werlley")


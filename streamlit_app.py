import streamlit as st
# Atividade 01:
# Fazer seu primeiro web app com o streamlit, devendo realizar o deploy e postar o link
# Este app-web deverá conter:
# 1) Seu nome
# 2) um tema que pretende tratar
# 3) A divisão das seções do app, prevendo futura expansão para apresentar dados e gráficos.
# 4) Bases de dados que imagina usar


st.title("🚀 Iniciando meu primeiro app")
st.write ('**Quantidade de matrículas nas escolas estaduais do ES, por modalidade de ensino em 2025.**')
st.text ('')
st.markdown ('📌 **Desenvolvedor:**')
st.text ('Márcio Ribeiro')
st.text ('')
st.markdown ('🔹 **Do tema:**')
st.text ('Criar um dashboard das matrículas do ano de 2025, por modalidade e situação de ensino, incluido alunos do AEE (Atendimento Educação Especial).')
st.text ('')
st.write ('🎨 **Do layout:**')
st.write ('O layout deverá permitir que o usuário selecione a modalidade desejada:')
st.markdown ('*- Ensino fundamental anos iniciais*')
st.write ('*- Ensino fundamental anos finais*')
st.write ('*- Ensino Médio*')
st.markdown ('Também deverá possibilitar que o usuário selecione a situação em que o ensino é aplicado:')
st.write ('*- Regular*')
st.write ('*- EJA*')
st.write ('*- Sócio Educativa*')
st.write ('*- Prisional*')
st.text ('')
st.write ('📝 **Da base de dados:**')
st.text ('Será consumida a base de dados local(csv), estraída do Sistema SEGES. Por motivos de segurança, nao será permitido o consumo direto da base de dados do sistema da SEDU.')
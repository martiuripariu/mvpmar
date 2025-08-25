import streamlit as st

# Nome da página
st.set_page_config(
    page_title = "Iniciando meu primeiro app",
    page_icon="🚀",
    layout="wide")

# Título principal
st.title("**Quantidade de matrículas nas escolas estaduais do ES, por modalidade de ensino em 2025.**")
st.markdown("---")
st.text ('')

# 1§ - Apresentação
st.header("📌 **Desenvolvedor:**")
st.write("*Márcio Ribeiro*")
st.text ('')

# 2§ - Tema
st.header("🔹 **Do tema:**")
st.write("Criar um dashboard das matrículas do ano de 2025, por modalidade e situação de ensino, incluido alunos do AEE (Atendimento Educação Especial).")
st.text ('')

# 3§ - Layout
st.header("🎨 **Do layout:**")
st.write("O layout deverá permitir que o usuário selecione a modalidade desejada:")
st.text ('')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📝 Dashboard Modalidade")
    st.write("Ensino fundamental anos iniciais / anos finais / médio")

with col2:
    st.subheader("📝 Dashboard Situação")
    st.write("Regular / EJA / Sócio Educativa / Prisional")


with col3:
    st.subheader("👥 Dashboard Regional")
    st.write("Superintendencias / Cidades / Escolas")

# 4§ - Bases de dados
st.header("📝 **Da base de dados:**")
st.write("Será consumida a base de dados local(csv), extraído do Sistema SEGES e dados do Último Censo Escolar.")
st.markdown("""
- Censo Escolar
- Sistema SEGES
""")

# 5§ Próximas ações
st.header("Próximas Ações")
st.write("Requisições dos usuários que serão, em breve, atendidas.")

st.markdown("""
    1. Indicadores de taxa de ocupação por escola;
    2. Comparativos entre regionais;
    3. Previsões e estatisticas;
    4. Relatórios em PDF;
    5. Download dos dados filtrados;
    6. Gráficos interativos de evolução de matrículas
""")

# Rodapé
st.markdown("---")
st.markdown("Developed by MRibeiro - set/25")

# Lembretes de comandos git
# abrir o terminal no ambiente virtual bash e usar os comandos:
# $ git add nome_do_arquivo
# $ git commit -m "Primeira versão" ou $ git commit --amend -m "Primeira versão"
# $ git branch -M main
# $ git push --force
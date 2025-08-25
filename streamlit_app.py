import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel de Matrículas", layout="wide")

st.title("📊 Painel de Matrículas Nacional - Regular e AEE")

# Carregando dados
@st.cache_data
def carregar_dados():
    try:
        # Usar sep=';' se seu CSV usa ponto e vírgula
        df = pd.read_csv('matriculas.csv', sep=';')
        return df
    except FileNotFoundError:
        st.error("Arquivo 'matriculas.csv' não encontrado.")
        return pd.DataFrame()

df = carregar_dados()

if not df.empty:

    # 🔹 NOVO: Estatísticas descritivas gerais da base
    st.subheader("📊 Estatísticas Descritivas da Base de Dados")
    desc = df.describe(include='all').T  # transposto para ficar mais legível
    st.dataframe(desc, use_container_width=True)

    st.markdown("---")

    # --- Filtros principais ---
    st.sidebar.header("🔍 Filtros")

    # Filtro por UF/SIGLA
    ufs = df['SIGLA'].unique()
    uf_padrao = ["ES"] if "ES" in ufs else []  # evita erro caso o ES não exista no dataset
    uf_selecionada = st.sidebar.multiselect("Filtrar por Estado (SIGLA)", ufs, default=uf_padrao)

    # Filtro por Cidade
    cidades = df[df['SIGLA'].isin(uf_selecionada)]['UF_CIDADE'].unique()
    cidades_selecionadas = st.sidebar.multiselect("Filtrar por Cidade", cidades, default=cidades)

    # Filtro por grupo
    grupo = st.sidebar.radio("Selecionar Grupo", ["Ambos", "Regular", "AEE"])

    # Filtro por colunas específicas (de acordo com grupo)
    colunas_regular = [
        "CRECHE_PARCIAL", "CRECHE_INTEGRAL", "PRE_PARCIAL", "PRE_INTEGRAL",
        "FUND1_PARCIAL", "FUND1_INTEGRAL", "FUND2_PARCIAL", "FUND2_INTEGRAL",
        "MEDIO_PARCIAL", "MEDIO_INTEGRAL", "EJA_FUND", "EJA_MEDIO", "TOTAL_REGULAR", "POR_CENTO"
    ]

    colunas_aee = [
        "PRE_PARCIAL_AEE", "PRE_INTEGRAL_AEE", "FUND1_PARCIAL_AEE", "FUND1_INTEGRAL_AEE",
        "FUND2_PARCIAL_AEE", "FUND2_INTEGRAL_AEE", "MEDIO_PARCIAL_AEE", "MEDIO_INTEGRAL_AEE",
        "EJA_FUND_AEE", "EJA_MEDIO_AEE", "TOTAL_AEE", "POR_CENTO_AEE"
    ]

    if grupo == "Regular":
        colunas_mostrar = st.sidebar.multiselect("Selecionar colunas REGULAR", colunas_regular, default=colunas_regular)
    elif grupo == "AEE":
        colunas_mostrar = st.sidebar.multiselect("Selecionar colunas AEE", colunas_aee, default=colunas_aee)
    else:  # Ambos
        colunas_mostrar = st.sidebar.multiselect(
            "Selecionar colunas (Regular + AEE)", colunas_regular + colunas_aee,
            default=colunas_regular + colunas_aee
        )

    # --- Aplicando os filtros ---
    df_filtrado = df[
        (df['SIGLA'].isin(uf_selecionada)) &
        (df['UF_CIDADE'].isin(cidades_selecionadas))
    ]

    # --- Mostrando dados filtrados ---
    st.subheader("📄 Dados Filtrados")

    if colunas_mostrar:
        dados_filtrados = df_filtrado[['SIGLA', 'UF_CIDADE', 'DESCRICAO'] + colunas_mostrar]
        st.dataframe(dados_filtrados)

        # 🔹 Botão para download CSV dos dados filtrados
        csv = dados_filtrados.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV dos dados filtrados",
            data=csv,
            file_name="dados_filtrados.csv",
            mime="text/csv"
        )
    else:
        st.info("Selecione pelo menos uma coluna para visualizar os dados.")

    # --- Gráfico de barras ---
    st.subheader("📈 Gráfico de Barras (Total por Cidade)")

    if grupo == "Regular" and "TOTAL_REGULAR" in df_filtrado.columns:
        fig = px.bar(
            df_filtrado,
            x="UF_CIDADE",
            y="TOTAL_REGULAR",
            color="SIGLA",
            title="Total de Matrículas Regulares por Cidade"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif grupo == "AEE" and "TOTAL_AEE" in df_filtrado.columns:
        fig = px.bar(
            df_filtrado,
            x="UF_CIDADE",
            y="TOTAL_AEE",
            color="SIGLA",
            title="Total de Matrículas AEE por Cidade"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif grupo == "Ambos" and "TOTAL_REGULAR" in df_filtrado.columns and "TOTAL_AEE" in df_filtrado.columns:
        df_plot = df_filtrado[["UF_CIDADE", "SIGLA", "TOTAL_REGULAR", "TOTAL_AEE"]].copy()
        df_plot = df_plot.melt(id_vars=["UF_CIDADE", "SIGLA"], 
                               value_vars=["TOTAL_REGULAR", "TOTAL_AEE"],
                               var_name="Tipo", value_name="Total")

        fig = px.bar(
            df_plot,
            x="UF_CIDADE",
            y="Total",
            color="Tipo",
            barmode="group",
            title="Comparativo de Matrículas - Regular vs AEE"
        )
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Nenhum dado disponível para exibir.")





# Lembretes de comandos git
# abrir o terminal no ambiente virtual bash e usar os comandos:
# $ git add streamlit_app.py
# $ git add requirements.txt
# $ git add README.md
# $ git add matriculas.csv
# $ git commit -m "Primeira versão" ou $ git commit --amend -m "Vr 1.3 c/descritivas"
# $ git status
# $ git log
# $ git push --force
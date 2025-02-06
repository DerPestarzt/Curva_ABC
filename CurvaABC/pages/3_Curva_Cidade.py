import os
import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Análise Curva ABC",
    layout="wide"
)

# CSS personalizado
st.markdown("""
    <style>
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px;
    }
    .card-a { 
        border-left: 4px solid #98FB98; 
        background-color: #f0fff0;
    }
    .card-b { 
        border-left: 4px solid #FFE4B5; 
        background-color: #fff8ee;
    }
    .card-c { 
        border-left: 4px solid #FFB6C1; 
        background-color: #fff0f3;
    }
    .total-value { 
        font-size: 24px; 
        font-weight: bold;
        color: #2c3e50;
    }
    .items-count { 
        color: #666;
        font-weight: 500;
    }
    .card h3 {
        color: #2c3e50;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    .card p {
        margin: 5px 0;
        color: #34495e;
    }
    .card strong {
        color: #2c3e50;
    }
    .stDataFrame {
        width: 100%;
        padding: 10px;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com navegação
st.markdown("""
    <div class="header-container">
        <div style="display: flex; align-items: center;">
            <h1>Análise Curva ABC</h1>
        </div>
        <div>
            <button style="background-color: #1E90FF; color: white; padding: 8px 15px; border: none; border-radius: 5px;">
                Importar CSV
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Função para carregar dados
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("CurvaCidade.xlsx")
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

df = load_data()

if df is not None:
    # Primeiro, vamos imprimir as colunas disponíveis para debug
    print("Colunas disponíveis:", df.columns.tolist())
    
    # Usar os nomes corretos das colunas
    class_a = df[df['Classificação'] == 'A']
    class_b = df[df['Classificação'] == 'B']
    class_c = df[df['Classificação'] == 'C']

    # Cards para cada classificação
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="card card-a">
                <h3 style="margin-bottom: 10px;">Classificação A</h3>
                <p class="items-count" style="margin: 5px 0;">{} cidades</p>
                <p class="total-value" style="margin: 5px 0;">R$ {:,.2f}</p>
            </div>
        """.format(len(class_a), class_a['Valor Total'].sum()), unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card card-b">
                <h3 style="margin-bottom: 10px;">Classificação B</h3>
                <p class="items-count" style="margin: 5px 0;">{} cidades</p>
                <p class="total-value" style="margin: 5px 0;">R$ {:,.2f}</p>
            </div>
        """.format(len(class_b), class_b['Valor Total'].sum()), unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card card-c">
                <h3 style="margin-bottom: 10px;">Classificação C</h3>
                <p class="items-count" style="margin: 5px 0;">{} cidades</p>
                <p class="total-value" style="margin: 5px 0;">R$ {:,.2f}</p>
            </div>
        """.format(len(class_c), class_c['Valor Total'].sum()), unsafe_allow_html=True)

    # Tabela detalhada
    st.markdown("### Tabela Detalhada")
    
    # Botão de download
    st.download_button(
        label="Download",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='tabela_detalhada.csv',
        mime='text/csv',
    )

    # Exibição da tabela com formatação
    st.dataframe(
        df.style.format({
            'Soma de VTOTAL': 'R$ {:,.2f}',
            'Valor Total': 'R$ {:,.2f}',
            'Percentual de Participação': '{:.1%}',
            'Percentual Acumulado': '{:.1%}'
        }).applymap(lambda x: 'background-color: #98FB98' if x == 'A' 
                   else ('background-color: #FFE4B5' if x == 'B' 
                   else ('background-color: #FFB6C1' if x == 'C' else '')), 
                   subset=['Classificação']),
        use_container_width=True
    )

    # Informações básicas sobre o DataFrame
    st.subheader("Informações do Dataset")
    st.write(f"Total de linhas: {df.shape[0]}")
    st.write(f"Total de colunas: {df.shape[1]}")

    st.markdown("### Proporções por Classificação")
    
    # Criar três colunas para os cards de proporção
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="card card-a">
                <h3 style="margin-bottom: 10px;">Classificação A</h3>
                <p style="margin: 5px 0;"><strong>Corte:</strong> 80%</p>
                <p style="margin: 5px 0;"><strong>Proporção Cidade:</strong> 21%</p>
                <p style="margin: 5px 0;"><strong>Proporção Valor:</strong> 79,72%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="card card-b">
                <h3 style="margin-bottom: 10px;">Classificação B</h3>
                <p style="margin: 5px 0;"><strong>Corte:</strong> 95%</p>
                <p style="margin: 5px 0;"><strong>Proporção Cidade:</strong> 26%</p>
                <p style="margin: 5px 0;"><strong>Proporção Valor:</strong> 15,27%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="card card-c">
                <h3 style="margin-bottom: 10px;">Classificação C</h3>
                <p style="margin: 5px 0;"><strong>Corte:</strong> 100%</p>
                <p style="margin: 5px 0;"><strong>Proporção Cidade:</strong> 52%</p>
                <p style="margin: 5px 0;"><strong>Proporção Valor:</strong> 5,01%</p>
            </div>
        """, unsafe_allow_html=True)   
import streamlit as st

st.set_page_config(
    page_title="Análise Curva ABC",
    layout="wide"
)

# CSS personalizado
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0;
        color: #004225;  /* Verde escuro Concrem */
    }
    .card {
        padding: 30px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0,66,37,0.1);
        margin: 20px auto;
        text-align: center;
        border: 1px solid rgba(0,66,37,0.1);
    }
    .nav-section {
        margin: 2rem auto;
        max-width: 800px;
    }
    .card h2 {
        color: #004225;
        margin-bottom: 20px;
        font-size: 1.8rem;
    }
    .card h3 {
        color: #004225;
        margin: 15px 0;
        font-size: 1.4rem;
    }
    .card p {
        color: #333;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 10px 0;
    }
    .card ul {
        list-style-type: none;
        padding: 0;
        margin: 15px 0;
    }
    .card li {
        color: #333;
        margin: 10px 0;
        font-size: 1.1rem;
    }
    .card strong {
        color: #004225;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-title">Sistema de Análise Curva ABC Concrem</h1>', unsafe_allow_html=True)

# Descrição do sistema
st.markdown("""
    <div class="nav-section">
        <div class="card">
            <h2>Bem-vindo ao Sistema de Análise Curva ABC</h2>
            <p>Utilize o menu lateral para navegar entre as diferentes análises:</p>
            <br>
            <h3>Análises Disponíveis:</h3>
            <ul>
                <li><strong>Curva Cliente</strong> - Análise ABC por cliente</li>
                <li><strong>Curva SKU</strong> - Análise ABC por SKU</li>
                <li><strong>Curva Cidade</strong> - Análise ABC por cidade</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)
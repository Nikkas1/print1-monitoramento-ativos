import streamlit as st
import pandas as pd
import sys
import os

# Adiciona o diretório raiz ao path para importar o backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import data_manager

st.set_page_config(page_title="Gestão de Ativos", page_icon="🏭", layout="wide")

st.title("🏭 Visão Geral dos Ativos")
st.write("Bem-vindo ao sistema de monitoramento de motores. Selecione uma opção no menu lateral para cadastrar ou visualizar os dados.")

# Carrega os dados do "backend"
equipamentos = data_manager.get_equipamentos()

if equipamentos:
    df = pd.DataFrame(equipamentos)
    st.subheader("Equipamentos Cadastrados")
    # Datatable interativo
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    # Cores semânticas para UX (Aviso)
    st.info("Nenhum equipamento cadastrado ainda. Vá até o menu lateral para adicionar o primeiro.")
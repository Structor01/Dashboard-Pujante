import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Dashboard Pujante",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para estilo preto e prata
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f1f1f;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2c3e50;
        margin: 0.5rem 0;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #6c757d;
        margin-bottom: 0.5rem;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Carrega e processa os dados das planilhas"""
    try:
        # Carregar dados de leads
        leads_df = pd.read_excel('data/LeadsKommoPujante.xlsx')
        
        # Carregar dados de escritórios apoiadores
        escritorios_df = pd.read_excel('data/escritorios_apoiadores.xlsx')
        
        # Processar datas
        if 'Data de criação' in leads_df.columns:
            leads_df['Data de criação'] = pd.to_datetime(leads_df['Data de criação'], errors='coerce')
        
        return leads_df, escritorios_df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return None, None

def create_metrics_cards(leads_df, escritorios_df):
    """Cria cards de métricas principais"""
    col1, col2, col3, col4 = st.columns(4)
    
    # Total de leads
    total_leads = len(leads_df) if leads_df is not None else 0
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Leads</div>
            <div class="metric-value">{total_leads:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Escritórios apoiadores
    total_escritorios = len(escritorios_df) if escritorios_df is not None else 0
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Escritórios Apoiadores</div>
            <div class="metric-value">{total_escritorios}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Receita mensal
    receita_mensal = total_escritorios * 350
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Receita Mensal</div>
            <div class="metric-value">R$ {receita_mensal:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Receita anual
    receita_anual = receita_mensal * 12
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Receita Anual</div>
            <div class="metric-value">R$ {receita_anual:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

def create_leads_charts(leads_df):
    """Cria gráficos relacionados aos leads"""
    if leads_df is None or leads_df.empty:
        st.warning("Dados de leads não disponíveis")
        return
    
    col1, col2 = st.columns(2)
    
    # Gráfico de leads por etapa
    with col1:
        st.subheader("📈 Leads por Etapa do Funil")
        if 'Etapa do lead' in leads_df.columns:
            etapas_count = leads_df['Etapa do lead'].value_counts()
            
            fig_etapas = px.pie(
                values=etapas_count.values,
                names=etapas_count.index,
                title="Distribuição de Leads por Etapa",
                color_discrete_sequence=['#2c3e50', '#34495e', '#7f8c8d']
            )
            fig_etapas.update_layout(
                font=dict(size=12),
                showlegend=True,
                height=400
            )
            st.plotly_chart(fig_etapas, use_container_width=True)
    
    # Gráfico de leads por período
    with col2:
        st.subheader("📅 Leads por Período")
        if 'Data de criação' in leads_df.columns:
            # Filtrar dados válidos
            leads_com_data = leads_df.dropna(subset=['Data de criação'])
            
            if not leads_com_data.empty:
                # Agrupar por data
                leads_com_data['Data'] = leads_com_data['Data de criação'].dt.date
                leads_por_dia = leads_com_data.groupby('Data').size().reset_index(name='Quantidade')
                
                fig_tempo = px.line(
                    leads_por_dia,
                    x='Data',
                    y='Quantidade',
                    title="Leads Criados por Dia",
                    markers=True
                )
                fig_tempo.update_traces(line_color='#2c3e50', marker_color='#e74c3c')
                fig_tempo.update_layout(
                    font=dict(size=12),
                    height=400,
                    xaxis_title="Data",
                    yaxis_title="Número de Leads"
                )
                st.plotly_chart(fig_tempo, use_container_width=True)
            else:
                st.info("Dados de data não disponíveis para análise temporal")

def create_escritorios_charts(escritorios_df):
    """Cria gráficos relacionados aos escritórios apoiadores"""
    if escritorios_df is None or escritorios_df.empty:
        st.warning("Dados de escritórios não disponíveis")
        return
    
    st.subheader("🏢 Escritórios Apoiadores")
    
    col1, col2 = st.columns(2)
    
    # Lista de escritórios
    with col1:
        st.subheader("Lista de Escritórios")
        if 'Nome do Escritório' in escritorios_df.columns:
            for idx, row in escritorios_df.iterrows():
                nome = row['Nome do Escritório']
                cidade = row.get('Cidade', 'N/A')
                st.markdown(f"**{nome}**")
                st.markdown(f"📍 {cidade}")
                st.markdown(f"💰 R$ 350,00/mês")
                st.markdown("---")
    
    # Distribuição por cidade
    with col2:
        st.subheader("Distribuição por Região")
        if 'Cidade' in escritorios_df.columns:
            # Simplificar cidades (pegar primeira cidade quando há múltiplas)
            cidades_simplificadas = []
            for cidade in escritorios_df['Cidade']:
                if pd.notna(cidade):
                    primeira_cidade = cidade.split(',')[0].strip()
                    cidades_simplificadas.append(primeira_cidade)
                else:
                    cidades_simplificadas.append('N/A')
            
            escritorios_df['Cidade_Principal'] = cidades_simplificadas
            cidades_count = escritorios_df['Cidade_Principal'].value_counts()
            
            fig_cidades = px.bar(
                x=cidades_count.index,
                y=cidades_count.values,
                title="Escritórios por Cidade Principal",
                color=cidades_count.values,
                color_continuous_scale=['#bdc3c7', '#2c3e50']
            )
            fig_cidades.update_layout(
                font=dict(size=12),
                height=400,
                xaxis_title="Cidade",
                yaxis_title="Número de Escritórios",
                showlegend=False
            )
            st.plotly_chart(fig_cidades, use_container_width=True)

def create_financial_analysis():
    """Cria análise financeira detalhada"""
    st.subheader("💰 Análise Financeira")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Projeção de Receita")
        
        # Dados para projeção
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        receita_mensal = [5250] * 12  # 15 escritórios × R$ 350
        receita_acumulada = np.cumsum(receita_mensal)
        
        fig_receita = go.Figure()
        
        # Receita mensal
        fig_receita.add_trace(go.Bar(
            x=meses,
            y=receita_mensal,
            name='Receita Mensal',
            marker_color='#2c3e50',
            yaxis='y'
        ))
        
        # Receita acumulada
        fig_receita.add_trace(go.Scatter(
            x=meses,
            y=receita_acumulada,
            name='Receita Acumulada',
            line=dict(color='#e74c3c', width=3),
            yaxis='y2'
        ))
        
        fig_receita.update_layout(
            title='Projeção de Receita Anual',
            xaxis_title='Mês',
            yaxis=dict(title='Receita Mensal (R$)', side='left'),
            yaxis2=dict(title='Receita Acumulada (R$)', side='right', overlaying='y'),
            height=400,
            font=dict(size=12)
        )
        
        st.plotly_chart(fig_receita, use_container_width=True)
    
    with col2:
        st.subheader("Indicadores Financeiros")
        
        # LTV (Lifetime Value) - assumindo retenção média de 24 meses
        ltv_medio = 350 * 24
        
        st.markdown(f"""
        **Métricas Principais:**
        
        - **Receita por Escritório:** R$ 350,00/mês
        - **LTV Médio:** R$ {ltv_medio:,.2f} (24 meses)
        - **Receita Total Mensal:** R$ 5.250,00
        - **Receita Total Anual:** R$ 63.000,00
        
        **Potencial de Crescimento:**
        
        - **+5 escritórios:** +R$ 1.750,00/mês
        - **+10 escritórios:** +R$ 3.500,00/mês
        - **Meta 30 escritórios:** R$ 10.500,00/mês
        """)

def main():
    """Função principal do dashboard"""
    # Título principal
    st.markdown('<h1 class="main-header">📊 Dashboard Pujante</h1>', unsafe_allow_html=True)
    
    # Carregar dados
    leads_df, escritorios_df = load_data()
    
    # Sidebar com filtros
    st.sidebar.title("🔧 Filtros e Configurações")
    st.sidebar.markdown("---")
    
    # Filtro de período para leads
    if leads_df is not None and 'Data de criação' in leads_df.columns:
        leads_com_data = leads_df.dropna(subset=['Data de criação'])
        if not leads_com_data.empty:
            min_date = leads_com_data['Data de criação'].min().date()
            max_date = leads_com_data['Data de criação'].max().date()
            
            date_range = st.sidebar.date_input(
                "Período de Análise",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )
            
            # Filtrar dados por período
            if len(date_range) == 2:
                start_date, end_date = date_range
                mask = (leads_df['Data de criação'].dt.date >= start_date) & \
                       (leads_df['Data de criação'].dt.date <= end_date)
                leads_df = leads_df[mask]
    
    # Métricas principais
    create_metrics_cards(leads_df, escritorios_df)
    
    st.markdown("---")
    
    # Gráficos de leads
    create_leads_charts(leads_df)
    
    st.markdown("---")
    
    # Gráficos de escritórios
    create_escritorios_charts(escritorios_df)
    
    st.markdown("---")
    
    # Análise financeira
    create_financial_analysis()
    
    # Tabela detalhada de leads (opcional)
    if st.sidebar.checkbox("Mostrar Tabela Detalhada de Leads"):
        st.subheader("📋 Dados Detalhados dos Leads")
        if leads_df is not None:
            # Selecionar colunas principais
            colunas_principais = ['ID', 'Lead título', 'Contato principal', 'Etapa do lead', 'Data de criação']
            colunas_disponiveis = [col for col in colunas_principais if col in leads_df.columns]
            
            st.dataframe(
                leads_df[colunas_disponiveis].head(50),
                use_container_width=True,
                height=400
            )
        else:
            st.warning("Dados de leads não disponíveis")

if __name__ == "__main__":
    main()


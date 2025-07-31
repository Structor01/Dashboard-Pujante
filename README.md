# 📊 Dashboard Pujante

Dashboard interativo desenvolvido com Streamlit para análise de leads e escritórios apoiadores da Pujante.

## 🚀 Funcionalidades

- **Métricas Principais**: Total de leads, escritórios apoiadores, receita mensal e anual
- **Análise de Leads**: Distribuição por etapa do funil e análise temporal
- **Escritórios Apoiadores**: Lista completa e distribuição geográfica
- **Análise Financeira**: Projeções de receita e indicadores de LTV
- **Interface Responsiva**: Design moderno com cores preto e prata

## 📈 Indicadores Apresentados

### Leads
- Total de leads: 1.695
- Distribuição por etapas do funil de vendas
- Análise temporal de criação de leads

### Escritórios Apoiadores
- Total de escritórios: 15
- Receita mensal: R$ 5.250,00 (15 × R$ 350,00)
- Receita anual: R$ 63.000,00
- LTV médio: R$ 8.400,00 (24 meses)

### Potencial de Crescimento
- +5 escritórios: +R$ 1.750,00/mês
- +10 escritórios: +R$ 3.500,00/mês
- Meta 30 escritórios: R$ 10.500,00/mês

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para criação do dashboard
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas
- **Python**: Linguagem de programação

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/Dashboard-Pujante.git
   cd Dashboard-Pujante
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

4. **Acesse no navegador**:
   O dashboard estará disponível em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
Dashboard-Pujante/
├── dashboard.py          # Aplicação principal do Streamlit
├── requirements.txt      # Dependências do projeto
├── data/                # Dados das planilhas
│   ├── LeadsKommoPujante.xlsx
│   └── escritorios_apoiadores.xlsx
└── README.md            # Documentação do projeto
```

## 📊 Dados

O dashboard utiliza duas planilhas principais:

1. **LeadsKommoPujante.xlsx**: Dados dos leads com informações de contato, etapas do funil e datas
2. **escritorios_apoiadores.xlsx**: Lista dos escritórios apoiadores e suas localizações

## 🎨 Design

O dashboard segue um design minimalista inspirado no estilo visual moderno, utilizando:
- Paleta de cores preto e prata
- Layout responsivo
- Visualizações interativas
- Cards de métricas destacados

## 📱 Funcionalidades Interativas

- **Filtros de Data**: Análise de leads por período específico
- **Sidebar**: Configurações e filtros avançados
- **Tabela Detalhada**: Visualização opcional dos dados completos dos leads
- **Gráficos Interativos**: Zoom, hover e seleção de dados

## 🔄 Atualizações

Para atualizar os dados:
1. Substitua os arquivos na pasta `data/`
2. Reinicie o dashboard
3. Os dados serão automaticamente recarregados

## 📞 Suporte

Para dúvidas ou sugestões sobre o dashboard, entre em contato com a equipe de desenvolvimento.

## 📄 Licença

Este projeto é de uso interno da Pujante.

---

**Desenvolvido com ❤️ para a Pujante**


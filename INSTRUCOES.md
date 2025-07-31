# 🚀 Instruções de Execução - Dashboard Pujante

## 📋 Pré-requisitos

Antes de executar o dashboard, certifique-se de ter:

- **Python 3.7 ou superior** instalado
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)

## 🔧 Instalação Passo a Passo

### 1. Clone o Repositório
```bash
git clone https://github.com/Structor01/Dashboard-Pujante.git
cd Dashboard-Pujante
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o Dashboard
```bash
streamlit run dashboard.py
```

### 4. Acesse no Navegador
O dashboard será aberto automaticamente no seu navegador padrão em:
```
http://localhost:8501
```

## 📊 Dados Incluídos

O projeto já inclui os dados necessários na pasta `data/`:
- `LeadsKommoPujante.xlsx` - Dados dos leads (1.695 registros)
- `escritorios_apoiadores.xlsx` - Dados dos escritórios apoiadores (15 registros)

## 🔄 Atualizando os Dados

Para atualizar os dados do dashboard:

1. Substitua os arquivos na pasta `data/` pelos novos arquivos
2. Mantenha os mesmos nomes dos arquivos
3. Reinicie o dashboard (Ctrl+C e execute novamente `streamlit run dashboard.py`)

## 🎯 Funcionalidades Disponíveis

### Métricas Principais
- Total de leads: 1.695
- Escritórios apoiadores: 15
- Receita mensal: R$ 5.250,00
- Receita anual: R$ 63.000,00

### Visualizações
- Distribuição de leads por etapa do funil
- Análise temporal de criação de leads
- Lista completa de escritórios apoiadores
- Distribuição geográfica dos escritórios
- Projeções de receita e análise financeira

### Filtros Interativos
- Filtro de período para análise de leads
- Opção de exibir tabela detalhada de leads

## 🛠️ Solução de Problemas

### Erro de Dependências
Se encontrar erros de dependências, tente:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Erro de Porta Ocupada
Se a porta 8501 estiver ocupada, use:
```bash
streamlit run dashboard.py --server.port 8502
```

### Problemas com Dados
- Verifique se os arquivos Excel estão na pasta `data/`
- Certifique-se de que os nomes dos arquivos estão corretos
- Verifique se os arquivos não estão corrompidos

## 📱 Acesso Remoto

Para acessar o dashboard de outros dispositivos na rede:
```bash
streamlit run dashboard.py --server.address 0.0.0.0
```

Depois acesse via: `http://[IP_DO_COMPUTADOR]:8501`

## 🔒 Segurança

- O dashboard é executado localmente por padrão
- Para uso em produção, considere configurar autenticação
- Mantenha os dados sensíveis protegidos

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique este arquivo de instruções
2. Consulte o README.md do projeto
3. Entre em contato com a equipe de desenvolvimento

---

**Dashboard Pujante - Desenvolvido com ❤️ para análise de dados**


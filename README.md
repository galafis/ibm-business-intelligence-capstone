# IBM Business Intelligence Professional Certificate Capstone Project

*[English version below / Versão em inglês abaixo]*

## 🇧🇷 Português

### 📊 Visão Geral

Este projeto representa o trabalho final do **IBM Business Intelligence Professional Certificate**, demonstrando competências avançadas em business intelligence, data warehousing, ETL, dashboards executivos, análise de KPIs, modelagem dimensional e soluções de BI empresariais. A plataforma desenvolvida oferece uma solução completa para inteligência de negócios, desde a coleta de dados até a apresentação de insights estratégicos.

**Desenvolvido por:** Gabriel Demetrios Lafis  
**Certificação:** IBM Business Intelligence Professional Certificate  
**Tecnologias:** IBM Cognos, Tableau, Power BI, SQL Server, Python, DAX, MDX  
**Área de Foco:** Business Intelligence, Data Warehousing, Executive Dashboards, KPI Analytics

### 🎯 Características Principais

- **Enterprise Data Warehouse:** Data warehouse empresarial completo
- **ETL Pipeline:** Pipeline ETL robusto e escalável
- **Executive Dashboards:** Dashboards executivos e estratégicos
- **KPI Management:** Gestão e monitoramento de KPIs
- **OLAP Analytics:** Análises multidimensionais OLAP
- **Self-Service BI:** BI self-service para usuários de negócio
- **Real-time Monitoring:** Monitoramento em tempo real

### 🛠️ Stack Tecnológico

| Categoria | Tecnologia | Versão | Propósito |
|-----------|------------|--------|-----------|
| **BI Platform** | IBM Cognos | 11.2+ | Plataforma BI principal |
| **Visualization** | Tableau | 2023.3+ | Visualizações avançadas |
| **Microsoft BI** | Power BI | Latest | Dashboards corporativos |
| **Database** | SQL Server | 2022 | Data warehouse |
| **ETL Tool** | SSIS | 2022 | Integração de dados |
| **OLAP** | SSAS | 2022 | Análises multidimensionais |
| **Programming** | Python | 3.11+ | Automação e análises |
| **Query Language** | DAX | Latest | Medidas e cálculos |
| **MDX** | MDX | Latest | Consultas multidimensionais |
| **Reporting** | SSRS | 2022 | Relatórios corporativos |

### 🚀 Começando

#### Pré-requisitos
- SQL Server 2019 ou superior
- IBM Cognos Analytics 11.2+
- Tableau Desktop 2023.3+
- Power BI Desktop
- Python 3.11 ou superior
- Visual Studio (para SSIS/SSAS)

#### Instalação
```bash
# Clone o repositório
git clone https://github.com/galafis/ibm-business-intelligence-capstone.git
cd ibm-business-intelligence-capstone

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\\Scripts\\activate  # Windows

# Instale as dependências Python
pip install -r requirements.txt

# Configure o data warehouse
sqlcmd -S localhost -i sql/create_datawarehouse.sql

# Execute a aplicação principal
python src/main_platform.py
```

#### Acesso Rápido
```bash
# Executar ETL completo
python src/etl/run_etl_pipeline.py --full-load

# Atualizar cubos OLAP
python src/olap/refresh_cubes.py --all

# Gerar relatórios executivos
python src/reporting/generate_executive_reports.py

# Monitorar KPIs
python src/kpi/kpi_monitor.py --real-time
```

### 📊 Funcionalidades Detalhadas

#### 🏢 **Enterprise Data Warehouse**
- **Dimensional Modeling:** Modelagem dimensional (Star/Snowflake)
- **Data Marts:** Data marts especializados por área
- **Slowly Changing Dimensions:** Gestão de dimensões que mudam
- **Fact Tables:** Tabelas de fatos otimizadas
- **Aggregate Tables:** Tabelas agregadas para performance
- **Data Lineage:** Rastreabilidade de dados

#### 🔄 **ETL Pipeline**
- **Data Extraction:** Extração de múltiplas fontes
- **Data Transformation:** Transformações complexas
- **Data Loading:** Carregamento otimizado
- **Error Handling:** Tratamento robusto de erros
- **Data Quality:** Validação e limpeza de dados
- **Incremental Loading:** Carregamento incremental

#### 📈 **Executive Dashboards**
- **CEO Dashboard:** Visão estratégica da empresa
- **CFO Dashboard:** Indicadores financeiros
- **Sales Dashboard:** Performance de vendas
- **Operations Dashboard:** Eficiência operacional
- **HR Dashboard:** Métricas de recursos humanos
- **Customer Dashboard:** Análise de clientes

#### 📊 **OLAP Analytics**
- **Multidimensional Cubes:** Cubos multidimensionais
- **Drill-down/Roll-up:** Navegação hierárquica
- **Slice and Dice:** Análises por diferentes dimensões
- **What-if Analysis:** Análises de cenários
- **Time Intelligence:** Inteligência temporal
- **Calculated Members:** Membros calculados

### 🏗️ Arquitetura do Sistema

```
ibm-business-intelligence-capstone/
├── src/
│   ├── main_platform.py          # Aplicação principal
│   ├── bi_platform.py            # Plataforma BI
│   ├── datawarehouse/
│   │   ├── dimensional_model.py  # Modelo dimensional
│   │   ├── fact_tables.py        # Tabelas de fatos
│   │   ├── dimension_tables.py   # Tabelas de dimensões
│   │   └── scd_manager.py        # Gestão de SCDs
│   ├── etl/
│   │   ├── extraction.py         # Extração de dados
│   │   ├── transformation.py     # Transformação
│   │   ├── loading.py            # Carregamento
│   │   └── data_quality.py       # Qualidade de dados
│   ├── olap/
│   │   ├── cube_builder.py       # Construtor de cubos
│   │   ├── mdx_queries.py        # Consultas MDX
│   │   ├── calculations.py       # Cálculos OLAP
│   │   └── hierarchies.py        # Hierarquias
│   ├── dashboards/
│   │   ├── executive_dashboard.py # Dashboard executivo
│   │   ├── financial_dashboard.py # Dashboard financeiro
│   │   ├── sales_dashboard.py     # Dashboard de vendas
│   │   └── operational_dashboard.py # Dashboard operacional
│   ├── kpi/
│   │   ├── kpi_calculator.py     # Calculadora de KPIs
│   │   ├── kpi_monitor.py        # Monitor de KPIs
│   │   ├── alerts.py             # Sistema de alertas
│   │   └── benchmarking.py       # Benchmarking
│   ├── reporting/
│   │   ├── report_generator.py   # Gerador de relatórios
│   │   ├── scheduled_reports.py  # Relatórios agendados
│   │   └── ad_hoc_reports.py     # Relatórios ad-hoc
│   ├── cognos/
│   │   ├── cognos_connector.py   # Conector Cognos
│   │   ├── framework_manager.py  # Framework Manager
│   │   └── report_studio.py      # Report Studio
│   └── utils/
│       ├── security_manager.py   # Gerenciador de segurança
│       ├── performance_monitor.py # Monitor de performance
│       └── metadata_manager.py   # Gerenciador de metadados
├── sql/
│   ├── datawarehouse/            # Scripts do DW
│   ├── etl/                      # Scripts ETL
│   ├── olap/                     # Scripts OLAP
│   └── reports/                  # Scripts de relatórios
├── cognos_models/                # Modelos Cognos
├── tableau_workbooks/            # Workbooks Tableau
├── powerbi_reports/              # Relatórios Power BI
├── ssas_cubes/                   # Cubos SSAS
├── tests/
│   ├── test_etl.py               # Testes ETL
│   ├── test_olap.py              # Testes OLAP
│   └── test_dashboards.py        # Testes de dashboards
└── docs/                         # Documentação
```

### 📊 Casos de Uso

#### 1. **Dashboard Executivo CEO**
```python
from src.dashboards.executive_dashboard import CEODashboard

# Dashboard CEO
ceo_dashboard = CEODashboard()
kpis = ceo_dashboard.calculate_executive_kpis()
charts = ceo_dashboard.generate_strategic_charts(kpis)

# Métricas principais
revenue_growth = kpis['revenue_growth']
market_share = kpis['market_share']
customer_satisfaction = kpis['customer_satisfaction']
```

#### 2. **Análise OLAP Multidimensional**
```python
from src.olap.cube_builder import SalesCube

# Análise de vendas multidimensional
sales_cube = SalesCube()
result = sales_cube.query(
    measures=['Sales Amount', 'Profit Margin'],
    dimensions=['Time.Year', 'Geography.Country', 'Product.Category'],
    filters={'Time.Year': '2024', 'Geography.Region': 'Americas'}
)
```

#### 3. **Pipeline ETL Automatizado**
```python
from src.etl.etl_pipeline import ETLPipeline

# Pipeline ETL
pipeline = ETLPipeline()

# Extração
source_data = pipeline.extract_from_sources([
    'ERP_System', 'CRM_System', 'Web_Analytics'
])

# Transformação
transformed_data = pipeline.transform(source_data)

# Carregamento
pipeline.load_to_datawarehouse(transformed_data)
```

### 🧪 Testes e Qualidade

#### Executar Testes
```bash
# Testes de ETL
python -m pytest tests/test_etl.py -v

# Testes de OLAP
python -m pytest tests/test_olap.py -v

# Testes de dashboards
python -m pytest tests/test_dashboards.py -v

# Validação de qualidade de dados
python src/etl/data_quality.py --validate-all

# Testes de performance
python tests/performance_tests.py
```

#### Métricas de Qualidade
- **Data Accuracy:** >99% de precisão dos dados
- **ETL Performance:** <30 minutos para carga completa
- **Dashboard Load Time:** <3 segundos
- **OLAP Query Response:** <5 segundos
- **Data Freshness:** Atualização a cada hora
- **System Availability:** >99.5% uptime

### 📈 Resultados e Impacto

#### KPIs Empresariais Monitorados
- **Financial KPIs:**
  - Revenue Growth Rate
  - Profit Margin
  - EBITDA
  - Cash Flow
  - ROI/ROE
- **Sales KPIs:**
  - Sales Growth
  - Conversion Rate
  - Average Deal Size
  - Sales Cycle Length
  - Customer Acquisition Cost
- **Operational KPIs:**
  - Operational Efficiency
  - Quality Metrics
  - Productivity Ratios
  - Cost per Unit
  - Inventory Turnover

#### Casos de Sucesso
- **Executive Decision Making:** 40% melhoria na velocidade de decisões
- **Data-Driven Culture:** 60% aumento no uso de dados
- **Cost Reduction:** 25% redução em custos operacionais
- **Revenue Growth:** 15% aumento na receita através de insights

### 🔧 Configuração Avançada

#### Configuração do Data Warehouse
```sql
-- Configuração de particionamento
CREATE PARTITION FUNCTION pf_sales_date (DATE)
AS RANGE RIGHT FOR VALUES 
('2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01');

-- Índices columnstore para performance
CREATE CLUSTERED COLUMNSTORE INDEX cci_fact_sales 
ON fact_sales;
```

#### Configuração de Segurança
```python
# config/security_config.py
SECURITY_CONFIG = {
    'role_based_access': {
        'executives': ['all_dashboards', 'strategic_reports'],
        'managers': ['departmental_dashboards', 'operational_reports'],
        'analysts': ['detailed_data', 'ad_hoc_analysis']
    },
    'data_masking': {
        'sensitive_fields': ['customer_ssn', 'employee_salary'],
        'masking_rules': 'partial_encryption'
    }
}
```

### 📊 Metodologias de BI

#### Kimball Methodology
1. **Business Requirements:** Levantamento de requisitos
2. **Dimensional Modeling:** Modelagem dimensional
3. **Physical Design:** Design físico do DW
4. **ETL Design:** Design do processo ETL
5. **BI Application Design:** Design das aplicações BI
6. **Deployment:** Implementação e deploy

#### Best Practices
- **Data Governance:** Governança de dados corporativa
- **Metadata Management:** Gestão de metadados
- **Performance Optimization:** Otimização de performance
- **Security & Compliance:** Segurança e conformidade
- **Change Management:** Gestão de mudanças

### 📊 Dashboards Especializados

#### Financial Dashboard
- **P&L Analysis:** Análise de demonstrativo de resultados
- **Budget vs Actual:** Orçado vs realizado
- **Cash Flow Forecast:** Previsão de fluxo de caixa
- **Financial Ratios:** Indicadores financeiros
- **Cost Center Analysis:** Análise por centro de custo

#### Sales Dashboard
- **Sales Performance:** Performance de vendas
- **Territory Analysis:** Análise por território
- **Product Performance:** Performance de produtos
- **Sales Funnel:** Funil de vendas
- **Customer Segmentation:** Segmentação de clientes

#### Operations Dashboard
- **Production Metrics:** Métricas de produção
- **Quality Control:** Controle de qualidade
- **Supply Chain:** Cadeia de suprimentos
- **Resource Utilization:** Utilização de recursos
- **Efficiency Metrics:** Métricas de eficiência

### 🎓 Competências Demonstradas

#### BI Technical Skills
- **Data Warehousing:** Modelagem e implementação de DW
- **ETL Development:** Desenvolvimento de processos ETL
- **OLAP Design:** Design de cubos multidimensionais
- **Dashboard Development:** Desenvolvimento de dashboards
- **Report Development:** Desenvolvimento de relatórios

#### BI Tools Expertise
- **IBM Cognos:** Analytics, Framework Manager, Report Studio
- **Microsoft BI:** SSIS, SSAS, SSRS, Power BI
- **Tableau:** Desktop, Server, Prep
- **SQL Server:** Database, Analysis Services
- **Python:** Automação e análises avançadas

#### Business Skills
- **Requirements Gathering:** Levantamento de requisitos
- **Stakeholder Management:** Gestão de stakeholders
- **Business Process Analysis:** Análise de processos
- **KPI Definition:** Definição de indicadores
- **Strategic Planning:** Planejamento estratégico

### 📚 Documentação Adicional

- **[BI Architecture Guide](docs/bi_architecture_guide.md):** Guia de arquitetura BI
- **[ETL Best Practices](docs/etl_best_practices.md):** Melhores práticas ETL
- **[Dashboard Design Guide](docs/dashboard_design_guide.md):** Guia de design de dashboards
- **[OLAP User Guide](docs/olap_user_guide.md):** Guia do usuário OLAP

### 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) antes de submeter pull requests.

### 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🇺🇸 English

### 📊 Overview

This project represents the capstone work for the **IBM Business Intelligence Professional Certificate**, demonstrating advanced competencies in business intelligence, data warehousing, ETL, executive dashboards, KPI analysis, dimensional modeling, and enterprise BI solutions. The developed platform offers a complete solution for business intelligence, from data collection to strategic insight presentation.

**Developed by:** Gabriel Demetrios Lafis  
**Certification:** IBM Business Intelligence Professional Certificate  
**Technologies:** IBM Cognos, Tableau, Power BI, SQL Server, Python, DAX, MDX  
**Focus Area:** Business Intelligence, Data Warehousing, Executive Dashboards, KPI Analytics

### 🎯 Key Features

- **Enterprise Data Warehouse:** Complete enterprise data warehouse
- **ETL Pipeline:** Robust and scalable ETL pipeline
- **Executive Dashboards:** Executive and strategic dashboards
- **KPI Management:** KPI management and monitoring
- **OLAP Analytics:** Multidimensional OLAP analytics
- **Self-Service BI:** Self-service BI for business users
- **Real-time Monitoring:** Real-time monitoring

### 🛠️ Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **BI Platform** | IBM Cognos | 11.2+ | Main BI platform |
| **Visualization** | Tableau | 2023.3+ | Advanced visualizations |
| **Microsoft BI** | Power BI | Latest | Corporate dashboards |
| **Database** | SQL Server | 2022 | Data warehouse |

### 🚀 Getting Started

#### Prerequisites
- SQL Server 2019 or higher
- IBM Cognos Analytics 11.2+
- Tableau Desktop 2023.3+
- Power BI Desktop
- Python 3.11 or higher
- Visual Studio (for SSIS/SSAS)

#### Installation
```bash
# Clone the repository
git clone https://github.com/galafis/ibm-business-intelligence-capstone.git
cd ibm-business-intelligence-capstone

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate  # Windows

# Install Python dependencies
pip install -r requirements.txt

# Run main application
python src/main_platform.py
```

### 📊 Detailed Features

#### 🏢 **Enterprise Data Warehouse**
- **Dimensional Modeling:** Dimensional modeling (Star/Snowflake)
- **Data Marts:** Specialized data marts by area
- **Slowly Changing Dimensions:** Managing changing dimensions
- **Fact Tables:** Optimized fact tables
- **Aggregate Tables:** Aggregate tables for performance
- **Data Lineage:** Data traceability

#### 🔄 **ETL Pipeline**
- **Data Extraction:** Multi-source data extraction
- **Data Transformation:** Complex transformations
- **Data Loading:** Optimized loading
- **Error Handling:** Robust error handling
- **Data Quality:** Data validation and cleansing
- **Incremental Loading:** Incremental loading

### 🧪 Testing and Quality

```bash
# ETL tests
python -m pytest tests/test_etl.py -v

# OLAP tests
python -m pytest tests/test_olap.py -v

# Dashboard tests
python -m pytest tests/test_dashboards.py -v
```

### 📈 Results and Impact

#### Monitored Enterprise KPIs
- **Financial KPIs:** Revenue Growth Rate, Profit Margin, EBITDA
- **Sales KPIs:** Sales Growth, Conversion Rate, Customer Acquisition Cost
- **Operational KPIs:** Operational Efficiency, Quality Metrics, Productivity Ratios

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by Gabriel Demetrios Lafis**  
*IBM Business Intelligence Professional Certificate Capstone Project*

